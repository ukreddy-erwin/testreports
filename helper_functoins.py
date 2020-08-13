import xml.etree.ElementTree as obj
import datetime
import mariadb
import glob

import datetime,logging

#pip3 install mariadb

logging.basicConfig(filename='DBImport_Log.log',level=logging.INFO)
def WriteLog(str1):
    d = datetime.datetime.now()
    print(d," : ",str1)
    logging.info(str(d)+" : "+str1)

def process_path(sFile):
    return sFile.replace('\\','/')

def removeLastSlash(st):
    if st[-1] == "/" or st[-1] == "\\":
        st = st[:-1]
    return st

def mariadb_date_format(sDate):
    sDate = sDate.strip()
    if validate(sDate):
        #sDate = '3/1/2020 1:04:46 PM'
        d = datetime.datetime.strptime(sDate,'%m/%d/%Y %I:%M:%S %p')
        return d
    else:
        return sDate


def validate(date_text):
    try:
        datetime.datetime.strptime(date_text, '%m/%d/%Y %I:%M:%S %p')
        return True
    except ValueError:
        return False

def extractSubString(fullstring,substring):
    if substring in fullstring:
        fullstring=fullstring.split(substring)[1]
        if "," in fullstring:
            fullstring = fullstring.split(",")[0]
    else:
        fullstring=""
    return fullstring

def updateXML(element,sType):
    if sType == "GEO":
        updateXMLGEO(element)
    if sType == "ACT":
        updateXMLACT(element)
    if sType == "FEA":
        updateXMLFEA(element)
    if sType == "ENV":
        updateXMLENV(element)
        
def updateXMLGEO(filename):
    tree=obj.ElementTree(file=filename)
    root = tree.getroot()

    for dates in root.iter("Date"):
        dates.text = str(mariadb_date_format(dates.text))

    for dates in root.iter("Created"):
        dates.text = str(mariadb_date_format(dates.text))

    for dates in root.iter("Modified"):
        dates.text = str(mariadb_date_format(dates.text))

    tree=obj.ElementTree(root)

    with open(filename,"wb") as fileupdate:
        tree.write(fileupdate)

#https://youtu.be/9DYYKSYtMuw
#https://docs.python.org/2/library/xml.etree.elementtree.html
def updateXMLACT(filename):
    tree=obj.ElementTree(file=filename)
    root = tree.getroot()
    for item in root.iter("item"):
        child = item.find('Username')
        lc,bn = child.text.split(",")
        lc = lc.replace("LC:","")
        bn = bn.replace("BN:","")
        #print(lc,bn)
        item.remove(child)
        new_child1 = obj.SubElement(item, 'license')
        new_child1.text = lc
        new_child2 = obj.SubElement(item, 'buildnumber')
        new_child2.text = bn
        StartDate = item.find('StartDate')
        StartDate.text = str(mariadb_date_format(StartDate.text))
        EndDate = item.find('EndDate')
        EndDate.text = str(mariadb_date_format(EndDate.text))
        Created = item.find('Created')
        Created.text = str(mariadb_date_format(Created.text))
        Modified = item.find('Modified')
        Modified.text = str(mariadb_date_format(Modified.text))
    
    tree=obj.ElementTree(root)

    with open(filename,"wb") as fileupdate:
        tree.write(fileupdate)
        
def updateXMLFEA(filename):
    tree=obj.ElementTree(file=filename)
    root = tree.getroot()
    for item in root.iter("item"):
        child = item.find('Username')
        lc = extractSubString(child.text,"LC:")
        RE_TY = extractSubString(child.text,"RE_TY:")
        RE_DB = extractSubString(child.text,"RE_DB:")
        #print(lc,bn)
        item.remove(child)
        new_child1 = obj.SubElement(item, 'license')
        new_child1.text = lc
        new_child2 = obj.SubElement(item, 'RE_TY')
        new_child2.text = RE_TY
        new_child3 = obj.SubElement(item, 'RE_DB')
        new_child3.text = RE_DB
        StartDate = item.find('StartDate')
        StartDate.text = str(mariadb_date_format(StartDate.text))
        EndDate = item.find('EndDate')
        EndDate.text = str(mariadb_date_format(EndDate.text))
        Created = item.find('Created')
        Created.text = str(mariadb_date_format(Created.text))
        Modified = item.find('Modified')
        Modified.text = str(mariadb_date_format(Modified.text))
    
    tree=obj.ElementTree(root)

    with open(filename,"wb") as fileupdate:
        tree.write(fileupdate)

def importXML(xml_file,table):
    try:
        xml_file = process_path(xml_file)
        conn = mariadb.connect(
            user="root",
            password="Notallowed1!",
            host="172.168.56.3",
            database="dmlicensedata")
        cur = conn.cursor() 

        #insert information 
        try:
            #xml_file = "C:/temp/GEO_7095_5539_8_1_2020_8_31_2020.XML"
            #table = "dmlicensedata.geo"
            load_xml = "LOAD XML INFILE '"+ xml_file +"' INTO TABLE "+ table +" ROWS IDENTIFIED BY '<item>'"
            WriteLog("Executing: "+ load_xml)
            cur.execute(load_xml) 
        except mariadb.Error as e: 
            WriteLog(f"Error: {e}")

        conn.commit() 
        conn.close()
        WriteLog("Processing ended,connection closed for: "+xml_file)
    except mariadb.Error as e:
        WriteLog(f"Error connecting to MariaDB Platform: {e}")
        sys.exit(1)

def processXML(sFolder,sType):
    elements = glob.glob(sFolder+"\\"+ sType +"_*.xml")
    WriteLog("files found with " + sType + ":"+str(len(elements)))
    print(elements)
    for element in elements:
        if len(element)> len(element.replace(" ", "")):
            WriteLog("Error: Spaces in the filename are not supported")
        else:
            element = process_path(element)
            WriteLog("Processing:" + element)
            importXML(element,"dmlicensedata."+sType)
            updateXML(element,"dmlicensedata."+sType)

if __name__=="__main__":
    xml_folder = r"C:\temp"
    xml_folder = removeLastSlash(xml_folder)
    WriteLog("Started Preprocessing XML files")
    processXML(xml_folder,"GEO")
    processXML(xml_folder,"FEA")
    processXML(xml_folder,"ACT")
    processXML(xml_folder,"ENV")
    WriteLog("Completed importing XML files to Database")
    

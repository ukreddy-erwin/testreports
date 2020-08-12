import xml.etree.ElementTree as obj
import datetime

def mariadb_date_format(sDate):
    sDate = sDate.strip()
    if validate(sDate):
        #sDate = '3/1/2020 1:04:46 PM'
        d = datetime.datetime.strptime(sDate,'%d/%m/%Y %I:%M:%S %p')
        return d
    else:
        return sDate


def validate(date_text):
    try:
        datetime.datetime.strptime(date_text, '%d/%m/%Y %I:%M:%S %p')
        return True
    except ValueError:
        return False

#https://youtu.be/9DYYKSYtMuw
def updateXML(filename):
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

if __name__=="__main__":
    updateXML(r"C:\users\UdayKiranReddy\Desktop\Customer4.xml")

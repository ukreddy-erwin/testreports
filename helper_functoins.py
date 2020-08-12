def mariadb_date_format(sDate):
    sDate = sDate.strip()
    import datetime
    #sDate = '3/1/2020 1:04:46 PM'
    d = datetime.datetime.strptime(sDate,'%d/%m/%Y %I:%M:%S %p')
    return d

print(mariadb_date_format('3/1/2020 1:04:46 PM'))
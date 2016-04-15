import MySQLdb

sql = """
select * from sensorhistorian where SensorID='SGS10031' and Datetime>'2016-04-14' ORDER BY Datetime DESC
"""

print "ID        SensorID       Datetime      Longitude  Latitude   Battery" 
try:
    conn=MySQLdb.connect(host='local',user='root',passwd='root',db='sensor',port=3306)
    cur=conn.cursor()
    cur.execute(sql)
    results = cur.fetchall()
    for row in results:
        ID = row[0]
        SensorID = row[1]
        Datetime = row[2]
        Longitude = row[3]
        Latitude = row[4]
        Battery = row[17]
        print ID,SensorID,Datetime,Longitude,Latitude,Battery
    cur.close()
    conn.close()
except MySQLdb.Error,e:
     print "Mysql Error %d: %s" % (e.args[0], e.args[1])
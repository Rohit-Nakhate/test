import pymssql 
#create config file for global variables 
server=""
user=""
password=""
tempdb=""

conn = pymssql.connect(server, user, password, "tempdb")
cursor = conn.cursor(as_dict=True)

cursor.execute('SELECT * FROM persons WHERE salesrep=%s', 'Mike Tyson')
for row in cursor:
    print("ID=%d, Name=%s" % (row['id'], row['name']))

conn.close()
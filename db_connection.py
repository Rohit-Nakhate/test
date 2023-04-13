import pyodbc as odbc

DEIVER_NAME=""
SERVERNAME=""
DATABASE_NAME=""

connection_string = f""" DRIVER_NAME={{DRIVER_NAME}};
                    SERVER_NAME={{DRIVER_NAME}};DATABASE_NAME={{DRIVER_NAME}};"""

conn = odbc.connect(connection_string)
print(conn)
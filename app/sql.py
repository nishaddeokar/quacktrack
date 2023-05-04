import sqlite3

# MAKE CONNECTION TO DATABASE
con = sqlite3.connect("out.db")
print("Opened database successfully")

con.execute('''CREATE TABLE IF NOT EXISTS HEALTH_DATA
         (ID DATE PRIMARY KEY      NOT NULL,
         STEP           INT    NOT NULL,
         STEP_TARGET            INT     NOT NULL,
         WEIGHT           FLOAT     NOT NULL,
         WEIGHT_TARGET           FLOAT     NOT NULL,
         HEIGHT           FLOAT     NOT NULL,
         LEVEL            INT     NOT NULL)''')

print("Table created successfully")


con.execute("INSERT OR REPLACE INTO HEALTH_DATA (ID,STEP,STEP_TARGET,WEIGHT,WEIGHT_TARGET,HEIGHT,LEVEL) \
      VALUES ('2023-04-25', 2400, 0, 59, 0, 0, 1)")

con.execute("INSERT OR REPLACE INTO HEALTH_DATA (ID,STEP,STEP_TARGET,WEIGHT,WEIGHT_TARGET,HEIGHT,LEVEL) \
      VALUES ('2023-04-26', 2600, 0, 59, 0, 0, 1)")

con.execute("INSERT OR REPLACE INTO HEALTH_DATA (ID,STEP,STEP_TARGET,WEIGHT,WEIGHT_TARGET,HEIGHT,LEVEL) \
      VALUES ('2023-04-27', 2700, 0, 60, 0, 0, 1)")

con.execute("INSERT OR REPLACE INTO HEALTH_DATA (ID,STEP,STEP_TARGET,WEIGHT,WEIGHT_TARGET,HEIGHT,LEVEL) \
      VALUES ('2023-04-28', 3500, 0, 59.5, 0, 0, 1)")

con.execute("INSERT OR REPLACE INTO HEALTH_DATA (ID,STEP,STEP_TARGET,WEIGHT,WEIGHT_TARGET,HEIGHT,LEVEL) \
      VALUES ('2023-04-29', 3200, 0, 58.5, 0, 0, 1)")

con.execute("INSERT OR REPLACE INTO HEALTH_DATA (ID,STEP,STEP_TARGET,WEIGHT,WEIGHT_TARGET,HEIGHT,LEVEL) \
      VALUES ('2023-04-30', 3900, 0, 58, 0, 0, 1)")

con.execute("INSERT OR REPLACE INTO HEALTH_DATA (ID,STEP,STEP_TARGET,WEIGHT,WEIGHT_TARGET,HEIGHT,LEVEL) \
      VALUES ('2023-05-01', 4300, 0, 58.5, 0, 0, 1)")

con.execute("INSERT OR REPLACE INTO HEALTH_DATA (ID,STEP,STEP_TARGET,WEIGHT,WEIGHT_TARGET,HEIGHT,LEVEL) \
      VALUES ('2023-05-02', 5000, 0, 57, 0, 0, 1)")

con.execute("INSERT OR REPLACE INTO HEALTH_DATA (ID,STEP,STEP_TARGET,WEIGHT,WEIGHT_TARGET,HEIGHT,LEVEL) \
      VALUES ('2023-05-03', 4800, 0, 57, 0, 0, 29)")

con.commit()
print("Records created successfully")

sql_query = """SELECT * FROM HEALTH_DATA;"""

cursor = con.cursor()

cursor.execute(sql_query)
print("List of tables\n")
print(cursor.fetchall())

con.close()
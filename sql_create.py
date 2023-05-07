#CREATE A TABLE
conn = psycopg2.connect(database = "a", user = "a", password = "1", host = "127.0.0.1", port = "5432")
cur = conn.cursor()

cur.execute('''CREATE TABLE stocks
      (ID INT PRIMARY KEY     NOT NULL,
      ticker         TEXT    NOT NULL,
      boughtprice    INT     NOT NULL,
      quantity       INT     NOT NULL,
      boughtprice    INT,
	  soldprice      REAL,
	  soldpricetotal REAL,
	  percentagegrow INT,
	  moneygrow      INT);''')
print("Table created successfully")
cur.execute('''CREATE SEQUENCE sequence1
INCREMENT 1
START 1;''')
print("SEQUENCE created successfully")
conn.commit()

conn.close()
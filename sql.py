import psycopg2

database = "a"
user = "a"
password = "1"

def select():
    #print("SELECTING")
    conn = psycopg2.connect(database=database, user=user, password=password, host="127.0.0.1", port="5432")
    cur = conn.cursor()
    cur.execute("SELECT *  from stocks")
    rows = cur.fetchall()
    for row in rows:
        print("ID = ", row[0], ", TICKER = ", row[1],
              ", BOUGHTPRICE = ", row[2], ", QUANTITY = ", row[3],
              ", SOLDPRICE = ", row[5], ", BoughtPriceTotal = ",
              row[4], ", SoldPriceTotal = ",row[6],
              ", PercentageGrow,% = ",row[7], ", MoneyGrow = ",
              row[8])
    conn.close()

def insert():
    print("INSERTING")
    conn = psycopg2.connect(database=database, user=user, password=password, host="127.0.0.1", port="5432")
    cur = conn.cursor()

    ticker = input("Enter TICKER ")
    boughtprice = int(input("Enter BoughtPrice "))
    quantity = int(input("Enter Quantity "))
    soldprice = int(input("Enter SoldPrice (Leave blank if u haven't sold) "))
    boughtpricetotal = boughtprice * quantity
    if soldprice:
        soldpricetotal = int(soldprice) * quantity
        percentagegrow = 100 - (boughtpricetotal * 100 / soldpricetotal)
        moneygrow = soldpricetotal - boughtpricetotal

        #nextval -IS AUTOINCREMENT FIELD, sequence1 - is SEQUENCE IN DB

        sql_query = "INSERT INTO stocks (ID, TICKER, BOUGHTPRICE, QUANTITY, SOLDPRICE, BoughtPriceTotal, SoldPriceTotal, PercentageGrow, MoneyGrow) VALUES (nextval('sequence1'),'{}',{},{},{},{},{},{},{})".format(ticker, boughtprice, quantity, soldprice, boughtpricetotal, soldpricetotal, percentagegrow, moneygrow)
    else:
        sql_query = "INSERT INTO stocks (ID, TICKER, BOUGHTPRICE, QUANTITY, BoughtPriceTotal) VALUES (nextval('sequence1'),'{}',{},{},{})".format(ticker, boughtprice, quantity, boughtpricetotal)
    cur.execute(sql_query)

    conn.commit()
    cur.execute("SELECT *  from stocks")
    rows = cur.fetchall()
    for row in rows:
        print("ID = ", row[0], ", TICKER = ", row[1],
              ", BOUGHTPRICE = ", row[2], ", QUANTITY = ", row[3],
              ", SOLDPRICE = ", row[5], ", BoughtPriceTotal = ",
              row[4], ", SoldPriceTotal = ", row[6],
              ", PercentageGrow,% = ", row[7], ", MoneyGrow = ",
              row[8])
    conn.close()

def delete():
    print("DELETING")
    conn = psycopg2.connect(database=database, user=user, password=password, host="127.0.0.1", port="5432")
    cur = conn.cursor()
    sql_query = "DELETE from stocks where TICKER='{}';"
    x = sql_query.format(input("Enter TICKER to delete a stock "))
    cur.execute(x)
    conn.commit()
    print("Total number of rows deleted :", cur.rowcount)

    cur.execute("SELECT *  from stocks")
    rows = cur.fetchall()
    for row in rows:
        print("ID = ", row[0], ", TICKER = ", row[1],
              ", BOUGHTPRICE = ", row[2], ", QUANTITY = ", row[3],
              ", SOLDPRICE = ", row[5], ", BoughtPriceTotal = ",
              row[4], ", SoldPriceTotal = ", row[6],
              ", PercentageGrow,% = ", row[7], ", MoneyGrow = ",
              row[8])
    conn.close()

def update():
    print("UPDATING")
    conn = psycopg2.connect(database=database, user=user, password=password, host="127.0.0.1", port="5432")
    cur = conn.cursor()

    sql_query = "UPDATE stocks SET {} = '{}' where TICKER = '{}'"
    x = sql_query.format(input("Enter Column Name "), input("Enter New_Value "), input("Enter TICKER of stock "))
    cur.execute(x)
    conn.commit()

    cur.execute("SELECT *  from stocks")
    rows = cur.fetchall()
    for row in rows:
        print("ID = ", row[0], ", TICKER = ", row[1],
              ", BOUGHTPRICE = ", row[2], ", QUANTITY = ", row[3],
              ", SOLDPRICE = ", row[5], ", BoughtPriceTotal = ",
              row[4], ", SoldPriceTotal = ", row[6],
              ", PercentageGrow,% = ", row[7], ", MoneyGrow = ",
              row[8])
    conn.close()
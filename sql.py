import psycopg2
import pika, os, logging

def select():
    print("SELECTING")
    conn = psycopg2.connect(database="testdb1", user="postgres", password="1", host="127.0.0.1", port="5432")
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
    conn = psycopg2.connect(database="testdb1", user="postgres", password="1", host="127.0.0.1", port="5432")
    cur = conn.cursor()

    a=input("Enter TICKER ")
    b=int(input("Enter BP "))
    q=int(input("Enter Quantity "))
    s=input("Enter SP (Leave blank if u haven't sold) ")
    bpt=b*q
    if s:
        spt=int(s)*q
        pg=100-(bpt*100/spt)
        mg=spt-bpt
        sql = "INSERT INTO stocks (ID,TICKER,BOUGHTPRICE,QUANTITY,SOLDPRICE,BoughtPriceTotal,SoldPriceTotal,PercentageGrow,MoneyGrow) VALUES (nextval('shares'),'{}',{},{},{},{},{},{},{})".format(a,b,q,s,bpt,spt,pg,mg)
    else:
        sql = "INSERT INTO stocks (ID,TICKER,BOUGHTPRICE,QUANTITY,BoughtPriceTotal) VALUES (nextval('shares'),'{}',{},{},{})".format(a, b, q, bpt)
    cur.execute(sql)

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
    conn = psycopg2.connect(database="testdb1", user="postgres", password="1", host="127.0.0.1", port="5432")
    cur = conn.cursor()
    sql = "DELETE from stocks where TICKER='{}';"
    x=sql.format(input("Enter TICKER to delete a stock "))
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
    conn = psycopg2.connect(database="testdb1", user="postgres", password="1", host="127.0.0.1", port="5432")
    cur = conn.cursor()

    sql = "UPDATE stocks set {} = '{}' where TICKER = '{}'"
    x=sql.format(input("Enter Column "),input("Enter New_Value "),input("Enter TICKER of stock "))
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

def sendmsg():
    logging.basicConfig()

    url = os.environ.get('CLOUDAMQP_URL',
                         'amqps://')
    params = pika.URLParameters(url)
    params.socket_timeout = 5

    connection = pika.BlockingConnection(params)
    channel = connection.channel()
    channel.queue_declare(queue='MyQueue1')

    print("Preparing to send msg ...")
    channel.basic_publish(exchange='', routing_key='MyQueue1', body=input("Enter msg "))
    print("[x] Message sent to consumer")
    connection.close()
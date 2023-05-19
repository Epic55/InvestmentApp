import psycopg2

database = "a"
user = "a"
password = "1"

conn = psycopg2.connect(database=database, user=user, password=password, host="127.0.0.1", port="5432")
cur = conn.cursor()

class StockClass:

    def __init__(self, ticker, boughtprice, quantity, soldprice):
        self.id = None
        self.ticker = ticker
        self.boughtprice = boughtprice
        self.quantity = quantity
        self.soldprice = soldprice

    def save(self, ticker, boughtprice, quantity, soldprice):

        if soldprice:
            soldpricetotal = int(soldprice) * quantity
            boughtpricetotal = boughtprice * quantity
            percentagegrow = 100 - (boughtpricetotal * 100 / soldpricetotal)
            moneygrow = soldpricetotal - boughtpricetotal
            sql = "INSERT INTO stocks (ID, TICKER, BOUGHTPRICE, QUANTITY, SOLDPRICE, BoughtPriceTotal, SoldPriceTotal, PercentageGrow, MoneyGrow) VALUES (nextval('sequence1'),'{}',{},{},{},{},{},{},{})".format(
                self.ticker, self.boughtprice, self.quantity, self.soldprice, boughtpricetotal, soldpricetotal, percentagegrow, moneygrow)
        else:
            boughtpricetotal = boughtprice * quantity
            sql = "INSERT INTO stocks (ID, TICKER, BOUGHTPRICE, QUANTITY, BoughtPriceTotal) VALUES (nextval('sequence1'),'{}',{},{},{})".format(self.ticker, self.boughtprice, self.quantity, boughtpricetotal)

        cur.execute(sql)
        conn.commit()

    @classmethod
    def create(cls, ticker, boughtprice, quantity, soldprice):
        song = StockClass(ticker, boughtprice, quantity, soldprice)
        song.save(ticker, boughtprice, quantity, soldprice)
        return song

StockClass.create(input("Enter TICKER "),
                  int(input("Enter BoughtPrice ")),
                  int(input("Enter Quantity ")),
                  input("Enter SoldPrice (Leave blank if u haven't sold) "))
from tkinter import *
import tkinter as tk
import psycopg2
from sqlalchemy import create_engine

database = "a"
user = "a"
password = "1"

def gui():
    my_w = tk.Tk()
    my_w.geometry("900x200")
    conn = psycopg2.connect(database=database, user=user, password=password, host="127.0.0.1", port="5432")
    my_conn = conn.cursor()
   # cur.execute("SELECT *  from stocks")
   # my_conn = create_engine("postgresql://a:1@127.0.0.1/a")
    r_set = my_conn.execute("SELECT *  from stocks")



    e=Label(my_w,width=13,text='ID',borderwidth=2, relief='ridge',anchor='center',font="Helvetica 8 bold")
    e.grid(row=0,column=0)
    e=Label(my_w,width=13,text='Ticker',borderwidth=2, relief='ridge',anchor='center',font="Helvetica 8 bold")
    e.grid(row=0,column=1)
    e=Label(my_w,width=13,text='BoughtPrice',borderwidth=2, relief='ridge',anchor='center',font="Helvetica 8 bold")
    e.grid(row=0,column=2)
    e=Label(my_w,width=13,text='Quantity',borderwidth=2, relief='ridge',anchor='center',font="Helvetica 8 bold")
    e.grid(row=0,column=3)
    e=Label(my_w,width=13,text='SoldPrice',borderwidth=2, relief='ridge',anchor='center',font="Helvetica 8 bold")
    e.grid(row=0,column=4)
    e=Label(my_w,width=14,text='BoughtPriceTotal',borderwidth=2, relief='ridge',anchor='center',font="Helvetica 8 bold")
    e.grid(row=0,column=5)
    e=Label(my_w,width=13,text='SoldPriceTotal',borderwidth=2, relief='ridge',anchor='center',font="Helvetica 8 bold")
    e.grid(row=0,column=6)
    e=Label(my_w,width=13,text='PercentageGrow',borderwidth=2, relief='ridge',anchor='center',font="Helvetica 8 bold")
    e.grid(row=0,column=7)
    e=Label(my_w,width=13,text='MoneyGrow',borderwidth=2, relief='ridge',anchor='center',font="Helvetica 8 bold")
    e.grid(row=0,column=8)

    i = 1
    for stocks in r_set:
        for j in range(len(stocks)):
            e = Label(my_w,width=13, text=stocks[j],borderwidth=2,relief='ridge', anchor="center")
            e.grid(row=i, column=j)
        i = i + 1
    my_w.mainloop()
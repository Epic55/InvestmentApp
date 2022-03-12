from sql import *
from tk import *
from api import *
from rabbitmq import *

def f(agrument):
    match agrument:
        case "1": return select()
        case "2": return insert()
        case "3": return delete()
        case "4": return update()
        case "5": return sendmsg()
        case "6": return gui()
        case "7": return getapi()
        case "8": exit()
for i in iter(int,1):
    print("\n","Choose number what u want to do: ")
    print(" 1 - show all shares, 2 - insert data about new share, 3 - delete data about share,","\n",
          "4 - update data about share, 5 - send msg via rabbitmq, 6 - launch GUI,","\n",
          "7 - use api to get info about company, 8 - exit")
    f(input("Enter number: "))
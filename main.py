from sql import *

def f(agrument):
    match agrument:
        case "1": return select()
        case "2": return insert()
        case "3": return delete()
        case "4": return update()
        case "5": exit()
for i in iter(int,1):
    print("\n","Choose number what u want to do: ")
    print("1 - show all shares, 2 - insert data about new share, 3 - delete data about share, 4 - update data about share, 5 - exit from programm")
    f(input("Enter number: "))
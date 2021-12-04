print("Health Management System")
r= input("What you want to do: retreive/locked : ")
if r == "retreive":
    s=input("Who are you : ")
    if s=="1":
        n=input("Press 1 for Diet and 2 for Exercise : ")
        if n=="1":
            d=open("harry diet.txt")
            print(d.read())
        else:
            d=open("harry exe.txt")
            print(d.read())
    elif s=="2":
        m = input("Press 1 for Diet and 2 for Exercise : ")
        if m == "1":
            d = open("asif diet.txt")
            print(d.read())
        else:
            d = open("asif exe.txt")
            print(d.read())
    elif s=="3":
        h = input("Press 1 for Diet and 2 for Exercise : ")
        if h == "1":
            d = open("hammad diet.txt")
            print(d.read())
        else:
            d = open("hammad exe.txt")
            print(d.read())

elif r=="locked":
    def getdate(q):
        import datetime
        return datetime.datetime.now()
    t=input("Who are you? : ")
    if t=="1":
        q=input("Press 1 for Diet and 2 for Exercise : ")
        if q=="1":
            y=open("harry diet.txt","r+")
            print(y.read())
            print(getdate(q), end=" ")
            b=input()
            print(y.write(b), end=" ")
        else:
            y=open("harry exe.txt","r+")
            print(y.read())
            print(getdate(q), end=" ")
            v=input()
            print(y.write(v), end=" ")
    elif t == "2":
        q = input("Press 1 for Diet and 2 for Exercise : ")
        if q == "1":
            y = open("asif diet.txt", "r+")
            print(y.read())
            print(getdate(q), end=" ")
            b = input()
            print(y.write(b), end=" ")
        else:
            y = open("asif exe.txt", "r+")
            print(y.read())
            print(getdate(q), end=" ")
            v = input()
            print(y.write(v), end=" ")
    elif t == "3":
        q = input("Press 1 for Diet and 2 for Exercise : ")
        if q == "1":
            y = open("hammad diet.txt", "r+")
            print(y.read())
            print(getdate(q), end=" ")
            b = input()
            print(y.write(b), end=" ")
        else:
            y = open("hammad exe.txt", "r+")
            print(y.read())
            o=getdate(q)
            print(o, end=" ")
            v = input()
            print(y.write(v), end=" ")
            input("Press Enter to close")
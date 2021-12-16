import csv
def getID(username):
    with open("users.csv","r") as f:
        reader = csv.reader(f)
        for x in reader:
            if username in x:
                return int(x[0])
def games(ID):
    with open("users.csv","r") as f:
        reader = csv.reader(f)
        for x in reader:
            if str(ID) in x:
                return int(x[3])
def wins(ID):
    with open("users.csv","r") as f:
        reader = csv.reader(f)
        for x in reader:
            if str(ID) in x:
                return int(x[2])
def losses(ID):
    with open("users.csv","r") as f:
        reader = csv.reader(f)
        for x in reader:
            if str(ID) in x:
                return int(int(x[3])-int(x[2]))
def username(ID):
    with open("users.csv","r") as f:
        reader = csv.reader(f)
        for x in reader:
            if str(ID) in x:
                return x[1]
def balance(ID):
    with open("users.csv","r") as f:
        reader = csv.reader(f)
        for x in reader:
            if str(ID) in x:
                return int(x[4])
def checker(user):
    with open("users.csv","r") as f:
        reader = csv.reader(f)
        for row in reader:

            if user in row:
                return True
        return False
def giveCoin(user,amount):
    rows = list()
    with open("users.csv","r") as f:
        reader = csv.reader(f)
        for row in reader:
            rows.append(row)
        for x in rows:
            if str(user) in x:
                temp = int(x[4])
                x[4] = str(temp + amount)
    print(rows)
    with open("users.csv","w",newline='') as c:
        writer = csv.writer(c)
        for x in rows:
            writer.writerow(x)
def addWin(user,num):
    rows = list()
    with open("users.csv","r") as f:
        reader = csv.reader(f)
        for row in reader:
            rows.append(row)
        for x in rows:
            if str(user) in x:
                temp = int(x[2])
                x[2] = str(temp + num)
                temp = int(x[3])
                x[3] = str(temp + 1)

    with open("users.csv","w",newline='') as c:
        writer = csv.writer(c)
        for x in rows:
            writer.writerow(x)

def write(user):
    with open("users.csv","a",newline='') as f:
        writer = csv.writer(f)
        writer.writerow(user)

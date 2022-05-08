import sqlite3 as sq

db = sq.connect("material.db")
cr = db.cursor()
x = []

a = cr.execute("select day, class, eight from materials where eight='Programming'")
af = cr.fetchall()#.append(" 8 - 10 ")
af.append(" 8 - 10 ")
b = cr.execute("select day, class, ten from materials where ten='Programming'")
bf = cr.fetchall()#.append(" 10 - 12 ")
bf.append(" 10 - 12 ")
c = cr.execute("select day, class, twelve from materials where twelve='Programming'")
cf = cr.fetchall()#.append(" 12 - 2 ")
cf.append(" 12 - 2 ")
d = cr.execute("select day, class, two from materials where two='Programming'")
df = cr.fetchall()#.append(" 2 - 4 ")
df.append(" 2 - 4 ")
e = cr.execute("select day, class, four from materials where four='Programming'")
ef = cr.fetchall()#.append(" 4 - 6 ")
ef.append(" 4 - 6 ")
x.append(af)
x.append(bf)
x.append(cf)
x.append(df)
x.append(ef)

for i, b in enumerate(x):
    # for i, b in enumerate(a):
    # print(f" {a} ")
        if i>5:
            print(b, end=", ")
        elif len(b) != 1:
            if i == 0 :#and b == 'Programming'
                print(f"{b} lllll")
            elif i == 1:#and b == 'Programming'
                print(f"{b} hhhh")
            elif i == 2:#and b == 'Programming'
                print(f"{b} nnnnn")
            elif i == 3:#and b == 'Programming'
                print(f"{b} xxxxx")
            elif i == 4 :#and b == 'Programming'
                print(f"{b} aaaaa")

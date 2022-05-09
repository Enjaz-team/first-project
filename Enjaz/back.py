import sqlite3 as sq
from flask import Flask, render_template

main_app = Flask(__name__)

m = ['p']
db = sq.connect("material.db")
cr = db.cursor()
x = []

a = cr.execute(f"select day, class, eight from materials where eight='{m[0]}'")
af = cr.fetchall()
af.append(" 8 - 10 ")
b = cr.execute(f"select day, class, ten from materials where ten='{m[0]}'")
bf = cr.fetchall()
bf.append(" 10 - 12 ")
c = cr.execute(f"select day, class, twelve from materials where twelve='{m[0]}'")
cf = cr.fetchall()
cf.append(" 12 - 2 ")
d = cr.execute(f"select day, class, two from materials where two='{m[0]}'")
df = cr.fetchall()
df.append(" 2 - 4 ")
e = cr.execute(f"select day, class, four from materials where four='{m[0]}'")
ef = cr.fetchall()
ef.append(" 4 - 6 ")
x.append(af)
x.append(bf)
x.append(cf)
x.append(df)
x.append(ef)

for i, b in enumerate(x):
    if i>5:
        print(b, end=", ")
    elif len(b) != 1:
        if i == 0 :
            print(f"{b} lllll")
        elif i == 1:
            print(f"{b} hhhh")
        elif i == 2:
            print(f"{b} nnnnn")
        elif i == 3:
            print(f"{b} xxxxx")
        elif i == 4 :
            print(f"{b} aaaaa")

@main_app.route("/")
def front():
    return render_template("front.html",
                           title="homepage")

if __name__ == "__main__":
    main_app.run(debug=True, port=8000)
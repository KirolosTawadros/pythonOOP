import sqlite3

db = sqlite3.connect("app.db")

cr = db.cursor()

cr.execute(
    "CREATE TABLE if not exists users (user_id INTEGER, name TEXT)")

cr.execute(
    "CREATE TABLE if not exists skills(name TEXT, progress INT, user_id INTEGER)")

# cr.execute("insert into users (user_id,name) values(1,'ahmed')")
# cr.execute("insert into users (user_id,name) values(2,'gamal')")
# cr.execute("insert into users (user_id,name) values(3,'mahmoud')")

my_list = ["ahmed", "sayed", "Ali", "Kirolos", "Ahmed"]

for key, user in enumerate(my_list):

    cr.execute(f"insert into users(user_id,name) values({key + 1},'{user}')")

db.commit()

db.close()

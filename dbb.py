import sqlite3
#query the DB and return all the records
def show_all():
#connect to database
	conn = sqlite3.connect('moviess.db')
#create a cursor
	c = conn.cursor()
	c.execute("SELECT rowid, * FROM moviess")
	items = c.fetchall()

	for item in items:
		print(item)
	conn.commit()

#close our connection

	conn.close()

def add_one(Name,Actor,Actress,Director,Year of Release):
	conn = sqlite3.connect('moviess.db')
	c = conn.cursor()
	c.execute("INSERT INTO movie VALUES (?,?,?,?,?)", (Name, Actor, Actress, Director,Year of Release))
	conn.commit()
	conn.close()
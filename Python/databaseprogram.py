import sqlite3
class data:
	def meth(self):
		self.conn = sqlite3.connect('sample2.db')
		self.c = self.conn.cursor()
		self.conn.commit()
	def create(self):
		# Create table
		self.c.execute('''CREATE TABLE if not exists student1 (Name varchar(30),Rollno varchar(30),Subject1 integer,Subject2 integer,Subject3 integer)''')
		self.conn.commit()
	def get_values_for_insert(self):
		# Insert a row of data
		n=int(input('Enter the number of records : '))
		dict={}
		for ran in range(n):
			name=str(input('Enter name : '))
			rno=str(input('Enter roll number : '))
			m1=int(input('Enter mark in subject 1 : '))
			m2=int(input('Enter mark in subject 2 : '))
			m3=int(input('Enter mark in subject 3 : '))
			d.add(name)
			d.add(rno)
			d.add(m1)
			d.add(m2)
			d.add(m3)
		self.c.executemany("INSERT INTO student1 VALUES (%s,%s,%s,%s,%s)",d)
		self.conn.commit()
	def fetchres(self):
		self.c.execute('SELECT count(*) FROM student1')
		print self.c.fetchone()
		self.conn.commit()
	def update(self):
		self.c.execute("update student1 set subject3=100 where Name='Srikantan'")
		for row in self.c.execute('SELECT * FROM student1'):
				print self.c.fetchone()
		self.conn.commit()
	def endcon(self):
		self.conn.close()
object=data()
object.meth()
object.create()
object.get_values_for_insert()
object.fetchres()
object.update()
object.endcon()
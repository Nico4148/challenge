import sqlite3

def insert_data(single_cmd):
	conn=sqlite3.connect('/var/www/lab_app/challenge.db')
	curs=conn.cursor()
	curs.execute(single_cmd)
	conn.commit()
	conn.close()

'''
[Student]
Code Name Email Address Phone DateOfBirth
'''
buffer_cmd = '''
	INSERT INTO Student
	VALUES(
		95562304,
		'Nicolas Bernal',
		'nicobernal187@gmail.com',
		'Bernardo Houssay 1042',
		1154711031,
		'1989-12-18'
	); '''
insert_data(buffer_cmd)

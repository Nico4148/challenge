import sqlite3

def execute_cmd_list(str_list):
	for i in str_list:
		conn=sqlite3.connect('/var/www/lab_app/challenge.db')
		curs=conn.cursor()
		curs.execute(i)
		conn.commit()
		conn.close()

cmd_string_list = []
course_list = [
	'Calculo I', 
	'Calculo II', 
	'Calculo III', 
	'Fisica I', 
	'Fisica II', 
	'Variable Compleja'
	]
for index, value in enumerate(course_list):
	buffer_cmd = '''
		INSERT INTO Course
		VALUES(
			%s,
			'%s'
		); ''' %(index, value)
	cmd_string_list.append(buffer_cmd)

execute_cmd_list(cmd_string_list)

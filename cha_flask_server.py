from flask import Flask, render_template, session, request, jsonify
import sqlite3
from flask_json import json_response,FlaskJSON
import json

app = Flask(__name__)
FlaskJSON(app)

app.debug = False
app.secret_key = 'none'

enable_web = False

str_ip = '192.168.0.251'

@app.route("/cha_api_get_student_by_id/<student_id>")
def get_student_by_id(student_id):
    conn=sqlite3.connect('/cha/challenge.db')
    curs=conn.cursor()
    str_query = '''
        SELECT *
        FROM Student AS s
        WHERE s.Code = '%s' ;
    ''' % student_id
    result = curs.execute(str_query)
    data = ''
    for i in result:
        data += str(i)# + '_'
    conn.close()
    if not data:
        data = 'not found'
    return json_response(student_data = data)

@app.route("/cha_api_get_course/<course_id>")
def get_course_by_id(course_id = ''):
    conn=sqlite3.connect('/cha/challenge.db')
    curs=conn.cursor()
    str_query = '''
        SELECT *
        FROM Course AS c
        WHERE c.Code = '%s'
    ''' % course_id
    result = curs.execute(str_query)
    data = ''
    for i in result:
        data += str(i)
    conn.close()
    if not data:
        data = 'not found'
    return json_response(student_data = data)

@app.route("/cha_api_create_student/<student_data>")
def get_create_student(student_data):
    student_data_list = student_data.split('_')
    data = 'pass'
    if len(student_data_list) != 7:
        return json_response(student_data = 'error data lenght')
    else:

        def check_string(str_attr):
            for char in str_attr:
                if char.isdigit():
                    return False
            return True

        def check_date(str_date):
            return True

        def check_student_database(student_code):
            conn=sqlite3.connect('/cha/challenge.db')
            curs=conn.cursor()
            str_query = '''
                SELECT *
                FROM Student AS s
                WHERE s.Code = '%s' ;
            ''' % student_code
            result = curs.execute(str_query)
            data = ''
            for i in result:
                data += str(i)
            conn.close()
            return data
        def commit_new_student(data):
            buffer_cmd = ''' INSERT INTO Student VALUES(%s,'%s %s','%s','%s',%s,'%s'); ''' %(data[0],data[1],data[2],data[3],data[4], data[5], data[6])
            conn=sqlite3.connect('/cha/challenge.db')
            curs=conn.cursor()
            curs.execute(buffer_cmd)
            conn.commit()
            conn.close()
            return
        Code = student_data_list[0]
        if not Code.isnumeric() or len(Code) != 8:
            return json_response(student_data = 'error student code')

        Name = student_data_list[1]

        if not check_string(Name):
            return json_response(student_data = 'error student name')

        LastName = student_data_list[2]
        if not check_string(LastName):
            return json_response(student_data = 'error student last name')

        Email = student_data_list[3]
        if '@' not in Email:
            return json_response(student_data = 'error student email')

        Address = student_data_list[4]

        Phone = student_data_list[5]
        if not Phone.isnumeric() or len(Phone) != 10:
            return json_response(student_data = 'error student phone')

        DateOfBirth = student_data_list[6]
        if not check_date(DateOfBirth):
            return json_response(student_data = 'error student date of birth')

        data = check_student_database(Code)
        if data:
            return json_response(student_data = 'error student %s allready exists' %Code)

        data = []
        data.append(Code)
        data.append(Name)
        data.append(LastName)
        data.append(Email)
        data.append(Address)
        data.append(Phone)
        data.append(DateOfBirth)
        commit_new_student(student_data_list)
        return json_response(student_data = 'new student saved')

    return json_response(student_data = data)

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=8080)

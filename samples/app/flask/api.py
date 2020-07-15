# python3 -m venv venv
# . venv/bin/activate activate
# pip install mariadb flask

import sys
import flask
from flask import request
import json
import mariadb

app = flask.Flask(__name__)
app.config["DEBUG"] = True

config = {
    'host': '127.0.0.1',
    'user': 'app_user',
    'password': 'Password123!',
    'database': 'todo'
}

@app.route('/api/tasks', methods=['GET','POST','PUT','DELETE'])
def index():
   conn = mariadb.connect(**config)
   cur = conn.cursor()

   json_data = []

   if request.method == 'GET':
    cur.execute("select * from tasks order by id desc")
    row_headers=[x[0] for x in cur.description] 
    for result in cur:
        json_data.append(dict(zip(row_headers,result)))

   if request.method == 'POST':
       description = request.json['description']
       cur.execute("insert into tasks (description) values (?)",[description])
       json_data = { 'success': True }

   if request.method == 'PUT':
       id = request.json['id']
       completed = request.json['completed']
       cur.execute("update tasks set completed = ? where id = ?", [completed,id])
       json_data = { 'success': True }

   if request.method == 'DELETE':
       id = request.args.get('id')
       cur.execute("delete from tasks where id = ?",[id])
       json_data = { 'success': True }

   return json.dumps(json_data)

app.run(port=8080)



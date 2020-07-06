#!flask/bin/python
from flask import Flask, jsonify, abort, request
import pandas as pd
from sqlalchemy import create_engine

app = Flask(__name__)

@app.route('/todo/api/tasks', methods=['GET'])
def get_tasks():
    con_str = 'mysql+pymysql://dev:ax2@localhost:3307/test'
    engine = create_engine(con_str)
    df = pd.read_sql_table('statskode', con=engine)
    return df.to_html()


@app.route('/todo/api/tasks/<int:task_id>', methods=['GET'])
def get_task(task_id):
    task = [task for task in tasks if task['id'] == task_id]
    if len(task) == 0:
        abort(404)
    return jsonify({'task': task[0]})

if __name__ == '__main__':
    app.run(debug=True)


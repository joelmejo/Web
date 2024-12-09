from flask import Flask, jsonify, render_template
import psycopg

app = Flask(__name__)

db_config: dict = {
    'host': 'localhost',
    'port': '5432',
    'dbname': 'accademia',
    'user': 'postgres',
    'password': 'postgres'
}

def db_connection():
    connection = psycopg.connect(
        dbname = db_config['dbname'],
        host = db_config['host'],
        user = db_config['user'],
        password = db_config['password']
    )
    return connection

@app.route('/', methods=['GET'])
def benvenuto():
    return render_template('index.html')

@app.route('/query', methods=['GET'])
def query():
    connection = db_connection()
    try:
        cursor = connection.cursor()
        queri = '''SELECT * FROM assenza;'''
        cursor.execute(queri)
        records = cursor.fetchall()
    finally:
        connection.close()
    return jsonify(records)

if __name__ == '__main__':
    app.run(host="127.0.0.1", port=8080, debug=True)


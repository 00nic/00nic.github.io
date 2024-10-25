from flask import Flask, render_template, redirect, flash, url_for, request
from flask_mysqldb import MySQL
from dotenv import load_dotenv
import os

app = Flask(__name__)

load_dotenv

app.config['MYSQL_DB']= os.getenv('MYSQL_DB')
app.config['MYSQL_HOST']= os.getenv('MYSQL_HOST')
app.config['MYSQL_USER']= os.getenv('MYSQL_USER')
app.config['MYSQL_PASSWORD']= os.getenv('MYSQL_PASSWORD')
app.config['MYSQL_CURSORCLASS']= 'DictCursor'
app.config['SECRET_KEY']= '4848'

mysql = MySQL(app)


@app.route('/portfolio', defaults= {'id_proyecto' : None})
@app.route('/portfolio/<id_proyecto>')
def portfolio(id_proyecto):
    cur= mysql.connection.cursor()
    cur.execute('SELECT * FROM proyectos')
    proyectos= cur.fetchall()
    proyecto = None
    if id_proyecto is not None :
        cur.execute('SELECT * FROM proyectos WHERE id_proyecto = %s', (id_proyecto,))
        proyecto = cur.fetchone()
    cur.close()
    return render_template('index.html', proyectos = proyectos, proyecto = proyecto)

@app.route('/sobreMi')
def sobreMi():
    return render_template('sobreMi.html')

if __name__ == '__main__':
    app.run(debug= True, port= 5000)

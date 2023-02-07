import pyodbc
import sqlite3
from flask import Flask
from flask import render_template
from flask import send_from_directory

app = Flask(__name__)

conexion = pyodbc.connect('Driver={ODBC Driver 17 for SQL server};'  

    'Server=srv-fldb01;' #Servidor donde está la base de datos

    'Database=Infor_parqueaderos;' #Base de datos

    'UID=consultaParqueadero;' #Usuario creado para la consulta

    'PWD=Parqueadero123') #Password del usuario

@app.route('/')
def index():

    return render_template('index.html')

@app.route('/park')
def park():

    return render_template('indexPark.html')

@app.route('/par_parquea/<Zona>')
def par_parquea(Zona):
    
    query = "SELECT * FROM Parqueadero where Zona = " + "'" + Zona +"'"
    Cursor = conexion.cursor()
    Cursor.execute(query)
    parqueaderos = Cursor.fetchall()
    
    conexion.commit()
    return render_template('parqueadero.html', parqueaderos=parqueaderos)

@app.route('/con_control')
def con_control():

    Cursor = conexion.cursor()
    Cursor.execute("SELECT * FROM Controlador")
    controladores = Cursor.fetchall()
    
    conexion.commit()
    return render_template('controladores.html', controladores=controladores)    

if __name__ == '__main__':
    app.run(debug=True)


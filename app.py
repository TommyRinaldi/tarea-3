from flask import *
import os
app= Flask(__name__)
import psycopg2
from psycopg2 import Error

    # Connect to an existing database
slave = psycopg2.connect(user="my_user",
                                  password="password123",
                                  host="127.0.0.1",
                                  port="65432",
                                  database="postgres")

master = psycopg2.connect(user="my_user",
                                  password="password123",
                                  host="127.0.0.1",
                                  port="55432",
                                  database="postgres")

@app.route("/inventario")
def aplicacion():
    
    #r.set('hello','world')
    #value= r.get('hello')
    #print (value)   #imprime en la consola
    #return (value)   #retorna en localhost
    #data = request.form.get('input_name', default_value)
    return render_template('index.html')
    #return ("<form method='GET' action='/search'><input type='text' name='producto'/><input type='submit' value='Submit'/></form>")
@app.route("/agregar",methods=['POST'])
def agregar():
    cursor = master.cursor()
    insert_query = f""" INSERT INTO tabla (numero, string) VALUES ('{request.form['Cantidad']}','{request.form['Nombre cocinero']}')"""
    cursor.execute(insert_query)
    master.commit()
    return render_template('redirect.html')
@app.route("/mostrar")
def mostrar():
    cursor = slave.cursor()
    cursor.execute("SELECT * from tabla")
    return render_template('inventario.html',inventario=cursor.fetchall())
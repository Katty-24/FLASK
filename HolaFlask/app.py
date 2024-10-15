from flask import Flask
from flask_cors import CORS
app=Flask(__name__)
CORS(app)

@app.route("/")
def HolaFlask():
    return "<h1>¡Hola Flask!</h1> <hr>"

##Haga un programa que calcule el promedio de notas sabiendo que 
## tienen un valor de 30%, 30% y 40% respectivamente.
@app.route("/Notas")
@app.route("/Notas/<float:nota1>/<float:nota2>/<float:nota3>")
def Notas(nota1=0,nota2=0,nota3=0):
    resultado=(nota1*30)/100+(nota2*30)/100+(nota3*40)/100
    return f"<h1> El resultado es: {resultado}</h1> <hr>"

## 2.) Un programa que al capturar la edad de una persona diga si es:
## Menor de edad (Menor a 18 años)
## Adulto (Mayor o igual a 18 años y menor a 60 años)
## Adulto mayor (Mayor o igual a 60 años)
@app.route("/edades")
@app.route("/edades/<int:edad>")
def edades(edad:0):
    if edad<18:
        R="Menor de edad"
    elif(edad<60):
        R="Adulto"
    else:
        R="Adulto Mayor"
    return f"<h1>La persona es: {R}</h1> <hr>"

## Realizar un algoritmo con funciones que en la primera opción cargue e imprima 
## vectores, en la segunda opción cargue e imprima matrices
import numpy as np
@app.route("/arreglos")
@app.route("/arreglos/<int:valores>/<int:columnas>")
@app.route("/arreglos/<int:valores>/<int:columnas>/<int:filas>")
def arreglos(valores=0,columnas=0,filas=0):
    if filas==0:
        arreglo=np.random.randint(valores, size=columnas)
    else:
        arreglo=np.random.randint(valores, size=(filas,columnas))
    
    return f"<h1>El arreglo aleatorio es: {arreglo}</h1> <hr>"

if __name__=='__main__':
    app.run(debug=True)
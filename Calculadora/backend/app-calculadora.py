from flask import Flask
from flask_cors import CORS
import math as mt
from flask import jsonify
app=Flask(__name__)
CORS(app)

## suma
@app.route("/")
@app.route("/<float:numero1>/<float:numero2>")
@app.route("/<int:numero1>/<int:numero2>")
@app.route("/<int:numero1>/<float:numero2>")
@app.route("/<float:numero1>/<int:numero2>")
def suma(numero1=0,numero2=0):
    resultado=numero1+numero2
    ##return f"<h1>El resultado es: {resultado}</h1> <hr>"
    data={
        "Resultado":resultado,
        "Operacion":"suma",
     }
    return jsonify(data)

## Resta
@app.route("/resta/<float:numero1>/<float:numero2>")
@app.route("/resta/<int:numero1>/<int:numero2>")
@app.route("/resta/<int:numero1>/<float:numero2>")
@app.route("/resta/<float:numero1>/<int:numero2>")
def resta(numero1=0,numero2=0):
    resultado=numero1-numero2
    ##return f"<h1>El resultado es: {resultado}</h1> <hr>"
    data={
        "Resultado":resultado,
        "Operacion":"resta",
     }
    return jsonify(data)

## multiplicacion
@app.route("/multiplicacion/<float:numero1>/<float:numero2>")
@app.route("/multiplicacion/<int:numero1>/<int:numero2>")
@app.route("/multiplicacion/<int:numero1>/<float:numero2>")
@app.route("/multiplicacion/<float:numero1>/<int:numero2>")
def multiplicacion(numero1=0,numero2=0):
    resultado=numero1*numero2
    ##return f"<h1>El resultado es: {resultado}</h1> <hr>"
    data={
        "Resultado":resultado,
        "Operacion":"multiplicacion",
     }
    return jsonify(data)

## Division 
@app.route("/division/<float:numero1>/<float:numero2>")
@app.route("/division/<int:numero1>/<int:numero2>")
@app.route("/devision/<float:numero1>/<int:numero2>")
@app.route("/division/<int:numero1>/<float:numero2>")
def division(numero1=0,numero2=0):
    resultado=numero1/numero2
    ##return f"<h1>El resultado es: {resultado}</h1> <hr>"
    data={
        "Resultado":resultado,
        "Operacion":"division",
     }
    return jsonify(data)

## potenciacion
@app.route("/potenciacion/<float:numero1>/<float:numero2>")
@app.route("/potenciacion/<int:numero1>/<int:numero2>")
@app.route("/potenciacion/<float:numero1>/<int:numero2>")
@app.route("/potenciacion/<int:numero1>/<float:numero2>")
def potenciacion(numero1=0,numero2=0):
    resultado=numero1**numero2
    ##return f"<h1>El resultado es: {resultado}</h1> <hr>"
    data={
        "Resultado":resultado,
        "Operacion":"potenciacion",
     }
    return jsonify(data)

## Seno
@app.route("/seno/<float:numero1>")
@app.route("/seno/<int:numero1>")
def seno(numero1=0):
    resultado=mt.sin(numero1)
    ##return f"<h1>El resultado es: {resultado}</h1> <hr>"
    data={
        "Resultado":resultado,
        "Operacion":"seno",
     }
    return jsonify(data)
## coseno
@app.route("/coseno/<float:numero1>")
@app.route("/coseno/<int:numero1>")
def coseno(numero1=0):
    resultado=mt.cos(numero1)
    ##return f"<h1>El resultado es: {resultado}</h1> <hr>"
    data={
        "Resultado":resultado,
        "Operacion":"coseno",
     }
    return jsonify(data)

if __name__=='__main__':
    app.run(debug=True)

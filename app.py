from flask import Flask, render_template
from pedido import *

app = Flask(__name__)

"""
    Ruta principal de la aplicación.
    Renderiza el template 'consulta_pedido.html' que muestra un formulario para consultar un pedido.
    """

@app.route('/')
def index():
    return render_template('consulta_pedido.html')

@app.route('/pedido/<codigo_pedido>')

#Ruta para consultar un pedido en especifico
def consultar_pedido(codigo_pedido):
    db = Database("mi_base_de_datos.db")  
    # Realiza la consulta del pedido en base al número de pedido
    pedido = db.consultar_pedido(codigo_pedido)

    if pedido:
        # Si se encuentra el pedido, renderiza el template 'pedido.html' con los datos del pedido
        return render_template('consulta_pedido.html', pedido=pedido, codigo_pedido=codigo_pedido)

    else:
        # Si no se encuentra el pedido, muestra un mensaje de error
        error_message = "No se encontró ningún pedido con el número especificado."
        return render_template('consulta_pedido.html', error_message=error_message)
    

if __name__ == '__main__':
    app.run()


from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    resultado = None
    if request.method == 'POST':
        try:
            numero1 = float(request.form['numero1'])
            numero2 = float(request.form['numero2'])
            operacion = request.form['operacion']

            if operacion == 'suma':
                resultado = numero1 + numero2
            elif operacion == 'resta':
                resultado = numero1 - numero2
            elif operacion == 'multiplicacion':
                resultado = numero1 * numero2
            elif operacion == 'division':
                if numero2 != 0:
                    resultado = numero1 / numero2
                else:
                    resultado = '❌ Error: división entre cero'
        except ValueError:
            resultado = '⚠️ Por favor, ingresa solo números válidos.'

    return render_template('index.html', resultado=resultado)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)

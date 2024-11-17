from flask import Flask, render_template, request

app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html', title="Inicio")


@app.route('/ejercicio1', methods=['GET', 'POST'])
def ejercicio1():
    resultado = None
    if request.method == 'POST':
        # Capturar datos del formulario
        nota1 = int(request.form['nota1'])
        nota2 = int(request.form['nota2'])
        nota3 = int(request.form['nota3'])
        asistencia = int(request.form['asistencia'])

        # Calcular promedio
        promedio = (nota1 + nota2 + nota3) / 3

        # Determinar estado
        if promedio >= 40 and asistencia >= 75:
            estado = "Aprobado"
        else:
            estado = "Reprobado"

        resultado = {
            "promedio": promedio,
            "estado": estado
        }
    return render_template('ejercicio1.html', title="Ejercicio 1", resultado=resultado)


@app.route('/ejercicio2', methods=['GET', 'POST'])
def ejercicio2():
    resultado = None
    if request.method == 'POST':
        # Capturar datos del formulario
        nombres = [
            request.form['nombre1'],
            request.form['nombre2'],
            request.form['nombre3']
        ]

        # Encontrar el nombre más largo
        nombre_mas_largo = max(nombres, key=len)
        longitud = len(nombre_mas_largo)

        resultado = {
            "nombre": nombre_mas_largo,
            "longitud": longitud
        }
    return render_template('ejercicio2.html', title="Ejercicio 2", resultado=resultado)


if __name__ == '__main__':
    app.run(debug=True)

from flask import Flask
from flask import render_template

# templates are html. por defecto, estos html deben estar en la carpeta templates, pero se puede establecer como parametro en Flask

app = Flask(__name__) #instancia
#app = Flask(__name__, template_folder = 'templates') #si queremos especificar la ruta de la carpeta templates

@app.route('/') #wrap (decorator)
def index():
    return render_template('index.html')

@app.route('/user/')
@app.route('/user/<name>') #wrap (decorator)
@app.route('/user/<name>/<int:age>') #wrap (decorator)
def user(name='Vicente', age = 50):
    #age = 20
    my_list = [1,4,5]
    return render_template('variables.html', user_name=name, age = age, list=my_list)

@app.route('/herencia')
@app.route('/herencia/<title>') #wrap (decorator)
def herencia(title='vicente'):
    return render_template('herencia.html', title = title)

if __name__ == '__main__':
    app.run(debug=True, port=8002) #lunch server on port 5000
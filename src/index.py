# llamamos al framework de flask
from flask import Flask, render_template
from configurations import DevelopmentConfig

# Arrancamos la aplicacion 
app = Flask(__name__)
# Activamos la configuraciones de desarrolo
app.config.from_object(DevelopmentConfig)


# RUTAS
@app.route('/')
def home():
            # renderizamos las vistas de html
    return render_template('home.html')

            #nobre de la ruta
@app.route('/about')
def about():
    return render_template('about.html')


# Mantener en escucha la aplicacion
if __name__ == '__main__': 
    # Ejecuta la aplicacion y recarga el navegador
    app.run(debug=True)
            

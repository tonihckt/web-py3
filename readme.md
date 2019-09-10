***** primero antes de crear un entorno virtual
**** -> pip install virtualenv 
**** -> pip install --upgrade virtualenv


crear entorno de trabajo con python3
 -> python3 -m venv venv
 o
 -> python2 -m virtualenv venv

 activar el entorno de trabajo python3
 ->  . venv/bin/activate

 instalar flask
 -> pip install Flask

en el caso que no veas flask en la carpeta lib
***-> pip install --upgrade pip



 ##################
 #####configuraciones
 Para cambiar Flask al entorno de desarrollo y habilitar el modo de depuración, configure FLASK_ENV:
-> export FLASK_ENV=development
-> flask run
 ##################

 *ordenar tabulaciones del codigo 
1. CMD + Shift + P -> Format Document OR
2. Selecciona Prettify
3. CMD + Shift + P -> Format Selection



 ##################
subir a produccion la web o a un servidor
##############
usaremos - registrate ::: https://elements.heroku.com/
instalar heroku cli
-> brew tap heroku/brew && brew install heroku
::: comandos heroku 
-> heroku login
preprar entorno de web para servidor 
1- crear un archivo: requirements.txt ( aqui van las librerias que necesita el proyecto)
2- crear un archivo: runtime.txt (especificamos la version de python)
3- crear un archivo: Procfile  (decide que archivo ejecuta al principio)

instalar gunicorn ( dependecia que require heroku)
-> pip install gunicorn

te lista las libreria que has usado en el proyecto y estas se copian a requirements.txt
-> pip freeze

*** subir proyecto a github
git init
git add .


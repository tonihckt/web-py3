***** primero antes de crear un entorno virtual
**** -> pip install virtualenv 
**** -> pip install --upgrade virtualenv

crear entorno de trabajo con python
 -> python3 -m venv venv
 o
 -> python2 -m virtualenv venv

 activar el entorno de trabajo python
 -> source venv/bin/activate

############## Manejando paquetes con pip
 instalar paquetes
 -> pip install Flask |o| -> pip install Flask requests==1.1.1
 desintalar paquetes
 -> pip uninstall Flask
 actualizar un paquete
 -> pip install --upgrade Flask
 muestra la info del paquetes
 -> pip show Flask
muestra todos los paquetes instalados en el entorno virtual
-> pip list
en el caso que no veas flask en la carpeta lib
***-> pip install --upgrade pip

te crea un archivo con todas las librerias del entorno virtual
-> pip freeze > requirements.txt
*** para instalar las librerias listadas de requirements.txt(opcional)
****-> pip install -r requirements.txt

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
nos conetamos a heroku por consola
-> heroku login



-------------
preprar entorno de web para servidor 
1- crear un archivo: requirements.txt ( aqui van las librerias que necesita el proyecto)
2- crear un archivo: runtime.txt (especificamos la version de python)
3- crear un archivo: Procfile  (decide que archivo ejecuta al principio)
    * ver versiones diponibles(https://devcenter.heroku.com/articles/python-support#specifying-a-python-version)

instalar gunicorn ( dependecia que require heroku)
-> pip install gunicorn

te lista las libreria que has usado en el proyecto y estas se copian a requirements.txt
-> pip freeze
---------------

-------------------------------------------------
*** subir proyecto a github
git init
git add .
git commit -m "web-py3"
git remote add origin git@github.com:aquiVaLaRutaQueTengas.git
git push -u origin master
---------------

seguimos con heroku
creamos proyec en heroku
-> heroku create nombreProyecto
sincromizamos heroku con repositorio de github
-> heroku git:remote nombreProyecto
subir proyecto a heroku
-> git push heroku master
abrir proyecto
-> heroku open


# Diferencias entre estas extensiones y cómo se generan a partir de un archivo * .py
> .py: este es normalmente el código fuente de entrada que has escrito.
> .pyc: Este es el bytecode compilado. Si importa un módulo, Python creará un archivo * .pyc que contiene el código de bytes para que la importación sea más fácil (y rápida).
> .pyo: este es un archivo * .pyc que se creó mientras las optimizaciones (-O) estaban activadas.
> .pyd: Esto es básicamente un archivo dll de Windows. http://docs.python.org/faq/windows.html#is-a-pyd-file-the-same-as-a-dll
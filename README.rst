=======
PyBright
=======

Es un proyecto escrito en Python,  sirve como  Wrapper al API de : `Brightcove <http://www.brigtcove.com>`_. A fin de facilitar el acceso a la data de videos y playlists que algunas empresas suelen almacenar y servir desde alli.

PyBright puede ejecutarse desde la linea de comandos, o puede tambien usarse como libreria en nuestros scripts python.


Instalacion:
------------

- Clonar el proyecto:

::
 
 git clone https://github.com/wasuaje/pyBright.git .


Requerimientos:
---------------

- Preferiblemente utilice dentro de un virtualenv: 


::

 sudo apt-get install python-setuptools o sudo yum install python-setuptools
 sudo easy-install pip
 pip install virtualenv

- SimpleJson 

::
 
 pip install simplejson


- Archivo de configuracion con los valores wtoken y rtoken llamado defaults.cfg como el siguiente
 

::

 [Config]
 rtoken=insert read token here
 wtoken=insert write token here

- La data de prueba en tu ubicacion actual:

::

 cp pybright/video_data.dat .



Utilizacion:
------------

- Opciones desde la linea de comandos:

::

 usage: bcove.py [-h] [-v] [-p] [-l] [-x] [-f FIND] [-g GETS] [-t TAGS]
                [-u UPDATE] [-c CREAT] [-d DOWNLOAD] [-r REMOVE] [-b BESTR]

 Wrapper around Brightcove API

 optional arguments:
  -h, --help            show this help message and exit
  -v, --video           Selecciona trabajar con Videos:
  -p, --playlist        Selecciona para trabajar con Playlists:
  -l, --load            Descarga la data de Brightcove a este equipo, luego
                        puede usar exportarla a csv
  -x, --export          Exporta la data a un fichero .csv
  -f FIND, --find FIND  Busca un item por id en la data local
  -g GETS, --gets GETS  Get Item por id en la data remota rbightcove
  -t TAGS, --tags TAGS  Busca un item por tags
  -u UPDATE, --update UPDATE
                        Actualiza a alwaysAvailable un id
  -c CREAT, --cfind CREAT
                        Busca un item por creation date
  -d DOWNLOAD, --download DOWNLOAD
                        Descarga un video desde Brightcove dado un ID
  -r REMOVE, --remove REMOVE
                        Elimina video de Brightcove dado un ID
  -b BESTR, --bestr BESTR
                        Descarga el mejor rendition del video dado un ID


- Ejemplo desde la linea de comandos (Crea un CSV de la data existente):

::
 
 python bcove.py -vx 
 
 $ ls
 LICENSE		README.rst	defaults.cfg	myprogram.py	pyBright	video_data.dat	videos.csv

Ayuda:
-----------------

::

 Comunicate conmigo a wasuaje@hotmail.com si tienes duda o encuentras problemas para implementarlo.

=======
PyBright
=======

Es un proyecto escrito en Python,  sirve como  Wrapper al API de : `Brightcove <http://www.brigtcove.com>`_. A fin de facilitar el acceso a la data de videos y playlists que algunas empresas suelen almacenar y servir desde alli.

PyBright puede ejecutarse desde la linea de comandos, o puede tambien usarse como libreria en nuestros scripts python.




Requiere:
---------

- Requiere SimpleJson 

::
 
 pip install simplejson


- Crea un archivo de configuracion con los valores wtoken y rtoken llamado defaults.cfg
 

::

 [Config]
 rtoken=insert read token here
 wtoken=insert write token here

- Copia la data de prueba a tu ubicacion actual:

::

 cp pybright/video_data.dat .

Instalacion:
------------

- Luego de clonar el proyecto en un directorio vacìo, coloque su read token y su write token dentro de un archivo llamado defaults.cfg en la raiz de su proyecto

::
 
 git clone https://github.com/wasuaje/pyBright.git .

Utilizacion:
------------

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
                        Actualiza a alwaysVallable un id
  -c CREAT, --cfind CREAT
                        Busca un item por creation date
  -d DOWNLOAD, --download DOWNLOAD
                        Descarga un video desde Brightcove dado un ID
  -r REMOVE, --remove REMOVE
                        Elimina video de Brightcove dado un ID
  -b BESTR, --bestr BESTR
                        Descarga el mejor rendition del video dado un ID


Ayuda:
-----------------

::

 Comunicate conmigo a wasuaje@hotmail.com si tienes duda o encuentras problemas para implementarlo.

=======
PyBright
=======

Es un proyecto escrito en Python,  sirve como  Wrapper al API de : `Brightcove <http://www.brigtcove.com>`_. A fin de facilitar el acceso a la data de videos y playlists que algunas empresas suelen almacenar y servir desde alli.

PyBright puede ejecutarse desde la linea de comandos, o puede tambien usarse como libreria en nuestros scripts python.




Requerimientos:
---------------

- Python 2.7
- SimpleJson
- Prereiblemente virtualenv 


::

 # Install Setuptools in Debian / Ubuntu
 sudo apt-get install python-setuptools 
 
 # Centos / Fedora
 yum install python-setuptools

::

 #Install pip in Debian / Ubuntu
 sudo aptitude install python-pip
 
 #Centos / Fedora
 yum install python-pip


::

 #Virtualenv
 pip install virtualenv

::
 
 #Activar virtualenv
 virtualenv myvenv

 cd myvenv

 source/bin activate

::

 #Instalar simplejson dentro de nuestro ambiente virtual
 pip install simplejson

- Crear archivo de configuracion con los valores wtoken y rtoken llamado defaults.cfg como el siguiente
 

::

 [Config]
 rtoken=insert read token here
 wtoken=insert write token here

- Copiar la data de prueba en tu ubicacion actual:

::

 cp pybright/video_data.dat .


- Clonar el proyecto:

::
 
 git clone https://github.com/wasuaje/pyBright.git .


Utilizacion:
------------

- Opciones desde la linea de comandos:

::

 $ python pyBright/bcove.py

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
  -g GETS, --gets GETS  Get Item por id en la data remota brightcove
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

Ejemplos de uso:
----------------

- Ejemplo 1  Crea un CSV de la data existente desde la linea de comandos:

::
 
 python pyBright/bcove.py -vx 
 
 $ ls
 LICENSE  README.rst	defaults.cfg	myprogram.py pyBright video_data.dat	videos.csv


- Ejemplo 2  Descargar un video conocido su ID desde la linea de comandos:

::

 $ python pyBright/bcove.py -vd 2555607253001

  find_item_by_id 2555607253001
  Archivo: 986049905001_2555625549001_Agust-n-blanco-Mu-oz---Historiador-20130719-161102-446.mp4, tamaño: 99.313859 MB
  Desde URL:  http://brightcove.vo.llnwd.net/e1/uds/pd/986049905001/986049905001_2555625549001_Agust-n-blanco-Mu-oz---Historiador-20130719-161102-446.mp4
  Descarga finalizada


- Ejemplo 3  Buscar un video conocido su ID desde la linea de comandos:

::

 $ python pyBright/bcove.py -vf 2555607253001

 {  
   'videoFullLength':{  
      'referenceId':None,
      'displayName':u'Agust\xedn blanco Mu\xf1oz - Historiador-20130719-161102_446.mp4',
      'url':'http://brightcove.vo.llnwd.net/e1/uds/pd/986049905001/986049905001_2555625549001_Agust-n-blanco-Mu-oz---Historiador-20130719-161102-446.mp4',
      'encodingRate':404571,
      'frameWidth':480,
      'audioOnly':False,
      'controllerType':'DEFAULT',
      'videoDuration':1916808,
      'videoCodec':'H264',
      'videoContainer':'MP4',
      'frameHeight':320,
      'remoteStreamName':None,
      'remoteUrl':None,
      'uploadTimestampMillis':1374269857212      L,
      'id':2555625549001      L,
      'size':99313859
   },
   'creationDate':'1374269050639',
   'playsTotal':2433,
   'economics':'AD_SUPPORTED',
   'name':u'Agust\xedn Blanco Mu\xf1oz - Historiador',
   'publishedDate':'1374269050639',
   'renditions':[  
      {  
         'referenceId':None,
         'displayName':u'Agust\xedn blanco Mu\xf1oz - Historiador-20130719-161102_446.mp4',
         'url':'http://brightcove.vo.llnwd.net/e1/uds/pd/986049905001/986049905001_2555617492001_Agust-n-blanco-Mu-oz---Historiador-20130719-161102-446.mp4',
         'encodingRate':145480,
         'frameWidth':400,
         'audioOnly':False,
         'controllerType':'DEFAULT',
         'videoDuration':1916808,
         'videoCodec':'H264',
         'videoContainer':'MP4',
         'frameHeight':264,
         'remoteStreamName':None,
         'remoteUrl':None,
         'uploadTimestampMillis':1374269338745         L,
         'id':2555617492001         L,
         'size':35623461
      },
   ],
   'tags':[  
      u'Profesor Agust\xedn Blanco Mu\xf1oz',
      'golpe de estado',
      'Henrique Capriles Radonski',
      'venezuela',
      'democracia',
      'ucv',
      'HISTORIADOR',
      'poderes militares',
      'ascensos militares'
   ],
   'longDescription':None,
   'videoStillURL':'http://brightcove.vo.llnwd.net/e1/pd/986049905001/986049905001_2555626968001_video-still-for-video-2555607253001.jpg?pubId=986049905001',
   'length':1916808,
   'referenceId':None,
   'playsTrailingWeek':0,
   'linkText':None,
   'lastModifiedDate':'1374272846421',
   'thumbnailURL':'http://brightcove.vo.llnwd.net/e1/pd/986049905001/986049905001_2555626967001_thumbnail-for-video-2555607253001.jpg?pubId=986049905001',
   'linkURL':None,
   'id':2555607253001   L,
   'shortDescription':u'Agust\xedn Blanco Mu\xf1oz - Historiador'
 }


- Ejemplo 4 buscar la data de un video desde un programa / script:

::

 Python 2.7.11 (default, Dec 26 2015, 17:47:53)
 [GCC 4.2.1 Compatible Apple LLVM 7.0.2 (clang-700.1.81)] on darwin
 Type "help", "copyright", "credits" or "license" for more information.
 >>> from pyBright import *
 >>> id_to_seach = 2555607253001
 >>> bc=bcove('vid')
 >>> data = bc.find_local_item_by_id(id_to_seach)
 find_local_item_by_id 2555607253001
 >>> print data

 {'videoFullLength': {'referenceId': None, 'displayName': u'Agust\xedn blanco Mu\xf1oz - Historiador-20130719-161102_446.mp4', 'url': 'http://brightcove.vo.llnwd.net/e1/uds/pd/986049905001/986049905001_2555625549001_Agust-n-blanco-Mu-oz---Historiador-20130719-161102-446.mp4', 'encodingRate': 404571, 'frameWidth': 480, 'audioOnly': False, 'controllerType': 'DEFAULT', 'videoDuration': 1916808, 'videoCodec': 'H264', 'videoContainer': 'MP4', 'frameHeight': 320, 'remoteStreamName': None, 'remoteUrl': None, 'uploadTimestampMillis': 1374269857212L, 'id': 2555625549001L, 'size': 99313859}, 'creationDate': '1374269050639', 'playsTotal': 2433, 'economics': 'AD_SUPPORTED', 'name': u'Agust\xedn Blanco Mu\xf1oz - Historiador', 'publishedDate': '1374269050639', 'renditions': [{'referenceId': None, 'displayName': u'Agust\xedn blanco Mu\xf1oz - Historiador-20130719-161102_446.mp4', 'url': 'http://brightcove.vo.llnwd.net/e1/uds/pd/986049905001/986049905001_2555617492001_Agust-n-blanco-Mu-oz---Historiador-20130719-161102-446.mp4', 'encodingRate': 145480, 'frameWidth': 400, 'audioOnly': False, 'controllerType': 'DEFAULT', 'videoDuration': 1916808, 'videoCodec': 'H264', 'videoContainer': 'MP4', 'frameHeight': 264, 'remoteStreamName': None, 'remoteUrl': None, 'uploadTimestampMillis': 1374269338745L, 'id': 2555617492001L, 'size': 35623461}, {'referenceId': None, 'displayName': u'Agust\xedn blanco Mu\xf1oz - Historiador-20130719-161102_446.mp4', 'url': 'http://brightcove.vo.llnwd.net/e1/uds/pd/986049905001/986049905001_2555625549001_Agust-n-blanco-Mu-oz---Historiador-20130719-161102-446.mp4', 'encodingRate': 404571, 'frameWidth': 480, 'audioOnly': False, 'controllerType': 'DEFAULT', 'videoDuration': 1916808, 'videoCodec': 'H264', 'videoContainer': 'MP4', 'frameHeight': 320, 'remoteStreamName': None, 'remoteUrl': None, 'uploadTimestampMillis': 1374269857212L, 'id': 2555625549001L, 'size': 99313859}, {'referenceId': None, 'displayName': u'Agust\xedn blanco Mu\xf1oz - Historiador-20130719-161102_446.mp4', 'url': 'http://brightcove.vo.llnwd.net/e1/uds/pd/986049905001/986049905001_2555617518001_Agust-n-blanco-Mu-oz---Historiador-20130719-161102-446.mp4', 'encodingRate': 313073, 'frameWidth': 400, 'audioOnly': False, 'controllerType': 'DEFAULT', 'videoDuration': 1916808, 'videoCodec': 'H264', 'videoContainer': 'MP4', 'frameHeight': 264, 'remoteStreamName': None, 'remoteUrl': None, 'uploadTimestampMillis': 1374269374883L, 'id': 2555617518001L, 'size': 77272796}], 'tags': [u'Profesor Agust\xedn Blanco Mu\xf1oz', 'golpe de estado', 'Henrique Capriles Radonski', 'venezuela', 'democracia', 'ucv', 'HISTORIADOR', 'poderes militares', 'ascensos militares'], 'longDescription': None, 'videoStillURL': 'http://brightcove.vo.llnwd.net/e1/pd/986049905001/986049905001_2555626968001_video-still-for-video-2555607253001.jpg?pubId=986049905001', 'length': 1916808, 'referenceId': None, 'playsTrailingWeek': 0, 'linkText': None, 'lastModifiedDate': '1374272846421', 'thumbnailURL': 'http://brightcove.vo.llnwd.net/e1/pd/986049905001/986049905001_2555626967001_thumbnail-for-video-2555607253001.jpg?pubId=986049905001', 'linkURL': None, 'id': 2555607253001L, 'shortDescription': u'Agust\xedn Blanco Mu\xf1oz - Historiador'}

 >>> type(data)
 <type 'dict'>

 >>> print data['videoFullLength']['videoCodec']
 H264
 
 >>> print data['videoFullLength']['videoContainer']
 MP4

- Ejemplo 5 Descargar un video desde un programa / script

::
 
 Python 2.7.11 (default, Dec 26 2015, 17:47:53)
 [GCC 4.2.1 Compatible Apple LLVM 7.0.2 (clang-700.1.81)] on darwin
 Type "help", "copyright", "credits" or "license" for more information.
 >>> from pyBright import *
 >>> id_to_seach = 2555607253001
 >>> bc=bcove('vid')
 data = bc.download_video(id_to_seach)
 find_item_by_id 2555607253001
 Archivo: 986049905001_2555625549001_Agust-n-blanco-Mu-oz---Historiador-20130719-161102-446.mp4, tamaño: 99.313859 MB
 Desde URL:  http://brightcove.vo.llnwd.net/e1/uds/pd/986049905001/986049905001_2555625549001_Agust-n-blanco-Mu-oz---Historiador-20130719-161102-446.mp4
 Descarga finalizada


Ayuda:
-----------------

::

 Si tienes problema instalando o haciendo funcionar el codigo no dudes en comunicarte conmigo a wasuaje@gmail.com.

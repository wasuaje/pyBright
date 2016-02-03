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

 sudo apt-get install python-setuptools # sudo yum install python-setuptools
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


- Ejemplo1  desde la linea de comandos (Crea un CSV de la data existente):

::
 
 python pyBright/bcove.py -vx 
 
 $ ls
 LICENSE		README.rst	defaults.cfg	myprogram.py	pyBright	video_data.dat	videos.csv


- Ejemplo 2  Descargar un video conocido su ID desde la l inea de comandos:

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



Ayuda:
-----------------

::

 Comunicate conmigo a wasuaje@hotmail.com si tienes duda o encuentras problemas para implementarlo.

#!/usr/bin/python
# -*- coding: utf-8 -*-

from optparse import OptionParser
import urllib,httplib
import urllib2
import simplejson as json
import math
import os
import datetime
import sys
import time
#modulo para serializar el diccionario con la data
try:
    import cPickle as pickle
except ImportError:
    import pickle


class bcove:

	url="http://api.brightcove.com/services/library"
	     
	campos={
			'video_fields':'id,name,shortDescription,longDescription,creationDate,publishedDate,lastModifiedDate,linkURL,linkText,tags,videoStillURL,thumbnailURL,referenceId,length,economics,playsTotal,playsTrailingWeek,videoFullLength,renditions',
			'playlist_fields':'id,name,shortDescription,playlistType,videoIds,accountId,referenceId,filterTags,thumbnailURL'	
			}
		
	def __init__(self, rtoken,tipo,wtoken=''):
		self.rtoken = rtoken
		self.wtoken = wtoken
		self.tipo   = tipo
		self.parametros={}
		self.parametros['token']=self.rtoken	
		self.parametros['get_item_count']='true'
		self.parametros['page_size']=100
		self.parametros['media_delivery']='http'

		if tipo=='vid':
			self.parametros['command']='search_videos_unfiltered'						
			self.tip='video'
			self.titulos=bcove.campos[self.tip+"_fields"]
			self.exportfile='videos.csv'
		elif tipo=='play':
			self.parametros['command']='find_all_playlists'
			self.tip='playlist'
			self.titulos=bcove.campos[self.tip+"_fields"]
			self.exportfile='playlists.csv'  

		self.parametros[self.tip+'_fields']='id'
		self.dataf=self.tip+"_data.dat" 
		

	def import_data(self):		
		video_data={}
		submitVarsUrlencoded = urllib.urlencode(self.parametros)	
		req = urllib2.Request(bcove.url,submitVarsUrlencoded)
		response = urllib2.urlopen(req)
		thePage = response.read()
		f=json.loads(thePage)	
		
		#obtengo por primera vez el conteo total de videos
		total_videos = f['total_count']
		#como puedo obtener 100 resultados obtengo el total de paginas
		pg_size=20
		paginas=math.ceil(total_videos/pg_size)	
		paginas=int(paginas)
		
		#itero por cada pagina obtenido en el paso anterior
		for pg in range(0,paginas+1):
			self.parametros['page_number']=pg
			self.parametros['page_size']=pg_size
			#parametros.pop('video_fields')
			self.parametros[self.tip+'_fields']=self.titulos
			submitVarsUrlencoded = urllib.urlencode(self.parametros)	
			req = urllib2.Request(bcove.url,submitVarsUrlencoded)
			response = urllib2.urlopen(req)
			thePage = response.read()
			try:
				f=json.loads(thePage)	
			except:
				print "Error:", thePage
			#print f		
			print "pagina: %s" % pg		
			try:
				#itero por el contenido de cada pagina y lo salvo en un dict local
				for i in f['items']:
					#video_data[i['id']]={'nombre':i['name'],'url':i['FLVURL'],'descargado':0}
					video_data[i['id']]=i									
			except KeyError:
				print f['error']
				#print "Error obteniendo la informacion, tal vez deba ejecutar el script de nuevo",sys.exc_info()[0],sys.exc_info()[1]        
			#time.sleep(60)

		#serializo el contenido del dict local
		if os.path.exists(self.dataf):
			os.remove(self.dataf)
		fichero = file(self.dataf, "w")
		pickle.dump(video_data, fichero, 2)
		fichero.close()

	def read_data(self):
		fichero = file(self.dataf)
		data = pickle.load(fichero)
		fichero.close()
		return data

	def export_data(self):
		a=self.read_data()	
		#segun el tipo de datos
		titulos=self.titulos		
		z=titulos+'\n'
		self.write_file(self.exportfile,z)
		#lista con los titulos
		tit=titulos.split(',')
		#print tit
		for i in a.keys():		
			x=''
			for t in tit:
				try:			
					fld=a[i][t]			
					if isinstance(fld, long):		
						fld=str(fld)
					if fld == None:				
						fld=''
					if isinstance(fld, list):						
						fld="'"+str(fld).strip('[]')+"'"
						fld = fld.replace('"',"")
						fld = fld.replace("'","")	
					if isinstance(fld, int):						
						fld=str(fld)
					if isinstance(fld, dict):						
						fld=''
					if 'Date' in t:						
						#fld=datetime.datetime.fromtimestamp(int(fld)).strftime('%Y-%m-%d %H:%M:%S')
						fld = datetime.datetime.fromtimestamp(float(fld)/1000).strftime('%d-%m-%Y %H:%M:%S')
					fld = fld.replace('"',"'")
					fld = fld.encode('utf-8')			
					x+= '"'+fld+'",'
				except KeyError:
					pass
			#le agrego ultima comilla y el retorno de carro a efectos de mejor visibilidad
			x+='\n'
			self.write_file(self.exportfile,x)	
	
	def find_local_item_by_id(self,id):
		print "find_local_item_by_id",id
		a=self.read_data()			
		if id in a.keys():
			print a[id]
			return a[id]							
		else:
			print "No se encontro item con id",id

	def find_item_by_id(self,id):
		print "find_item_by_id",id
		parametros={}
		#parametros[self.tip+'_fields']="id,videoFullLength,shortDescription,renditions"
		parametros[self.tip+'_fields']=self.titulos
		parametros['media_delivery']='http'
		parametros['command']="find_video_by_id"
		parametros['video_id']=id
		parametros["token"]=self.rtoken
		submitVarsUrlencoded = urllib.urlencode(parametros)	
		req = urllib2.Request(bcove.url,submitVarsUrlencoded)
		response = urllib2.urlopen(req)
		thePage = response.read()
		try:
			f=json.loads(thePage)	
			return f
		except:
			pass
		return f	


	def find_item_by_creation_date(self,date):
		print "Buscando"
		retorno=[]
		a=self.read_data()	
		for i in a.keys():
			fld = datetime.datetime.fromtimestamp(float(a[i]['creationDate'])/1000).strftime('%d-%m-%Y')
			#print fld,date
			if date == fld:				
				#print a[i]['id']			
				retorno.append(a[i]['id'])
		#print retorno
		return retorno

	def find_item_by_tags(self,tgs):
		print "Buscando"
		retorno=[]		
		tgs=tgs.split(",")
		a=self.read_data()
		for i in a.keys():						
			fld=a[i]['tags']			
			if len(set(tgs).intersection(fld))==len(tgs):			
				retorno.append(a[i]['id'])
		#print retorno,len(retorno)
		return retorno,len(retorno)

	def get_renditions(self,id):
		#self.parametros['page_number']=pg			
		#parametros.pop('video_fields')
		self.parametros[self.tip+'_fields']="renditions"
		submitVarsUrlencoded = urllib.urlencode(self.parametros)	
		req = urllib2.Request(bcove.url,submitVarsUrlencoded)
		response = urllib2.urlopen(req)
		thePage = response.read()
		try:
			f=json.loads(thePage)	
		except:
			pass
		return f				
		

	def update_video(self,ids):
		"""
		{"params": {"token":"9fFiMGiBB0usSRe36g3vYwayybMA.",
 			"video": {"name":"MyVideo","id":"24687531",
           "startDate":null,"endDate":"1289520000000",
           "shortDescription":"Video not available after 2010.11.12"}
           },
			"method": "update_video"} 
		"""		
		video_data={}
		url="http://api.brightcove.com/services/post"
		params={}	
		params={"params":{"token":self.wtoken,"video":{"id":"%s"%ids,"tags":["segunda"]}}}
		params['method']='update_video'	
		header = {"Content-Type":"application/x-www-form-urlencoded"}
		#submitVarsUrlencoded = urllib.urlencode(params)
		submitVarsUrlencoded = urllib.urlencode({'json': json.dumps(params)})
		req = urllib2.Request(url,submitVarsUrlencoded,header)	
		response = urllib2.urlopen(req) 	
		thePage = response.read()
		f=json.loads(thePage)	
		#resutlado esperado en json 	{"result": {}, "error": null, "id": null}
		if f["error"] == None:
			#print f
			print "Video Actualizado"
		else:
			print "Error",f["error"]
		
		#obtengo por primera vez el conteo total de videos		


	def delete_video(self,vidid):
		#en este caso el url es distinto		
		url="http://api.brightcove.com/services/post"
		parametros={}
		parametros['params']={'token':self.wtoken,'video_id':vidid,'cascade':'true'}
		parametros['method']='delete_video'	
		header = {"Content-Type":"application/x-www-form-urlencoded"}			
		submitVarsUrlencoded = urllib.urlencode({'json': json.dumps(parametros)})
		req = urllib2.Request(url,submitVarsUrlencoded,header)	
		response = urllib2.urlopen(req) 	
		thePage = response.read()
		f=json.loads(thePage)	
		#resutlado esperado en json 	{"result": {}, "error": null, "id": null}
		if f["error"] == None:
			#print f
			print "Video eliminado"
		else:
			print "Error eliminado id: %s" % vidid, f["error"]


	def download_video(self,vidid):		
		#data=self.read_data()	#local data 
		#if vidid in data.keys():

		f=self.find_item_by_id(vidid)
		#print f
		url=f['videoFullLength']['url']		
		desc=f['shortDescription']
		file_name = url.split('/')[-1]
		if not os.path.exists(file_name):
			tamano=f['videoFullLength']['size']/1000.00/1000.00
			print u"Archivo: %s, tamaño: %s MB" % (file_name, tamano)
			print u"Desde URL: ",url
			urllib.urlretrieve (url, file_name)
			print "Descarga finalizada"
			return file_name,desc
		else:
			raise Exception("Archivo ya descargado !")

	def download_br_video(self,vidid):		
		#data=self.read_data()	#local data 
		#if vidid in data.keys():
		#video con todos sus renditions
		dat={}
		f=self.find_item_by_id(vidid)		
		if f==None:
			raise ValueError, 'Archivo eliminado o no disponible en Brightcove'
			return None
		for rn in f["renditions"]:
			dat[rn["size"]]=rn["url"]		
		ord=sorted(dat,reverse = True)
		#print dat[ord[0]]
		#sys.exit(1)
		#print f
		#cuando ya ordene los renditios
		#url=f['videoFullLength']['url']		
		url=dat[ord[0]]
		desc=f['shortDescription']
		file_name = url.split('/')[-1]
		if not os.path.exists(file_name):
			tamano=ord[0]/1000.00/1000.00
			print u"Archivo: %s, tamaño: %s MB" % (file_name, tamano)
			print u"Desde URL: ",url
			urllib.urlretrieve (url, file_name)
			print "Descarga finalizada"
			#return file_name,desc
			#mejor retorno el objeto completo con toda la data del video en proceso se extrae lo que se necesite
			return f,file_name
		else:
			raise Exception("Archivo ya descargado en disco !")
			#else:
			#	raise Exception("Archivo eliminado o no disponible en Brightcove")
			


	def write_file(self,file,newLine):	
		file = open(file, "a")
		file.write(newLine)
		file.close()

#Variables necesarias solo para pruebas la version definitiva no debe tener etos token debe proporcionarlo el usuario
rtoken='add your read brightcove token'
wtoken='add your read brightcove token'
         
medulatoken=""

if __name__ == "__main__":
	usage = "utilizacion: %prog [options] "
	parser = OptionParser(usage)
	#parser.add_option("-h", "--help", action="help")
		
	parser.add_option("-v", "--video",  action="store_true", dest="video", help='Selecciona trabajar con Videos: ')
	parser.add_option("-p", "--playlist",  action="store_true", dest="playlist", help='Selecciona para trabajar con Playlists: ')	
	parser.add_option("-l", "--load",  action="store_true", dest="load", help='Descarga la data de Brightcove a este equipo, luego puede usar -l para listarla mas rapidamente' )    	
	parser.add_option("-x", "--export", action="store_true", dest="export", help='Exporta la data a un fichero .csv')	
	parser.add_option("-f", "--find",  action="store", dest="find", type="int", help='Busca un item por id en la data local' )    	
	parser.add_option("-g", "--gets",  action="store", dest="gets", type="int", help='Get Item por id en la data remota rbightcove' )    	
	parser.add_option("-t", "--tags",  action="store", dest="tags", type="str", help='Busca un item por tags' )    	
	parser.add_option("-u", "--update",  action="store", dest="update", type="int", help='Actualiza a alwaysVallable un id' )    	
	parser.add_option("-c", "--cfind",  action="store", dest="creat", type="str", help='Busca un item por creation date' )    	
	parser.add_option("-d", "--download",  action="store", dest="download", type="int", help='Descarga un video desde Brightcove dado un ID ') 
	parser.add_option("-r", "--remove",  action="store", dest="remove", type="int", help='Elimina video de Brightcove dado un ID ') 
	parser.add_option("-b", "--bestr",  action="store", dest="bestr", type="int", help='Descarga el mejor rendition del video dado un ID ') 


	#parser.add_option("-r", "--remove",  action="store", dest="id", type="int", help='Elimina un video en Brightcove un id')    	
	#parser.add_option("-s", "--show",  action="store", dest="id2", type="int", help='Muestra la data para un video que esta en Brightcove')    	
	

	
	(options, args) = parser.parse_args()
	#print len(args)
	#if len(args) < 3:
	#	parser.error("numero incorrecto de argumentos")	
	
	if options.video:
		tipo='vid'
	elif options.playlist:
		tipo='play'

	#Acciones sgun cada opcion elegida
	#Actualiza data desde brightcove
	if options.load:
		#Inicializo la instancia de bcove
		bc=bcove(rtoken,tipo)	
		bc.import_data()

	if options.export:		
		bc=bcove(rtoken,tipo)	
		bc.export_data()

	if options.find:		
		bc=bcove(rtoken,tipo)	
		bc.find_local_item_by_id(options.find)

	if options.gets:		
		bc=bcove(rtoken,tipo)	
		bc.find_item_by_id(options.gets)

	if options.download:
		bc=bcove(rtoken,tipo)	
		bc.download_video(options.download)

	if options.bestr:
		bc=bcove(rtoken,tipo)	
		bc.download_br_video(options.bestr)

	if options.creat:
		bc=bcove(rtoken,tipo)	
		bc.find_item_by_creation_date(options.creat)

	if options.tags:
		bc=bcove(rtoken,tipo)	
		lst=bc.find_item_by_tags(options.tags)
		if  lst:
			print lst
		else:
			print "No se encontro"
	
	if options.update:
		#Inicializo la instancia de bcove
		#Necesita el read token y el write token
		bc=bcove(rtoken,tipo,wtoken)	
		bc.update_video(options.update)

	if options.remove:
		#Inicializo la instancia de bcove
		#Necesita el read token y el write token
		bc=bcove(rtoken,tipo,wtoken)	
		bc.delete_video(options.remove)


	# if options.datalocal:
	# 	a=read_data()
	# 	print "Numero de Registros locales:",len(a.keys())		
	
	# if options.dataremote:
	# 	a=get_remote_recs()
	# 	print "Numero de Registros remotos:",a
	
	
	# if options.init:
	# 	get_data(True)
	
	# if options.list:
	# 	if os.path.exists(exportfilename):
	# 		os.remove(exportfilename)
	# 	list_data_local()
	
	# if options.id > 0:
	# 	delete_video(options.id)
	
	# if options.id2 > 0:
	# 	get_video_by_id(options.id2)

	# if options.id3 > 0:
	# 	download_video(options.id3)

	# if options.playlist:
	# 	if os.path.exists(exportplay):
	# 		os.remove(exportplay)
	# 	#get_play_lists()
	# 	export_playlist()

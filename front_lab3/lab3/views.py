from django.shortcuts import render
import urllib.request
import json
import time





# Create your views here.
def home(request):
	return render(request,"home.html")


def search(request):
	#dato que se puso en el buscador
	query = request.GET.get('q')
	#se hace una copia de lo buscado
	nombre = query
	
	
	#obtener json desde API
	query = query.replace(' ',"%20")
	url = 'http://192.168.1.155/'+query
	
	
	#tiempo inicio
	start = time.time()
	req = urllib.request.Request(url)
	r = urllib.request.urlopen(req).read()
	cont = json.loads(r.decode('utf-8'))
	#tiempo fin 
	end = time.time()

	#transformando json a una lista
	data = []
	#atributos que se extraen desde el json
	atr1 = 'ceremony'
	atr2 = 'year'
	atr3 = 'category'
	atr4 = 'outcome'
	atr5 = 'original_languaje'
	for elem in cont:
		data.append([elem[atr1], elem[atr2], elem[atr3], elem[atr4], elem[atr5]])

	#tiempo respuesta de consulta	
	t_resp = end - start

	#datos que se envían al html
	context = {'data': data,'query':query, 't_resp':t_resp, 'test':cont,'name':nombre}
	return render(request,"search.html",context)

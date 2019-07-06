from django.shortcuts import render
import urllib.request
import json





# Create your views here.
def home(request):
	return render(request,"home.html")


def search(request):
	#dato que se puso en el buscador
	query = request.GET.get('q')

	#obtener json desde API
	url = 'http://192.168.1.155/'+query
	
	req = urllib.request.Request(url)
	r = urllib.request.urlopen(req).read()
	cont = json.loads(r.decode('utf-8'))

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
	t_resp = -1000

	#datos que se envían al html
	context = {'data': data,'query':query, 't_resp':t_resp, 'test':cont}
	return render(request,"search.html",context)
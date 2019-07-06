from django.shortcuts import render

# Create your views here.
def home(request):
	return render(request,"home.html")


def search(request):
	query = request.GET.get('q')
	data = [["ceremony1","2000","category1","outcome1","lang1"],["ceremony2","2000","category2","outcome2","lang2"]]
	t_resp = -1000
	context = {'data': data,'query':query, 't_resp':t_resp}
	return render(request,"search.html",context)
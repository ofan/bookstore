from django.http import HttpResponse
from django.template import Context, loader
from django.core import serializers
from member.models import Member

def home(request):
    t = loader.get_template('index.html')
    c = Context({})
    return HttpResponse(t.render(c))

def mainpage(request):
	t = loader.get_template('just_loged_in.html')
	c = Context({})
	return HttpResponse(t.render(c))

def login(request):
	t = loader.get_template('login.html')
	c = Context({})
	return HttpResponse(t.render(c))

def signup(request):
	t = loader.get_template('signup.html')
	c = Context({})
	return HttpResponse(t.render(c))

def processLogin(request):
	return HttpResponse('Hello')

def credentials(request):
	username = request.GET["username"];
	m = Member.objects.get(email=username);	
	data = serializers.serialize("json", [m,])
	
	return HttpResponse(data)
	
	

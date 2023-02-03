from django.shortcuts import render
from .models import Client

# Create your views here.
def register(request):
	if(request.method == "POST"):
    
		nom = request.POST["nom"]
		prenom = request.POST["prenom"]
		mail = request.POST["email"]
		password = request.POST["password"]
		telephone=request.POST["telephone"]
		adresse= request.POST["adresse"]
		c = Client(nom_cl=nom, prenom_cl=prenom, mail= mail, password=password, telephone= telephone, adresse=adresse)
		existing_client=None
		try:
			existing_client = Client.objects.get(mail=mail)
		except:
			print("client not found")
		if(existing_client):
			print(existing_client.mail, "@ already taken")
			error={}
			error["msg"]="Mail aleady taken"
			if error:
				print(error["msg"])
			return render(request, 'register.html', error)
		else:
			c.save()
	return render(request, 'register.html')
    
def home(request):
    return render(request,'home.html')

def login(request):
  return render (request,'login.html')

def kinesin(request):
  return render (request,'kinesin.html')

def kinesit(request):
  return render (request,'kinesit.html')

def kinesir(request):
  return render (request,'kinesir.html')

def about(request):
  return render (request,'about.html')

def mdp(request):
  return render (request,'mdp.html')






  
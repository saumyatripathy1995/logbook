from django.http import HttpResponse
from django.shortcuts import render
from.models import Log
# Create your views here.
from django.views.decorators.csrf import csrf_exempt


def lb(request):
    return HttpResponse()
@csrf_exempt
def login(request):
    if request.method == "GET":
        return render(request,'log/login.html')
    elif request.method == "POST":
        username = request.POST["username"]
        password = request.POST["password"]
        if username == "somayo" and password == "epsumlabs":
            return HttpResponse('login successful')
        else :
            return HttpResponse('Enter Valid Username/Password')
def add(request):
    if request.method=="POST":
        name=request.POST["name"]
        date=request.POST["date"]
        description=request.POST["description"]
        time=request.POST["time"]
        ob=Log(name=name,date=date,description=description,time=time)
        ob.save(force_insert=True)
        return HttpResponse("Added Succesfully")
    else:
        return render(request,'log/add.html')
def view(request):
    if request.method=="GET":
        v=Log.objects.all()
        return render(request,"log/view.html",context={"data":v})

@csrf_exempt
def requestid(request):
    if request.method=="GET":
        return HttpResponse("This is a get request")
    elif request.method=="POST":
        return HttpResponse("This is a post request")
    elif request.method=="PUT":
        return HttpResponse("This is a put request")
    elif request.method=="DELETE":
        return  HttpResponse("This is a delete request")

@csrf_exempt
def viewbyusername(request,username):
    v=Log.objects.filter(name=username)

    return render(request,"log/view.html",context={"data":v})

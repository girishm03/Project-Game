from django.shortcuts import render, redirect
from games.models import catdb, gamedb
from django.core.files.storage import FileSystemStorage
from django.utils.datastructures import MultiValueDictKeyError
from django.contrib.auth import authenticate, login
from django.contrib.auth.models import User
from gfrontend.models import ContactDB
from django.contrib import messages
# Create your views here.
def INDEX(request):
    return render(request,"index.html")
def addcat(request):
    return render(request,"AddCategory.html")
def cdata(request):
    if request.method == "POST":
        na = request.POST.get('cname')
        img = request.FILES['cimage']
        obj = catdb(C_name=na, C_image=img)
        obj.save()
        messages.success(request, "Category added successfully...!")
        return redirect(addcat)
def displaycat(request):
    data = catdb.objects.all()
    return render(request, "DisplayCategory.html", {'data': data})
def Editcat(request, dataid):
    cdata = catdb.objects.get(id=dataid)
    return render(request,"EditCategory.html",{'cdata':cdata})
def updatecategory(request, dataid):
    if request.method == "POST":
        na = request.POST.get('cname')
        try:
            img = request.FILES['cimage']
            fs = FileSystemStorage()
            file = fs.save(img.name, img)
        except MultiValueDictKeyError:
            file = catdb.objects.get(id=dataid).C_image
        catdb.objects.filter(id=dataid).update(C_name=na, C_image=file)
        messages.info(request, "Category updated successfully...!")
        return redirect(displaycat)
def deletecategory(request, dataid):
    category1 = catdb.objects.filter(id=dataid)
    category1.delete()
    messages.error(request, "Category deleted successfully...!")
    return redirect(displaycat)
def addgame(request):
    cat = catdb.objects.all()
    return render(request,"AddGame.html",{'cat':cat})
def gamedata(request):
    if request.method=="POST":
        gca = request.POST.get('category')
        gna = request.POST.get('gname')
        gdec = request.POST.get('gdescription')
        gpri = request.POST.get('gprice')
        gimg = request.FILES['gimage']
        obj2 = gamedb(Category_name=gca,game_name=gna,game_desciption=gdec,game_price=gpri,game_image=gimg)
        messages.success(request, "Game added successfully...!")
        obj2.save()
        return redirect(addgame)
def displaygame(request):
    data = gamedb.objects.all()
    return render(request, "DisplayGame.html", {'data': data})
def editgame(request, game_id):
    cat = catdb.objects.all()
    game1 = gamedb.objects.get(id=game_id)
    return render(request,"EditGame.html",{'cat':cat,'game1':game1})
def updategame(request, dataid):
    if request.method == "POST":
        gca = request.POST.get('category')
        gna = request.POST.get('gname')
        gdec = request.POST.get('gdescription')
        gpri = request.POST.get('gprice')

        try:
            gimg = request.FILES['gimage']
            fs = FileSystemStorage()
            file = fs.save(gimg.name, gimg)
        except MultiValueDictKeyError:
            file = gamedb.objects.get(id=dataid).game_image
        gamedb.objects.filter(id=dataid).update(Category_name=gca,game_name=gna,game_desciption=gdec,game_price=gpri,game_image=file)
        messages.info(request, "Game updated successfully...!")
        return redirect(displaygame)
def deletegame(request, dataid):
    game2 = gamedb.objects.filter(id=dataid)
    game2.delete()
    messages.error(request, "Game deleted successfully...!")
    return redirect(displaygame)
def admin_login(r):
    return render(r,"AdminLogin.html")
def adminlogin(request):
    if request.method=="POST":
        un=request.POST.get('user_name')
        pwd=request.POST.get('pass_word')

        if User.objects.filter(username__contains=un).exists():
            x=authenticate(username=un,password=pwd)
            if x is not None:
                login(request,x)
                request.session['username']=un
                request.session['password']=pwd
                return redirect('INDEX')
            else:
                return redirect('admin_login')
        else:
            return redirect('admin_login')
def admin_logout(request):
    del request.session['username']
    del request.session['password']
    return redirect(admin_login)

def displayuser(request):
    data = ContactDB.objects.all()
    return render(request, "DisplayUsers.html", {'data': data})

def deleteuser(request, dataid):
    employee = ContactDB.objects.filter(id=dataid)
    employee.delete()
    return redirect(displayuser)
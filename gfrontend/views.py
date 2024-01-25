from django.shortcuts import render, redirect
from games.models import catdb,gamedb
from gfrontend.models import ContactDB, registerDB, cartdb
from django.contrib import messages
# Create your views here.
def gamepage(r):
    cat = catdb.objects.all()
    return render(r, "GamesHub.html", {'cat':cat})

def game1(request):
    prod = gamedb.objects.all()
    return render(request, "Pgames.html", {'prod':prod})

def game1_filtered(request, cat_name):
    data =gamedb.objects.filter(Category_name=cat_name)
    return render(request, "Pgames_filtered.html",{'data':data})

def sprod(request, proid):
    data = gamedb.objects.get(id=proid)
    return render(request, "singlegame.html", {'data':data})

def abtus(request):
    return render(request, "Aboutus.html")

def contact_page(request):
    return render(request, "Contactpage.html")

def contactdata(request):
    if request.method == "POST":
        una = request.POST.get('username')
        ag = request.POST.get('age')
        loc = request.POST.get('location')
        ema = request.POST.get('email')
        mob = request.POST.get('mobile')
        obj = ContactDB(User_Name=una,Location=loc ,Age=ag ,Email=ema, Mobile_Number=mob)
        obj.save()
        return redirect(contact_page)


def services_page(request):
    return render(request, "Services.html")

def register_page(request):
    return render(request, "Register.html")

def registerdata(request):
    if request.method == "POST":
        na = request.POST.get('name')
        mob = request.POST.get('mobile')
        ema = request.POST.get('email')
        una = request.POST.get('username')
        pwd = request.POST.get('password')
        obj = registerDB(Name=na ,Password=pwd ,UserName=una, Email=ema, Mobile_Number=mob)
        obj.save()
        return redirect(register_page)

def UserLogin(request):
    if request.method=="POST":
        un = request.POST.get('uname')
        pwd = request.POST.get('Pass_Word')
        if registerDB.objects.filter(UserName=un,Password=pwd).exists():
            request.session['UserName']=un
            request.session['Password']=pwd
            messages.success(request, "Welcome")
            return redirect(gamepage)
        else:
            messages.error(request, "Invalid UserName or Password")
            return redirect(register_page)
    return redirect(register_page)

def User_logout(request):
    del request.session['UserName']
    del request.session['Password']
    return redirect(register_page)

def Cart_page(request):
    data = cartdb.objects.filter(user_name=request.session['UserName'])
    totalprice = 0
    for d in data:
        totalprice = totalprice + d.Total_price
    return render(request, "cart.html", {'data': data, 'totalprice': totalprice})


def cartdata(request):
    if request.method == "POST":
        una = request.POST.get('uname')
        pna = request.POST.get('gname')
        pri = request.POST.get('gprice')
        tpri = request.POST.get('totalprice')
        obj = cartdb(user_name=una, Game_name=pna,Price=pri ,Total_price=tpri)
        obj.save()
        return redirect(Cart_page)

def cart_delete(request,pro_id):
    pro = cartdb.objects.filter(id=pro_id)
    pro.delete()
    return redirect(Cart_page)

def checkout_page(request):
    data = cartdb.objects.filter(user_name=request.session['UserName'])
    totalprice = 0
    for i in data:
        totalprice = totalprice + i.Total_price
    return render(request, "Checkout.html", {'data': data,'totalprice':totalprice})

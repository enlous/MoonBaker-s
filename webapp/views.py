from django.shortcuts import render, redirect
from backendapp.models import itemdb, Productdb,contactdb,divisiondb,Orderdb
from webapp.models import userdb
from django.contrib import messages


# Create your views here.


def Homepage(request):
    data = itemdb.objects.all()

    return render(request, "Home.html", {'data': data})


def Aboutpage(request):
    return render(request, "Aboutus.html")


def Contactpage(request):
    return render(request, "Contact.html")


def Categ(request):
    return render(request, "disCategory.html")


def DISPLAY(request, itemCatg):
    print("===itemCatg===", itemCatg)
    catg = itemCatg.upper()

    products = divisiondb.objects.filter(Category=itemCatg)
    context = {
        'products': products,
        'catg': catg
    }
    return render(request, "disCategory.html", context)

def Categg(request):
    return render(request, "dissubcategory.html")
def DISPLAYsubCAT(request, procatg):
    datas=Productdb.objects.all()
    print("===proCatg===", procatg)
    catgs = procatg.upper()

    pros =Productdb .objects.filter(subName=procatg)
    context = {
        'pros': pros,
        'catgs': catgs,
        'datas': datas
    }
    return render(request, "dissubcategory.html", context)


def proSingle(request, datasid):
    datas = Productdb.objects.get(id=datasid)
    return render(request, "productSingle.html", {'dat': datas})


def Registration(request):
    return render(request, "registration.html")


def ULogin(request):
    if request.method == "POST":
        na = request.POST.get('UserName')
        em = request.POST.get('Email')
        pa = request.POST.get('Password')
        cp = request.POST.get('CPassword')
        obj = userdb(UserName=na, Email=em, Password=pa, CPassword=cp)
        obj.save()
        return redirect(Registration)


def logIN(request):
    return render(request, "loggoooo.html")


def customerlogin(request):
    if request.method == 'POST':
        UserName_r = request.POST.get('UserName')
        Password_r = request.POST.get('Password')
        if userdb.objects.filter(UserName=UserName_r, Password=Password_r).exists():
            request.session['UserName'] = UserName_r
            request.session['Password'] = Password_r

            return redirect(Homepage)
        else:
            return render(request, 'registration.html', {'msg': "sorry...invalid password or username"})


def customerlogout(request):
    del request.session['UserName']
    del request.session['Password']
    return redirect(Registration)

def CONTACTSS(request):
    if request.method == "POST":
        na = request.POST.get('Name')
        em = request.POST.get('Email')
        su = request.POST.get('Subject')
        me = request.POST.get('msg')
        obj = contactdb(Name=na, Email=em, Subject=su, Message=me)
        obj.save()
        messages.success(request, "Message send successfully")
        return redirect(Contactpage)


def Payment(request):
    data = itemdb.objects.all()

    return render(request, "payment.html", {'data': data})

def order(request):
    if request.method == "POST":
        na = request.POST.get('Name')
        em = request.POST.get('Email')
        ad = request.POST.get('Address')
        obj = Orderdb(Name=na, Email=em, Address=ad)
        obj.save()
        messages.success(request,"Order placed successfully")
        return redirect(Homepage)


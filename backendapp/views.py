from django.contrib.auth import authenticate, login
from django.contrib.auth.models import User

from django.shortcuts import render, redirect
from backendapp.models import Logindb, itemdb, Productdb, contactdb, divisiondb,Orderdb
from django.core.files.storage import FileSystemStorage
from django.utils.datastructures import MultiValueDictKeyError


# Create your views here.
def Frontend(request):
    return render(request, "index.html")


def LogAdmin(request):
    return render(request, "login.html")


def Loginpage(request):
    if request.method == "POST":
        na = request.POST.get('Name')
        em = request.POST.get('Email')
        nu = request.POST.get('Number')
        un = request.POST.get('UserName')
        pa = request.POST.get('Password')
        img = request.FILES['Image']
        obj = Logindb(Name=na, Email=em, Number=nu, UserName=un, Password=pa, Image=img)
        obj.save()
        return redirect(LogAdmin)


def DisplayTable(request):
    data = Logindb.objects.all()
    return render(request, "Display_logintable.html", {'data': data})


def pageEdit(request, dataid):
    data = Logindb.objects.get(id=dataid)
    print(data)
    return render(request, "Editpage.html", {'data': data})


def updatePage(request, dataid):
    if request.method == "POST":
        na = request.POST.get('Name')
        em = request.POST.get('Email')
        nu = request.POST.get('Number')
        un = request.POST.get('UserName')
        pa = request.POST.get('Password')

        try:
            img = request.FILES['Image']
            fs = FileSystemStorage()
            file = fs.save(img.name, img)
        except MultiValueDictKeyError:
            file = Logindb.objects.get(id=dataid).Image
            Logindb.objects.filter(id=dataid).update(Name=na, Email=em, Number=nu, UserName=un, Password=pa, Image=file)

            return redirect(DisplayTable)


def Deletedata(request, dataid):
    data = Logindb.objects.filter(id=dataid)
    data.delete()
    return redirect(DisplayTable)


def addpage(request):
    return render(request, "catpage.html")


def itempage(request):
    if request.method == "POST":
        na = request.POST.get('Name')
        de = request.POST.get('Description')
        img = request.FILES['Image']

        obj = itemdb(Name=na, Description=de, Image=img)
        obj.save()
        return redirect(addpage)


def Itemdisp(request):
    data = itemdb.objects.all()
    return render(request, "DisplayyItem.html", {'data': data})


def EditItem(request, dataid):
    data = itemdb.objects.get(id=dataid)
    print(data)
    return render(request, "EditCat.html", {'data': data})


def updateitem(request, dataid):
    if request.method == "POST":
        na = request.POST.get('Name')
        de = request.POST.get('Description')
        try:
            img = request.FILES['Image']
            fs = FileSystemStorage()
            file = fs.save(img.name, img)
        except MultiValueDictKeyError:
            file = itemdb.objects.get(id=dataid).Image
        itemdb.objects.filter(id=dataid).update(Name=na, Description=de, Image=file)

        return redirect(Itemdisp)


def DeleteItem(request, dataid):
    data = itemdb.objects.filter(id=dataid)
    data.delete()
    return redirect(Itemdisp)


# product

def propage(request):
    data = divisiondb.objects.all()
    return render(request, "productPage.html", {'data': data})


def Propagedetails(request):
    if request.method == "POST":
        ca = request.POST.get('subName')
        na = request.POST.get('Name')
        pr = request.POST.get('Price')
        qn = request.POST.get('Quantity')
        ds = request.POST.get('Description')
        img = request.FILES['Image']
        obj = Productdb(subName=ca, Name=na, Price=pr, Quantity=qn, Description=ds, Image=img)
        obj.save()
        return redirect(propage)


def prodisp(request):
    data = Productdb.objects.all()
    return render(request, "DisplayProduct.html", {'data': data})


def Editpro(request, dataid):
    data = Productdb.objects.get(id=dataid)
    da = divisiondb.objects.all()
    print(data)
    return render(request, "EditProduct.html", {'data': data, 'da': da})


def updatePro(request, dataid):
    if request.method == "POST":
        ca = request.POST.get('subName')
        na = request.POST.get('Name')
        pr = request.POST.get('Price')
        qn = request.POST.get('Quantity')
        ds = request.POST.get('Description')
        try:
            img = request.FILES['Image']
            fs = FileSystemStorage()
            file = fs.save(img.name, img)
        except MultiValueDictKeyError:
            file = Productdb.objects.get(id=dataid).Image
        Productdb.objects.filter(id=dataid).update(subName=ca, Name=na, Price=pr, Quantity=qn, Description=ds,
                                                   Image=file)

        return redirect(prodisp)


def Deletepro(request, dataid):
    data = Productdb.objects.filter(id=dataid)
    data.delete()
    return redirect(prodisp)


def USERlogin(request):
    return render(request, "UserLOGIN.html")


def adminlogin(request):
    if request.method == "POST":
        username_r = request.POST.get('username')
        password_r = request.POST.get('password')

        if User.objects.filter(username__contains=username_r).exists():
            user = authenticate(username=username_r, password=password_r)
            if user is not None:
                login(request, user)
                request.session['username'] = username_r
                request.session['password'] = password_r
                return redirect(Frontend)
            else:
                return redirect(USERlogin)
        else:
            return redirect(USERlogin)


def adminlogout(request):
    del request.session['username']
    del request.session['password']
    return redirect(USERlogin)

def Contactdisp(request):
    data = contactdb.objects.all()
    return render(request, "ContactDisplay.html", {'data': data})


def DeleteContact(request, dataid):
    data = contactdb.objects.filter(id=dataid)
    data.delete()
    return redirect(Contactdisp)


def divpage(request):
    data = itemdb.objects.all()
    return render(request, "divideditems.html", {'data': data})


def divpagedetails(request):
    if request.method == "POST":
        ca = request.POST.get('Category')
        na = request.POST.get('subName')
        ds = request.POST.get('Description')
        img = request.FILES['Image']
        obj = divisiondb(Category=ca, subName=na, Description=ds, Image=img)
        obj.save()

        return redirect(divpage)


def divdisp(request):
    data = divisiondb.objects.all()
    return render(request, "dividedTable.html", {'data': data})


def divEdit(request, dataid):
    data = divisiondb.objects.get(id=dataid)
    da = itemdb.objects.all()
    print(data)
    return render(request, "dividedEdit.html", {'data': data, 'da': da})


def divupdate(request, dataid):
    if request.method == "POST":
        ca = request.POST.get('Category')
        na = request.POST.get('subName')

        ds = request.POST.get('Description')
        try:
            img = request.FILES['Image']
            fs = FileSystemStorage()
            file = fs.save(img.name, img)
        except MultiValueDictKeyError:
            file = divisiondb.objects.get(id=dataid).Image
        divisiondb.objects.filter(id=dataid).update(Category=ca, subName=na, Description=ds, Image=file)

        return redirect(divdisp)


def divDelete(request, dataid):
    data = divisiondb.objects.filter(id=dataid)
    data.delete()
    return redirect(divdisp)

def DeleteContact(request, dataid):
    data = contactdb.objects.filter(id=dataid)
    data.delete()
    return redirect(Contactdisp)

def Orderdisp(request):
    data = Orderdb.objects.all()
    return render(request, "ORDERING.html", {'data': data})


def Deleteorder(request, dataid):
    data = Orderdb.objects.filter(id=dataid)
    data.delete()
    return redirect(Orderdisp)

import datetime
from django.shortcuts import render, redirect  
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from main.forms import ProductEntryForm
from main.models import Product
from django.http import HttpResponse, HttpResponseRedirect
from django.core import serializers
from django.urls import reverse

# Create your views here.

def register(request):
    form = UserCreationForm()

    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Your account has been successfully created!')
            return redirect('main:login')
    context = {'form':form}
    return render(request, 'register.html', context)

def login_user(request):
   if request.method == 'POST':
      form = AuthenticationForm(data=request.POST)

      if form.is_valid():
        user = form.get_user()
        login(request, user)
        response = HttpResponseRedirect(reverse("main:show_main"))
        response.set_cookie('last_login', str(datetime.datetime.now()))
        return response

   else:
      form = AuthenticationForm(request)
   context = {'form': form}
   return render(request, 'login.html', context)

def logout_user(request):
    logout(request)
    response = HttpResponseRedirect(reverse('main:login'))
    response.delete_cookie('last_login')
    return response

@login_required(login_url='/login')

def show_main(request):
    product_entries = Product.objects.filter(user=request.user)
    context = {
        'name' : request.user.username,
        'nama' : "Farrell Zidane Raihandrawan",
        'npm' : "2306275600",
        'kelas' : "PBP B",

        'item_name1': 'Manchester United 98/99 UCL Final',
        'item_description1' : '''This is Ole Gunnar Solksjaer's Match Worn
                                jersey who scored the last minute game winner.''',
        'price1' : '150.000.000',
        'item_rating1' : '9/10',

        'item_name2': 'Blackburn Rovers 94/95 ',
        'item_description2' : '''This is Alan Shearer's Match Worn
                                jersey who led the team wins the Premier League.''',
        'price2' : '100.000.000',
        'item_rating2' : '9/10',

        'item_name3': 'France Home jersey WC 2006',
        'item_description3' : '''This is Zinedine Zidane's Match Worn
                                jersey when he did the iconic headbutt.''',
        'price3' : '150.000.000',
        'item_rating3' : '10/10',

        'product_entries': product_entries,
        'last_login': request.COOKIES['last_login'],


    }

    return render(request, "main.html", context)


def create_product_entry(request):
    form = ProductEntryForm(request.POST or None)

    if form.is_valid() and request.method == "POST":
        product_entry = form.save(commit=False)
        product_entry.user = request.user
        product_entry.save()
        return redirect('main:show_main')

    context = {'form': form}
    return render(request, "create_product_entry.html", context)

def show_xml(request):
    data = Product.objects.all()
    return HttpResponse(serializers.serialize("xml", data), content_type="application/xml")

def show_xml_by_id(request, id):
    data_id = Product.objects.filter(pk=id)
    return HttpResponse(serializers.serialize("xml", data_id), content_type="application/xml")

def show_json(request):
    data = Product.objects.all()
    return HttpResponse(serializers.serialize("json", data), content_type="application/json")

def show_json_by_id(request, id):
    data_id = Product.objects.filter(pk=id)
    return HttpResponse(serializers.serialize("json", data_id), content_type="application/json")



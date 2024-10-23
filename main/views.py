from django.shortcuts import render 

def home(request):
    return render(request,'home.html')

def shop(request):
    return render(request,'shop.html')

def contact(request):
    return render(request,'contact.html')

def checkout(request):
    return render(request,'checkout.html')

def productdetail(request):
    return render(request,'productdetail.html')

def about(request):
    return render(request,'about.html')

def cart(request):
    return render(request,'cart.html')

def blog(request):
    return render(request,'blog.html')

def blogdetail(request):
    return render(request,'blogdetail.html')
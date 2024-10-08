from django.shortcuts import render,redirect,HttpResponse
from django.contrib.auth import authenticate,login,logout
from  django.contrib.auth.decorators import login_required
from .forms import *
from .models import *
#data form 
def home(request):
    if request.method=='POST':
        form=courseform(request.POST,request.FILES)
        if form.is_valid():
            form.save()
            
    r=courseform()
    return render(request,'course.html',{'form':r})
#home page
def getdata(request):
    data=course.objects.all()
    return render(request,'getdata.html',{'data':data})

#course page
@login_required(login_url='login')
def course_view(request):
    data=course.objects.all()
    return render(request,"course_view.html",{'data':data})

#register form
def register(request):
    if request.method=='POST':
        form=registerform(request.POST)
        if form.is_valid():
            form.save()
            return redirect('getdata')
    r=registerform()
    return render(request,'registration.html',{'data':r})

#login form
def login_view(request):
    if request.method=='POST':
        form1=loginform(request.POST)
        if form1.is_valid():
            username=form1.cleaned_data['username']
            password=form1.cleaned_data['password']
            user=authenticate(username=username,password=password)
            if user:
                login(request,user)
                return redirect('course')
            else:
                return HttpResponse("invali username or password")
    return render(request,'login.html')

#logout form
def logout_view(request):
    logout(request)
    return redirect('getdata')

#profile  page

@login_required(login_url='login')
def profile(request):
    user=request.user
    return render(request,'profiledata.html',{'user':user})

#increase the cart or add to cart items
@login_required(login_url='login')
def add_to_cart(request,id):
    Courses=course.objects.get(id=id)
    cartitem,created=cart_item.objects.get_or_create(user=request.user,Courses=Courses)
    cartitem.quantity+=1
    cartitem.save()
    return redirect('viewcart')
#decrese the cart items
def remove_cart(request,id):
    cartitem=cart_item.objects.get(id=id)
    if cartitem.quantity>1:
        cartitem.quantity-=1
        cartitem.save()
    else:
        cartitem.delete()
    return redirect('viewcart')
#display  the items

def coursedata(request):
    data=course.objects.all()
    return render(request,'coursedata.html',{'data':data})

#display cart items
@login_required(login_url='login')
def Cart_item_view(request):
    data=cart_item.objects.all()
    return render(request,'Cartdata.html',{'data':data})

#display cart items
@login_required(login_url='login')
def View_cart(request):
    data=cart_item.objects.all()
    total=sum(i.Courses.price*i.quantity for i in data) 
    return render(request,'viewcart.html',{'data':data ,'total':total})

#delete entire  cart items
@login_required(login_url='login')
def del_cartitem(request,id):
    cartitem=cart_item.objects.get(id=id)
    cartitem.delete()
    return redirect('viewcart')

#search the cart item
def search_product(request):
    data=request.GET['q']
    courses=course.objects.filter(coursename__icontains=data)
    return render(request,'search.html',{'courses':courses})




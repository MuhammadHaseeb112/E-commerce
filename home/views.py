from ast import If
from django.contrib import messages
from django.http import HttpResponse
from django.shortcuts import render,redirect
from django.contrib.auth.models import User, auth
import os
from .models import *
from .forms import *
from django.views.decorators.cache import cache_control #new
from django.core.paginator import Paginator
from django.core.files.storage import FileSystemStorage

from keras.models import load_model
from keras_preprocessing.image import img_to_array, load_img
import numpy as np
import matplotlib.pyplot as plt

import datetime

global_bike = None
global_rate = None

basepath = os.path.dirname(__file__)
MODEL_PATH = os.path.join(basepath,'static\\ClassificationModel.h5')

model1 = load_model("home\\static\\ClassificationModel.h5",compile=False)  


from keras.preprocessing.image import ImageDataGenerator

train_datagen = ImageDataGenerator(rescale = 1./255,
                                   shear_range = 0.2,
                                   zoom_range = 0.2,
                                   horizontal_flip = True)

train_directory="home\\static\\train"
training_set = train_datagen.flow_from_directory(train_directory,
                                                 target_size = (200, 200),
                                                 batch_size = 32,
                                                 class_mode = 'categorical')

lab = training_set.class_indices
lab={k:v for v,k in lab.items()}

def output(location):
    img=load_img(location,target_size=(200,200,3))
    img=img_to_array(img)
    img=img/255
    img=np.expand_dims(img,[0])
    answer=model1.predict(img)
    y_class = answer.argmax(axis=-1)
    y = " ".join(str(x) for x in y_class)
    y = int(y)
    res = lab[y]
    print("Clasifications:  ",res)
    return res

# "C:\Users\Admin\Pictures\8.png"




def test(request):
    s_user= request.session['username']
    check = Buyer_info.objects.filter(seller_name=s_user).exists()
    print("ali")
    print(check)

    return render(request, 'test.html',{'show_Notification':check})



@cache_control(no_chache=True,must_revalidate=True,no_store=True) #new
def admin_users(request):
    if request.user.is_authenticated and request.session['super_user'] == True:
        users = User.objects.all()
        return render(request,'admin_users.html', {'users': users})
    else:
        messages.info(request, "you are logout! To cheak users Please login first")
        print('your account is logout to cheak users please login first')
        return redirect('admin')


def delete_user(request, id,username):
    if request.user.is_authenticated:
        print(id)
        print(username)
        user = User.objects.get(id=id,username=username)
        bike = bikes.objects.filter(username=username)
        car = cars.objects.filter(username=username)
        laptop = laptops.objects.filter(username=username)
        mobile = mobiles.objects.filter(username=username)
        info = User_info.objects.filter(User_name=username)
        if bike:
            bike.delete()
        if car:
            car.delete()
        if laptop:    
            laptop.delete()
        if mobile:
            mobile.delete()
        if info:
            info.delete()
        if user:
            user.delete()
        messages.info(request, "User Deleted Succesfully")
        return redirect('admin_users')
    else:
        messages.info(request, "Please login First")
def bikes_page(request):
    dests = bikes.objects.filter(disable=False).order_by('-id')
    paginator = Paginator(dests, 20)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    nums = 'a' * page_obj.paginator.num_pages
    return render(request, 'bikes_page.html', {'page_obj': page_obj,'nums': nums})

def cars_page(request):
    dests = cars.objects.filter(disable=False).order_by('-id')
    paginator = Paginator(dests, 20)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    nums = 'a' * page_obj.paginator.num_pages
    return render(request, 'bikes_page.html', {'page_obj': page_obj,'nums': nums})

def mobiles_page(request):
    dests = mobiles.objects.filter(disable=False).order_by('-id')
    paginator = Paginator(dests, 20)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    nums = 'a' * page_obj.paginator.num_pages
    return render(request, 'bikes_page.html', {'page_obj': page_obj,'nums': nums})

def laptops_page(request):
    dests = laptops.objects.filter(disable=False).order_by('-id')
    paginator = Paginator(dests, 20)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    nums = 'a' * page_obj.paginator.num_pages
    return render(request, 'bikes_page.html', {'page_obj': page_obj,'nums': nums})

@cache_control(no_chache=True,must_revalidate=True,no_store=True) #new
def login(request):
    if not request.user.is_authenticated:
        if request.method == 'POST':
            username = request.POST['username']
            password = request.POST['password']
            username = username.strip()
            password = password.strip()
            # user = auth.authenticate(username==username,password==password)
            user = auth.authenticate(username=username,password=password)
            superusers = User.objects.filter(username=username,is_superuser=True)
            if superusers:
                request.session['super_user'] = True
                ss_user= request.session['super_user']
            else:
                request.session['super_user'] = False
                ss_user= request.session['super_user']
# and not superusers
            if user is not None :
                print("you are login")
                auth.login(request, user)
                request.session['username'] = username
                s_user= request.session['username']

                print('you are ' , request.session.get('username'))
                print('user = ', s_user)
                return redirect("home")
            else:
                messages.info(request, "invalid username or password")
                return redirect("login")

        else:
            return render(request,'login.html')
    else:
        messages.info(request, "your account is already login! please logout first")
        return redirect('home')



        
@cache_control(no_chache=True,must_revalidate=True,no_store=True) #new
def logout(request):
    
    auth.logout(request)
    request.session.flush()
    request.session.clear_expired()
    print('you are ' , request.session.get('username'))
    return redirect('home')

@cache_control(no_chache=True,must_revalidate=True,no_store=True) #new
def home(request):
    dests = []
    i=0
    dests_new = bikes.objects.filter(disable=False).order_by('?')
    # dests = dests[10]
    for val in dests_new:
        if i<10:
            dests.append(val)
            i = i+1
        else:
            break
    
    car = []
    i=0
    car_new = cars.objects.filter(disable=False).order_by('?')
    for val in car_new:
        if i<10:
            car.append(val)
            i = i+1
        else:
            break

    mobile = []
    i=0
    mobile_new = mobiles.objects.filter(disable=False).order_by('?')
    for val in mobile_new:
        if i<10:
            mobile.append(val)
            i = i+1
        else:
            break
    # mobile = mobiles.objects.all()
    laptop = []
    i=0
    laptop_new = laptops.objects.filter(disable=False).order_by('?')
    for val in laptop_new:
        if i<10:
            laptop.append(val)
            i = i+1
        else:
            break
    # laptop = laptops.objects.all()
    
    return render(request,'home.html', {'dests': dests,'car':car,'mobile':mobile,'laptop':laptop})
    

@cache_control(no_chache=True,must_revalidate=True,no_store=True) #new
def success(request):
	return HttpResponse('successfully uploaded')

@cache_control(no_chache=True,must_revalidate=True,no_store=True) #new
def aboutus(request):
    return render(request,'aboutus.html')

@cache_control(no_chache=True,must_revalidate=True,no_store=True) #new
def admin_products(request):
    if request.user.is_authenticated and request.session['super_user'] == True:
        return render(request,'admin_products.html')
    else:
        messages.info(request, "you are logout! to cheak a Products Please login first")
        print('your account is logout to cheak products please login first')
        return redirect('admin')


@cache_control(no_chache=True,must_revalidate=True,no_store=True) #new
def admin(request):
    return render(request,'admin.html')

@cache_control(no_chache=True,must_revalidate=True,no_store=True) #new
def contactus(request):
    if request.method == 'POST':
        # form = bikesForm(request.POST, request.FILES)
        form = contactForm(request.POST)
        form.save()
        messages.info(request, "Your Message is sent to Admin")
        return render(request,'contactus.html')
    else:
        return render(request,'contactus.html')
@cache_control(no_chache=True,must_revalidate=True,no_store=True) #new
def manage_product(request):
    if request.user.is_authenticated:
        dests = bikes.objects.filter(username= request.session.get('username'))
        car = cars.objects.filter(username= request.session.get('username'))
        mobile = mobiles.objects.filter(username= request.session.get('username'))
        laptop = laptops.objects.filter(username= request.session.get('username'))
        return render(request,'manage_product.html', {'dests':dests, 'car':car, 'mobile':mobile, 'laptop':laptop})
    else:
        messages.info(request, "you are logout! to cheak a Products Please login first")
        print('please login first')
        return redirect('home')


@cache_control(no_chache=True,must_revalidate=True,no_store=True) #new
def signup(request):
    
    if request.method == 'POST':

        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        username = request.POST['username']
        email = request.POST['email']
        password1 = request.POST['password1']
        password2 = request.POST['password2']

        # first_name = first_name.strip()
        # last_name = last_name.strip()
        # username = username.strip()
        # email = email.strip()
        # password1 = password1.strip()
        # password2 = password2.strip()


        if password1 == password2: 
            if User.objects.filter(username=username).exists():
                print("user name already taken")
                messages.info(request, 'username taken')
                return redirect('signup')
            elif User.objects.filter(email=email).exists():
                print("Email already registered")
                messages.info(request, 'Email taken')
                return redirect('signup')
            else:
                user = User.objects.create_user(email=email, password=password1, username=username, first_name=first_name, last_name=last_name)
                user.save();
                print('user created')
                messages.info(request, 'user created')
            return render(request, 'login.html')
        else:
            print("password not matched")
            messages.info(request, 'password not matched')
            return redirect('signup')
    else:
        return render(request, 'signup.html')


def edit(request, id,catagory):
    print(id)
    print(catagory)
    if catagory == "bikes":
        bike = bikes.objects.get(id=id,catagory=catagory)
        return render(request, 'edit.html', {'bike' : bike})
    elif catagory == "cars":
        bike = cars.objects.get(id=id,catagory=catagory)
        return render(request, 'edit.html', {'bike' : bike})
    elif catagory == "mobiles":
        bike = mobiles.objects.get(id=id,catagory=catagory)
        return render(request, 'edit.html', {'bike' : bike})
    elif catagory == "laptops":
        bike = laptops.objects.get(id=id,catagory=catagory)
        return render(request, 'edit.html', {'bike' : bike})
    else:
        print('something went wrong')

def admin_delete(request, id,catagory):
    if request.user.is_authenticated and request.session['super_user'] == True:
        if catagory == 'bikes':
            bike = bikes.objects.get(id=id,catagory=catagory)
            bike.delete()
            return redirect('admin_products')
        elif catagory == 'cars':
            bike = cars.objects.get(id=id,catagory=catagory)
            bike.delete()
            return redirect('admin_products')
        elif catagory == 'mobiles':
            bike = mobiles.objects.get(id=id,catagory=catagory)
            bike.delete()
            return redirect('admin_products')
        elif catagory == 'laptops':
            bike = laptops.objects.get(id=id,catagory=catagory)
            bike.delete()
            return redirect('admin_products')
        else:
            print('something went wrong')
    else:
        messages.info(request, "Please login first")


def delete(request, id,catagory):
    if catagory == 'bikes':
        bike = bikes.objects.get(id=id,catagory=catagory)
        bike.delete()
        return redirect('manage_product')
    elif catagory == 'cars':
        bike = cars.objects.get(id=id,catagory=catagory)
        bike.delete()
        return redirect('manage_product')
    elif catagory == 'mobiles':
        bike = mobiles.objects.get(id=id,catagory=catagory)
        bike.delete()
        return redirect('manage_product')
    elif catagory == 'laptops':
        bike = laptops.objects.get(id=id,catagory=catagory)
        bike.delete()
        return redirect('manage_product')
    else:
        print('something went wrong')

@cache_control(no_chache=True,must_revalidate=True,no_store=True) #new
def adminlogin(request):
    if not request.user.is_authenticated:
        if request.method == 'POST':
            username = request.POST['username']
            password = request.POST['password']
            username = username.strip()
            password = password.strip()
            # user = auth.authenticate(username==username,password==password)
            user = auth.authenticate(username=username,password=password)
            superusers = User.objects.filter(username=username,is_superuser=True)
            if superusers:
                request.session['super_user'] = True
                ss_user= request.session['super_user']
            else:
                request.session['super_user'] = False
                ss_user= request.session['super_user']

            if user is not None and superusers:
                print("you are login as admin")
                auth.login(request, user)
                request.session['username'] = username
                s_user= request.session['username']

                print('you are ' , request.session.get('username'))
                print('user = ', s_user)
                return redirect("admin_users")
            else:
                messages.info(request, "invalid username or password")
                return redirect("login")

        else:
            return render(request,'login.html')
    else:
        messages.info(request, "your account is already login! please logout first")
        return redirect('home')



@cache_control(no_chache=True,must_revalidate=True,no_store=True) #new
def add_product(request):
    if request.user.is_authenticated:
        if request.method == 'POST':

            if request.method == 'POST':
                form = bikesForm(request.POST, request.FILES)
                # form1 = bikesForm(request.POST, request.FILES)
                form.save(commit=False)
                imagefile = request.FILES['img']
                fs = FileSystemStorage()
                filename = fs.save(imagefile.name, imagefile)
                file_url = fs.url(filename)
                print(file_url)
                
                file_path = os.getcwd()
                file_path_full = os.path.join(file_path,'media',filename)
                print(file_path_full)
                                
                print(MODEL_PATH)
                img=file_path_full
                pic=load_img(img,target_size=(200,200,3))
                plt.imshow(pic)
                result_final = output(img)
                print("result_final is ", result_final)
                if 'bikes' in result_final:
                    # form.data['img'] = file_url
                    form.save()
                    print("Data for bike category save successfully.")
                    # return HttpResponse("picture saved")
                    return redirect('manage_product')
                else:
                    messages.info(request, "Invalid Picture!")
                    return redirect('add_product')
            else:
                form = bikesForm()
            return render(request, 'add_product.html')
            # for bikes end         
        else:
            return render(request,'add_product.html')
    else:
        messages.info(request, "you are logout! to add a Product Please login first")
        print('to add a product please login first')
        return redirect('home')

@cache_control(no_chache=True,must_revalidate=True,no_store=True) #new
def add_productcars(request):
    if request.method == 'POST':
        # for cars start
        # geeting data from cars form
        if request.method == 'POST':
            form1 = carsForm(request.POST, request.FILES)

                # if form1.is_valid():

            
                # form1 = bikesForm(request.POST, request.FILES)
            form1.save(commit=False)
            imagefile = request.FILES['img']
            fs = FileSystemStorage()
            filename = fs.save(imagefile.name, imagefile)
            file_url = fs.url(filename)
            print(file_url)
                
            file_path = os.getcwd()
            file_path_full = os.path.join(file_path,'media',filename)
            print(file_path_full)
                                
            print(MODEL_PATH)
            img=file_path_full
            pic=load_img(img,target_size=(200,200,3))
            plt.imshow(pic)
            result_final = output(img)
            print("result_final is ", result_final)
            if 'Cars' in result_final:
                    # form.data['img'] = file_url
                form1.save()
                print("Data for bike category save successfully.")
                    # return HttpResponse("picture saved")
                return redirect('manage_product')
            else:
                messages.info(request, "Invalid Picture!")
                return redirect('add_product')
                # return HttpResponse("picture not saved")






            
            
        else:
            form1 = carsForm()
        return redirect('add_product')
        # for cars end         
    else:
        return redirect('add_product')

@cache_control(no_chache=True,must_revalidate=True,no_store=True) #new
def add_productmobiles(request):
    if request.method == 'POST':
        # for cars start
        # geeting data from cars form
        if request.method == 'POST':
            form1 = mobilesForm(request.POST, request.FILES)

                # if form1.is_valid():

            form1.save(commit=False)
            imagefile = request.FILES['img']
            fs = FileSystemStorage()
            filename = fs.save(imagefile.name, imagefile)
            file_url = fs.url(filename)
            print(file_url)
                
            file_path = os.getcwd()
            file_path_full = os.path.join(file_path,'media',filename)
            print(file_path_full)
                                
            print(MODEL_PATH)
            img=file_path_full
            pic=load_img(img,target_size=(200,200,3))
            plt.imshow(pic)
            result_final = output(img)
            print("result_final is ", result_final)
            if 'mobiles' in result_final:
                    # form.data['img'] = file_url
                form1.save()
                print("Data for bike category save successfully.")
                    # return HttpResponse("picture saved")
                return redirect('manage_product')
            else:
                messages.info(request, "Invalid Picture!")
                return redirect('add_product')


            
        else:
            form1 = mobilesForm()
        return redirect('add_product')
        # for cars end         
    else:
        return redirect('add_product')

@cache_control(no_chache=True,must_revalidate=True,no_store=True) #new
def add_productlaptops(request):
    if request.method == 'POST':
        # for cars start
        # geeting data from cars form
        if request.method == 'POST':
            form1 = laptopsForm(request.POST, request.FILES)

                # if form1.is_valid():

            
            form1.save(commit=False)
            imagefile = request.FILES['img']
            fs = FileSystemStorage()
            filename = fs.save(imagefile.name, imagefile)
            file_url = fs.url(filename)
            print(file_url)
                
            file_path = os.getcwd()
            file_path_full = os.path.join(file_path,'media',filename)
            print(file_path_full)
                                
            print(MODEL_PATH)
            img=file_path_full
            pic=load_img(img,target_size=(200,200,3))
            plt.imshow(pic)
            result_final = output(img)
            print("result_final is ", result_final)
            if 'laptops' in result_final:
                    # form.data['img'] = file_url
                form1.save()
                print("Data for bike category save successfully.")
                    # return HttpResponse("picture saved")
                return redirect('manage_product')
            else:
                messages.info(request, "Invalid Picture!")
                return redirect('add_product')


            
        else:
            form1 = laptopsForm()
        return redirect('add_product')
        # for cars end         
    else:
        return redirect('add_product')



def admin_manage_product(request, catagory):
    if request.user.is_authenticated and request.session['super_user'] == True:
        print(catagory)
        if catagory == "bikes":    
            dests = bikes.objects.all().order_by('-id')
            paginator = Paginator(dests, 20)
            page_number = request.GET.get('page')
            page_obj = paginator.get_page(page_number)
            nums = 'a' * page_obj.paginator.num_pages
            return render(request, 'admin_manage_product.html', {'page_obj': page_obj,'nums': nums})
        if catagory == "cars":    
            dests = cars.objects.all().order_by('-id')
            paginator = Paginator(dests, 20)
            page_number = request.GET.get('page')
            page_obj = paginator.get_page(page_number)
            nums = 'a' * page_obj.paginator.num_pages
            return render(request, 'admin_manage_product.html', {'page_obj': page_obj,'nums': nums})
        if catagory == "mobiles":    
            dests = mobiles.objects.all().order_by('-id')
            paginator = Paginator(dests, 20)
            page_number = request.GET.get('page')
            page_obj = paginator.get_page(page_number)
            nums = 'a' * page_obj.paginator.num_pages
            return render(request, 'admin_manage_product.html', {'page_obj': page_obj,'nums': nums})
        if catagory == "laptops":    
            dests = laptops.objects.all().order_by('-id')
            paginator = Paginator(dests, 20)
            page_number = request.GET.get('page')
            page_obj = paginator.get_page(page_number)
            nums = 'a' * page_obj.paginator.num_pages
            return render(request, 'admin_manage_product.html', {'page_obj': page_obj,'nums': nums})
    else:
        print('please login first')
        return redirect('login')

        # return render(request,'admin_manage_product.html')
    # return render(request,'admin_manage_product.html')

def admin_update(request, id,catagory):
    print('Haseeb')
    print(id)
    print(catagory)
    if catagory== 'bikes':
        bike = bikes.objects.get(id=id,catagory=catagory)
        form = admin_bikesForm(request.POST, request.FILES, instance=bike)
        print("form saved")
        form.save()
        print("redirecting")
        return redirect('admin_products')
    elif catagory== 'cars':
        bike = cars.objects.get(id=id,catagory=catagory)
        form = admin_carsForm(request.POST, request.FILES, instance=bike)
        form.save()
        return redirect('admin_products')
    elif catagory== 'mobiles':
        bike = mobiles.objects.get(id=id,catagory=catagory)
        form = admin_mobilesForm(request.POST, request.FILES, instance=bike)
        form.save()
        return redirect('admin_products')
    elif catagory== 'laptops':
        bike = laptops.objects.get(id=id,catagory=catagory)
        form = admin_laptopsForm(request.POST, request.FILES, instance=bike)
        form.save()
        return redirect('admin_products')
    else:
        print('something went wrong')
        HttpResponse('404 Error')

def update(request, id,catagory):
    print('Haseeb')
    print(catagory)
    if catagory== 'bikes':
        bike = bikes.objects.get(id=id,catagory=catagory)
        form = bikesForm(request.POST, request.FILES, instance=bike)
        form.save()
        return redirect('manage_product')
    elif catagory== 'cars':
        bike = cars.objects.get(id=id,catagory=catagory)
        form = carsForm(request.POST, request.FILES, instance=bike)
        form.save()
        return redirect('manage_product')
    elif catagory== 'mobiles':
        bike = mobiles.objects.get(id=id,catagory=catagory)
        form = mobilesForm(request.POST, request.FILES, instance=bike)
        form.save()
        return redirect('manage_product')
    elif catagory== 'laptops':
        bike = laptops.objects.get(id=id,catagory=catagory)
        form = laptopsForm(request.POST, request.FILES, instance=bike)
        form.save()
        return redirect('manage_product')
    elif catagory== "varified":
        bike = Buyer_info.objects.get(id=id)
        form = Buyer_infoForm(request.POST, instance=bike)
        form.save()
        return redirect('home')
    else:
        print('something went wrong')
        HttpResponse('404 Error')


def view_product(request, id,catagory):
    print(id)
    print(catagory)
    if request.user.is_authenticated:
        s_user= request.session['username']
        currentTime=datetime.datetime.now()
        print("ali")
        print(currentTime)
        rate = Rating.objects.filter(product_id=id,Product_catagory=catagory)
        review = Buyer_info.objects.filter(Buyer_name=s_user,product_id=id).last()
        print("haseeb")
        global global_rate
        global_rate = rate
        if review:
            if str(currentTime) <= str(review.EndTime) and review.varification == True :        
                try:
                    
                    if Rating.objects.filter(buyer_id=int(review.id)).exists():
                        print("you can not comment because you already submited your feedback")
                        comment= False
                    else:
                        comment= True
                        print('you can comment')
                except Exception as e:
                    print(e)
                    comment= False
            else:
                comment= False
                print('you can not comment')
        else:
            comment= False

        global global_bike
        if catagory == "bikes":
            bike = bikes.objects.get(id=id,catagory=catagory)
            print(bike.username)
            info = User_info.objects.get(User_name=bike.username)
            global_bike = bike
            return render(request, 'view_product.html', {'bike':bike,'rate':rate,'review':review,'comment':comment,'info':info})
            
        elif catagory == "cars":
            bike = cars.objects.get(id=id,catagory=catagory)
            print(bike.username)
            info = User_info.objects.get(User_name=bike.username)
            global_bike = bike
            return render(request, 'view_product.html', {'bike':bike,'rate':rate,'review':review,'comment':comment,'info':info})
        
        elif catagory == "laptops":
            bike = laptops.objects.get(id=id,catagory=catagory)
            print(bike.username)
            info = User_info.objects.get(User_name=bike.username)
            global_bike = bike
            return render(request, 'view_product.html', {'bike':bike,'rate':rate,'review':review,'comment':comment,'info':info})
        
        else:
            bike = mobiles.objects.get(id=id,catagory=catagory)
            print(bike.username)
            info = User_info.objects.get(User_name=bike.username)
            global_bike = bike
            return render(request, 'view_product.html', {'bike':bike,'rate':rate,'review':review,'comment':comment,'info':info})
    else:
        rate = Rating.objects.filter(product_id=id,Product_catagory=catagory)
        # global global_rate
        global_rate = rate
        # global global_bike
        review = None
        comment = None
        if catagory == "bikes":
            bike = bikes.objects.get(id=id,catagory=catagory)
            global_bike = bike
            return render(request, 'view_product.html', {'bike':bike,'rate':rate,'review':review,'comment':comment})
        elif catagory == "cars":
            bike = cars.objects.get(id=id,catagory=catagory)
            global_bike = bike
            return render(request, 'view_product.html', {'bike':bike,'rate':rate,'review':review,'comment':comment})
        
        elif catagory == "laptops":
            bike = laptops.objects.get(id=id,catagory=catagory)
            global_bike = bike
            return render(request, 'view_product.html', {'bike':bike,'rate':rate,'review':review,'comment':comment})
        
        else:
            bike = mobiles.objects.get(id=id,catagory=catagory)
            global_bike = bike
            return render(request, 'view_product.html', {'bike':bike,'rate':rate,'review':review,'comment':comment})


def buy_now(request, ProductId,ProductName,SellerName,UserName):
    print(ProductId)
    print(ProductName)
    print(SellerName)
    print(UserName)
    
    if SellerName==UserName:
        messages.info(request, "You can not buy your own product")
        print('You can not buy your own product')

        global global_bike,global_rate
        return render(request, 'view_product.html', {'bike':global_bike,'rate':global_rate})
    else:
        info = Buyer_info.objects.create(Buyer_name=UserName, seller_name=SellerName, product_id=ProductId, Product_name=ProductName)
        info.save();
        messages.info(request, 'your request to buy product is sent to seller')
        print('your request to buy product is sent to seller')
        return redirect('home')



def submit(request):
    form = RatingForm(request.POST, request.FILES)
    form.save()
    return redirect('home')

@cache_control(no_chache=True,must_revalidate=True,no_store=True) #new
def notification(request):
    s_user= request.session['username']

    print('you are ' , request.session.get('username'))
    print('user = ', s_user)
    seller = Buyer_info.objects.filter(seller_name=s_user)    

    return render(request,'notification.html', {'seller':seller,})

def search(request):
    if request.method == 'POST':    
        given_name = request.POST['name']
        print(given_name)
        # page_obj = bikes.objects.filter(name=given_name)
        # if not employee:
        bike = bikes.objects.filter(name__icontains=given_name)
        car = cars.objects.filter(name__icontains=given_name)
        mobile = mobiles.objects.filter(name__icontains=given_name)
        laptop = laptops.objects.filter(name__icontains=given_name)
        # if not employee:
        #     employee = Employee.objects.filter(eemail__iexact=given_name)
        # if not employee:
        #     employee = Employee.objects.filter(econtact=given_name)
        # if not employee:
        #     print('search not found')
        return render(request, 'search.html',{'bike':bike,'car':car,'mobile':mobile,'laptop':laptop})
    # return render(request,'notification.html', {'seller':seller,})

def userinfo(request):
    if request.method == 'POST':
        s_user= request.session['username']
        print(s_user)
        info = User_info.objects.filter(User_name=s_user)
        if info:
            info = User_info.objects.get(User_name=s_user)
            form = User_infoForm(request.POST, request.FILES, instance=info)
            form.save()
        else:
            form = User_infoForm(request.POST, request.FILES)
            form.save()
        return redirect('home')
    else:
        return render(request, 'userinfo.html')
    # return render(request,'notification.html', {'seller':seller,})

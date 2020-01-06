from django.shortcuts import render_to_response, redirect, render
from django.contrib.auth import logout as auth_logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import auth
from django.contrib.auth import logout
from .models import Profile,User,Gallery
import datetime
from django.core.files.storage import FileSystemStorage
from django.shortcuts import get_object_or_404
from .forms import Profile_form,Gallery_form
from django.core.mail import send_mail

# Create your views here.
def signup(request):
    return render(request,'signup.html')

#def info(request):
#    return render(request,'new.html')

def user_register(request):
    if request.user.first_visit:
        return render(request,'user_register.html')
    else:
        return redirect('/')

def user_register_details(request):
   # profile = Profile()
    
    if request.method == 'POST' and request.FILES['profile_pic']:

        profile_pic = request.FILES['profile_pic']
        fs = FileSystemStorage()
        filename = fs.save(profile_pic.name,profile_pic)
        uploaded_file_url = fs.url(filename)

        email = request.user.email
        regdno = request.POST['regdno']
        passout_year = request.POST['passout_year']
        branch = request.POST['branch']
        contactno = request.POST['contactno']
        profession = request.POST['profession']
        company = request.POST['company']
        work_location = request.POST['work_location']
        designation = request.POST['designation']
        work_country = request.POST['work_country']
        street_name = request.POST['street_name']
        street_number = request.POST['street_number']
        city = request.POST['city']
        state = request.POST['state']
        district = request.POST['district']
        country = request.POST['country']

        profile = Profile.objects.create(profile_pic = filename,email=email,regdno = regdno,passout_year = passout_year,branch = branch,contactno = contactno,profession = profession,company= company,work_location = work_location,designation = designation,work_country = work_country,street_name = street_name,street_number = street_number,city = city,state = state,district = district,country = country)
        request.user.first_visited()
        request.user.profile = profile
        profile.save()
        request.user.save()

        subject = 'Account Created !!'
        message = 'Welcome to Nalanda Institute Of Technology,' + request.user.first_name +'You are the Alumini of our College, Your account is created please wait till Admin approve you, then you can See your Profile on the Alumini Cell, Have a great day.'
        sender = 'NitAlumini2020@gmail.com'
        receiver = request.user.email
        send_mail(subject,message,sender,[receiver],fail_silently=False)
       # request.user.first_visit()
        return redirect('/')
        #return render(request,'profile.html',{'profile':profile})

    else:
        return render(request,'user_register.html')

def logout(request):
    auth.logout(request)
    return redirect('/')

def profile(request):
    print(request.user.email)
    #user = User.objects.get(email=request.user.email)
    #print(user.profile.regdno)
    uemail = request.user.email
    
    #profile = Profile.objects.get(email = uemail)
    user = User.objects.get(email=request.user.email)
    gallery = Gallery.objects.filter(email=request.user.email)
    #return render(request,'profile.html',{'profile':profile})
    return render(request,'profile.html',{'user':user,'gallery':gallery})

def alumini_cell(request):
    user = User.objects.all()
    eleven = User.objects.filter(profile__passout_year='2011').order_by('profile__regdno').filter(is_approved='True')
    twelve = User.objects.filter(profile__passout_year='2012').order_by('profile__regdno').filter(is_approved='True')
    thirteen = User.objects.filter(profile__passout_year='2013').order_by('profile__regdno').filter(is_approved='True')
    fourteen = User.objects.filter(profile__passout_year='2014').order_by('profile__regdno').filter(is_approved='True')
    fifteen = User.objects.filter(profile__passout_year='2015').order_by('profile__regdno').filter(is_approved='True')
    sixteen = User.objects.filter(profile__passout_year='2016').order_by('profile__regdno').filter(is_approved='True')
    seventeen = User.objects.filter(profile__passout_year='2017').order_by('profile__regdno').filter(is_approved='True')
    eighteen = User.objects.filter(profile__passout_year='2018').order_by('profile__regdno').filter(is_approved='True')
    nineteen = User.objects.filter(profile__passout_year='2019').order_by('profile__regdno').filter(is_approved='True')
    twenty = User.objects.filter(profile__passout_year='2020').order_by('profile__regdno').filter(is_approved='True')
    return render(request,'alumini_cell.html',{'eleven':eleven,'twelve':twelve,'thirteen':thirteen,'fourteen':fourteen,'fifteen':fifteen,'sixteen':sixteen,'seventeen':seventeen,'eighteen':eighteen,'nineteen':nineteen,'twenty':twenty})


def edit_profile(request):
    #print('chandan mannnnnnna')
    uemail = request.user.email
    #print(uemail)
    #uprofile = get_object_or_404(Profile,email = uemail)
    uprofile = Profile.objects.get(email = uemail)
    print(uprofile.regdno)
    if request.method == 'POST':
        form = Profile_form(request.POST or None,request.FILES or None,instance = uprofile)
        if form.is_valid():
            form = form.save()
            return redirect('profile')
    else:
        form = Profile_form(instance = uprofile)

    return render(request,'edit_profile.html',{'form':form})


def show_profile(request,email):

    user = User.objects.get(email = email)
    gallery = Gallery.objects.filter(email=email)
    return render(request,'view_profile.html',{'user':user,'gallery':gallery})

def approval(request):

    users = User.objects.filter(is_approved = 'False')
    return render(request,'approval.html',{'users':users})

def accept(request,email):
    user = User.objects.get(email = email)
    user.make_approve()
    user.save()
    subject = 'Approval'
    first_name = user.first_name.title()
    message = 'Congratulations,' +first_name + '. Now you are approved and you can find your Profile on the Alumini Cell .'
    sender = 'NitAlumini2020@gmail.com'
    receiver = email
    send_mail(subject,message,sender,[receiver],fail_silently=False)
    return redirect('approval')

def remove(request,email):
    user = User.objects.get(email = email)
    if user.profile:
        user.profile.delete()
    if user.gallery:
        user.gallery.delete()
    user.delete()
    return redirect('approval')

def add_images(request):
    if request.method == 'POST':
        form = Gallery_form(request.POST or None,request.FILES or None)
        if form.is_valid():
            form = form.save(commit = False)
            form.email = request.user.email
            form.save()
            #request.user.gallery = form
            request.user.save()
            return redirect('profile')
    else:
        form = Gallery_form()
    return render(request,'add_images.html',{'form':form})
   # return render(request,'add_images.html',{'form':form})

def delete_image(request,pk):

    user = User.objects.get(email = request.user.email)
    image = Gallery.objects.get(pk = pk)
    print(image.pk)
    image.delete()
    #user.gallery.save()
    return redirect('profile')

def search_result(request):
    email = request.POST['top-search-bar-email']
    res = User.objects.get(email = email)

    return render(request,'search_result.html',{'res':res})

def contact_mail(request):
    name = request.POST['name_sender']
    email = request.POST['email_sender']
    message = request.POST['message_sender']
    send_mail(name,message,email,['NitAlumini2020@gmail.com'],fail_silently=False)
    return redirect('/')







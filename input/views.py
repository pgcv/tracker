from django.http import HttpResponse
from django.shortcuts import render, redirect
from .models import UserInfo,File
from django.contrib.auth.decorators import login_required
from django.views.decorators.cache import cache_control
from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render_to_response,redirect
from django.template import RequestContext
from django.db.models import Q
from django.contrib import messages
from django.core.files.storage import FileSystemStorage
from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render, get_object_or_404, redirect
from ssdtracker import Det
import os

@cache_control(no_cache=True, must_revalidate=True)

def index(request):
	return render(request, 'input/applanding.html')


def signup(request):
	return render(request, 'input/signup.html')

def signup_form_submission(request):
	company_name = request.POST["company_name"]
	username = request.POST["username"]
	email = request.POST["email"]
	phone = request.POST["phone"]
	password = request.POST["password"]


	user_info = UserInfo(company_name=company_name, username=username, email=email, phone=phone, password=password)
	if company_name:
		user_info.save()
		return render(request, 'input/applanding.html')
	else:
		return render(request, 'input/signup.html')	

def signin(request):
    username = password = ''
    
    request.session['name']="user"
    context={}
    if request.POST:
        username = request.POST.get('username')
        password = request.POST.get('password')
        request.session['uname'] = username
        context['all_posts']=UserInfo.objects.all().filter(Q(email__icontains=username))
        user = authenticate(username=username, password=password)
        context['files']=File.objects.all().filter(Q(name=username))

        if username:
        	if password:
        		match= UserInfo.objects.filter(Q(email__icontains=username)&Q(password__icontains=password ))
        		if match:
        			return render(request, 'input/results.html', context)
        		else:
        			messages.error(request,'username or password not correct!')
        			return render(request, 'input/applanding.html')
  	
		
       
        '''
        if user is not None:
            if user.is_active:
                login(request, user)
                return HttpResponseRedirect('input/signup.html')
        '''	
    return render(request, 'input/applanding.html')

def showvideo():
    username=request.session['uname']    
    if username:
        match=File.objects.filter(Q(name_icontains=username))
        if match:
            return render(request, 'input/results.html', {'files': UserInfo.objects.all().filter(Q(email__icontains=username))})


def signout(request):
	return render(request, 'input/results.html')


def signout(request):
    if request.method == "POST":
        logout(request)

        return redirect('signin')

def upload(request):
    context={}
    check={}
    flag=0
    uploaded_file=request.FILES['document']
    fs=FileSystemStorage()
    name=fs.save(uploaded_file.name,uploaded_file)
    context['url']=fs.url(name)
    filepath= fs.url(name)
    filename= request.session['uname']
    context['all_posts']=UserInfo.objects.all().filter(Q(email__icontains=filename))
    check['test']=File.objects.all().filter(Q(name=filename))
    for ch in check['test']:
        cha=""
        cha=str(ch).rsplit(' ')[1]
        leng=len(cha)-4
        cha=str(cha)
        cha=cha[:leng]
        filepa=str(filepath)
        if str(cha) == filepa[:leng]:
            flag=1

    #return render(request,'input/results.html',context)
    form= File(name=filename,processed=0,filepath=filepath)
    if(flag==0):
        form.save()

    username=request.session['uname']  
    fileurl=filepath.rsplit('/')
    filep=fileurl[1]+'/'+fileurl[2]
    det = Det()
    det.process_video(filep)  
    context['files']=File.objects.all().filter(Q(name=username)) 
    return render(request, 'input/results.html', context)


def uploadprofile(request):
    context={}
    uploaded_file=request.FILES['image']
    fs=FileSystemStorage()
    name=fs.save(uploaded_file.name,uploaded_file)
    context['url']=fs.url(name)
    filepath= fs.url(name)
    filepath=filepath+"profile_image"
    filename= request.session['uname']
    context['all_posts']=UserInfo.objects.all().filter(Q(email__icontains=filename))


    #return render(request,'input/results.html',context)
    #form= UserInfo(company_name=company_name, username=username, email=email, phone=phone, password=password,image=filepath)
    #form.save()
       
    
      
    return render(request, 'input/results.html', context)    

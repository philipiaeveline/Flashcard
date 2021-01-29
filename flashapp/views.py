from django.shortcuts import render,redirect,get_object_or_404
from django.http import HttpResponse,Http404
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.views import LogoutView
from django.contrib.auth import login
from .models import Author,Picture,Category,Location
from .forms import SignUpForm,NewPostForm,EditProfileForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout
from django.contrib.auth.models import User
from django.contrib import messages
# Create your views here.

def signUp(request):    
    if request.method=='POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            name=form.cleaned_data['username']
            email = form.cleaned_data['email']
            send=welcome_email(name,email)
            HttpResponseRedirect('pics')
    else:
        form = SignUpForm()
    return render(request,'registration/registration_form.html',{'form':form})

@login_required(login_url = '/accounts/login/')
def pics(request):
    category = Category.get_categories()
    pictures = Picture.all_pics()
    location_pics = Location.get_location()
    return render(request,'pics.html',{'pictures': pictures, 'category': category, 'location_pics':location_pics })
@login_required(login_url = '/accounts/login/')
def profile(request):
    user_posts = Picture.user_pics(request.user)
    return render(request,'profile.html',{'user_posts':user_posts})

@login_required(login_url = '/accounts/login/')
def edit_profile(request):

    if request.method=='POST':
        form = EditProfileForm(request.POST,request.FILES)
        if form.is_valid():
            form.save()
            return redirect('profile')

    else:
        form = EditProfileForm(instance=request.user)
    return render(request,'update_profile.html',{'form':form})





@login_required(login_url = '/accounts/login/')
def single_pic(request,id):
    try:
        pic = Picture.objects.get(id = id)
    except DoesNotExist:
        raise Http404()
    return render(request,"single_pic.html", {"pic":pic})
    
@login_required(login_url = '/accounts/login/')
def new_post(request):
    if request.method=='POST':
        form = NewPostForm(request.POST,request.FILES)
        if form.is_valid():
            post=form.save(commit=False)
            post.user = request.user
            post.save()
            return redirect('pics')
    else:
        form = NewPostForm()
    return render(request,'new_post.html',{'form':form})

def search_results(request):
    if 'image' in request.GET and request.GET["image"]:
        search_term = request.GET.get('image')
        searched_pics = Picture.search_by_name(search_term)
        message = f'{search_term}'
        return render(request,'search.html',{"message":message,"image":searched_pics})
    else:
        message = "You have not entered anything to search"
        return render(request,'search.html',{"message":message})
@login_required(login_url = '/accounts/login/')
def viewPics_by_location(request,location):
    locationpic = Picture.view_pictures_by_location(location)
    return render(request,"location_pics.html",{"locationpic":locationpic})

@login_required(login_url = '/accounts/login/')
def viewPics_by_category(request,category):
    photos =Picture.view_pictures_by_category(category)
    return render (request,'category.html',{"photos":photos})

@login_required(login_url="/accounts/login/")
def logout_request(request):
    logout(request)
    return redirect('pics')



@login_required(login_url = '/accounts/login/')
def search_results(request):
    if 'image' in request.GET and request.GET['image']:
        search_term = request.GET.get('image')
        searched_pics = Picture.search_image(search_term)
        message = f'{search_term}'

        return render(request,'search.html',{'message':message,'image':searched_pics})

    else:
        message = "You have not entered anything to search"
        return render(request,'search.html',{"message":message})

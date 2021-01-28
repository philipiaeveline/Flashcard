from django.shortcuts import render,redirect
from django.http import HttpResponse,Http404
from .models import Author,Picture,Category,Location

# Create your views here.

def pics(request):
    category = Category.get_categories()
    pictures = Picture.all_pics()
    location_pics = Location.get_location()

    return render(request,'pics.html',{'pictures': pictures, 'category': category, 'location_pics':location_pics })


def single_pic(request,id):
    try:
        pic = Picture.objects.get(id = id)
    except DoesNotExist:
        raise Http404()
    return render(request,"single_pic.html", {"pic":pic})

def search_results(request):
    if 'image' in request.GET and request.GET["image"]:
        search_term = request.GET.get('image')
        searched_pics = Picture.search_by_name(search_term)
        message = f'{search_term}'

        return render(request,'search.html',{"message":message,"image":searched_pics})

    else:
        message = "You have not entered anything to search"
        return render(request,'search.html',{"message":message})

def viewPics_by_location(request,location):
    locationpic = Picture.view_pictures_by_location(location)
    return render(request,"location_pics.html",{"locationpic":locationpic})


def viewPics_by_category(request,category):
    photos =Picture.view_pictures_by_category(category)
    return render (request,'category.html',{"photos":photos})

from django.http import HttpResponse
from django.http import HttpResponseRedirect
from django.template import loader
from .models import artists
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt

@csrf_exempt
def get_values(request):
    if request.method == 'POST':
        table = artists()
        table.firstname = request.POST.get('fname')
        table.lastname = request.POST.get('lname')
        table.email = request.POST.get('email')
        table.band = request.POST.get('band')
        table.dateOfBirth = request.POST.get('dateOfBirth')
        table.musicGenre = request.POST.get('musicGenre')
        table.username = '@' + request.POST.get('uname')
        table.gender = request.POST.get('gender')
        table.password = request.POST.get('password')
        table.save()
        return HttpResponseRedirect('/login')
    
def members(request):
    usData = artists.objects.all().values()
    template = loader.get_template('main.html')
    context = {
        'all_users' : usData
    }
    return HttpResponse(template.render(context, request))

def sccn(request):
    hotti = loader.get_template('myfirst.html')
    return HttpResponse(hotti.render())

def login(request):
    usData = artists.objects.all().values()
    template = loader.get_template('login.html')
    context = {
        'users': usData
    }
    return HttpResponse(template.render(context, request))

def userhome(request, id):
    user_data = artists.objects.get(id = id)
    template = loader.get_template('userhomepage.html')
    context = {
        'user': user_data,
        'pp': str(user_data.pp)
    }
    return HttpResponse(template.render(context, request))

def userprofile(request, id):
    user_data = artists.objects.get(id = id)
    template = loader.get_template('userprofile.html')
    try:
        context = {
            'user': user_data,
            'cover': str(user_data.coverphoto),
            'pp': str(user_data.pp),
            'bios': user_data.bio[2:-2].replace("\\'", "'").replace('\\r", "', "\\r', '").replace('\\r", \'', "\\r', '").replace('\\r\', "', "\\r', '").split("\\r', '")
        }
    except:
        context = {
            'user': user_data,
            'cover': str(user_data.coverphoto),
            'pp': str(user_data.pp)
        }
    return HttpResponse(template.render(context, request))

def profiledit(request, id):
    user_data = artists.objects.get(id = id)
    template = loader.get_template('profiledit.html')
    try:
        context = {
            'user': user_data,
            'cover': str(user_data.coverphoto),
            'pp': str(user_data.pp),
            'bios': user_data.bio[2:-2].replace("\\'", "'").replace('\\r", "', "\\r', '").replace('\\r", \'', "\\r', '").replace('\\r\', "', "\\r', '").split("\\r', '")
        }
    except:
        context = {
            'user': user_data,
            'cover': str(user_data.coverphoto),
            'pp': str(user_data.pp)
        }
    return HttpResponse(template.render(context, request))

@csrf_exempt
def profilesave(request, id):
    user_data = artists.objects.get(id = id)
    user_data.bio = str(request.POST['bio']).split('\n')
    user_data.firstname = request.POST['fname']
    user_data.lastname = request.POST['lname']
    user_data.band = request.POST['band']
    user_data.dateOfBirth = request.POST['dateOfBirth']
    user_data.musicGenre = request.POST['musicGenre']
    try:
        user_data.coverphoto = request.FILES['cover']
    except:
        pass
    try:
        user_data.pp = request.FILES['pp']
    except:
        pass
    user_data.save()
    return HttpResponseRedirect('/userprofile/' + str(id))

def post(request, id):
    user_data = artists.objects.get(id = id)
    template = loader.get_template('post.html')
    context = {
        'user': user_data,
        'cover': str(user_data.coverphoto),
        'pp': str(user_data.pp)
    }
    return HttpResponse(template.render(context, request))

@csrf_exempt
def postsave(request, id):
    user_data = artists.objects.get(id = id)
    if user_data.text_post == None:
        user_data.text_post = []
    if user_data.media_post == '':
        user_data.media_post = []
    user_data.save()
    initdata_tp = user_data.text_post
    #initdata_mp = list(user_data.media_post)
    user_data.text_post = request.POST['textpost']
    try:
        user_data.media_post = request.FILES['mediapost']
    except:
        pass
    user_data.save()
    user_data.text_post = initdata_tp
    #user_data.media_post = initdata_mp.insert(0, str(user_data.media_post))
    user_data.save()
    return HttpResponseRedirect('/userhome/' + str(id))

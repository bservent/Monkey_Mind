from django.shortcuts import render, redirect, get_object_or_404
from .models import Meditation, Profile, Category
from main_app.forms import Profile_Form
from django.http import HttpResponse


#-----------------------------------------------------------------------------#
#                                S T A T I C                                  #
#-----------------------------------------------------------------------------#

def home(request):
    return render(request, 'home.html')

def register(request):
    return render(request, 'register.html')

def signin(request):
    return render(request, 'signin.html')

#-----------------------------------------------------------------------------#
#                                C A T E G O R Y                              #
#-----------------------------------------------------------------------------#
def categories_browse(request):
    categories = Category.objects.all()

    meditations_data = []
    for category in categories:
        meditations = Meditation.objects.filter(category_id=category.id)
        category_data = { 'category_name' : category.name, 'meditations' : meditations }
        meditations_data.append(category_data)
        print(meditations[0].name)
        return render(request, 'browse.html', { 'meditations_data' : meditations_data })


#-----------------------------------------------------------------------------#
#                                P R O F I L E                                #
#-----------------------------------------------------------------------------#

def profile(request, user_id):
    meditations = Meditation.objects.filter(user=request.user.id)
    profiles = Profile.objects.filter(user=request.user)
    context = { 'meditations' : meditations, 'profile' : request.user, 'profile' :profile }
    return render(request, 'profile.html', context)

def create_profile(request, user_id):
    error_message=''
    if request.method == 'POST':
        profile_form = Profile_Form(request.POST, request.FILES, instance = request.user.profile)
        if profile_form.is_valid():
            profile_form.save()
            return redirect('profile')
        else:
            error_message='Invalid sign-up try again'
    else: 
        profile_form = Profile_Form()
    
        # context = {'profile_form': profile_form}

        # return render(request, 'create_profile.html', context)

        return render(request, 'create_profile.html', {'profile_form': profile_form})
#-----------------------------------------------------------------------------#
#                                M E D I T A T I O N                          #
#-----------------------------------------------------------------------------#

from django.shortcuts import render, redirect, get_object_or_404
from .models import Meditation, User, Category


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
    # profiles = Profile.objects.filter(user=request.user)
    context = { 'meditations' : meditations, 'profile' : request.user, 'profile' :profile }
    return render(request, 'profile.html', context)

#-----------------------------------------------------------------------------#
#                                M E D I T A T I O N                          #
#-----------------------------------------------------------------------------#

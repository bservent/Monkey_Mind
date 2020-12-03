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
        Profile.objects.get_or_create(user=request.user)
        profile_form = Profile_Form(request.POST, request.FILES, instance = request.user.profile)
        if profile_form.is_valid():
            new_profile = profile_form.save()
            new_profile.user = request.user
            new_profile.save()
            return redirect('profile', new_profile.id)
        else:
            error_message='Invalid sign-up try again'
    else: 
        # profile_form = Profile_Form(instance=request.user.profile)
        profile_form = Profile_Form()
        context = {'profile_form': profile_form}
        return render(request, 'create_profile.html', context)

def edit_profile(request, user_id):
    sel_profile = Profile.objects.get(user_id=user_id)
    if request.method == 'POST':
        profile_form = Profile_Form(request.POST, instance=sel_profile)
        if profile_form.is_valid():
            updated_profile = profile_form.save()
            return redirect('profile', updated_profile.id)
    else:
        profile_form = Profile_Form(instance=sel_profile)
        context = { 'profile' : sel_profile, 'profile_form': profile_form }
        return render(request, 'edit_profile.html', context)

def delete_profile(request, user_id):
    print(user_id)
    Profile.objects.get(user_id=user_id).delete()
    return redirect('/')

#-----------------------------------------------------------------------------#
#                                M E D I T A T I O N                          #
#-----------------------------------------------------------------------------#

def meditation_detail(request, meditation_id):
    return render(request, 'meditation_detail.html') 

def add_collecting(request, meditation_id):
    form = CollectingForm(request.POST)
    if form.is_valid():
        add_collecting = form.save(commit=False)
        add_collecting.plant_id = plant_id
        add_collecting.save()
    return redirect('plants_detail', plant_id=plant_id)
    
def delete_collecting(request, collecting_id, plant_id):
    #plant = Plant.objects.get(id=plant_id)
    Collecting.objects.get(id=collecting_id).delete()
    return redirect('plants_detail', plant_id=plant_id)
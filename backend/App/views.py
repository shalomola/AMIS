from django.shortcuts import render, redirect
from django.contrib.auth.models import User, auth
from django.contrib import messages
from .models import *
from django.contrib.auth.decorators import login_required
from .forms import AssignmentForm

# Create your views here.


def index(request):
    return render(request, 'index.html')

# @login_required(login_url='login')
def register(request):
    if request.method == 'POST':
        username = request.POST['username']
        first_name = request.POST['fname']
        last_name = request.POST['lname']
        email = request.POST['email']
        password = request.POST['password']
        cpassword = request.POST['cpassword']

        #Check if passwords match
        if password == cpassword:
            #Check if email exists in the system
            if User.objects.filter(email=email).exists():
                messages.info(request, 'Email already in use')
                return redirect('register')
            #Check if username exists in the system
            elif User.objects.filter(username=username).exists():
                messages.info(request, 'Username already in use')
                return redirect('register')
            else:
                # Create user
                user = User.objects.create_user(username=username, email=email, password=password, first_name=first_name, last_name=last_name)
                user.save()


                #Log user in and redirect to settings page
                user_login = auth.authenticate(username=username, password=password)
                auth.login(request, user_login)

                #Create a Staff object for each user
                user_model = User.objects.get(username=username)
                new_staff = Staff.objects.create(user=user_model, staff_id=user_model.id, username=user_model.username, fname=user_model.first_name, lname=user_model.last_name)
                new_staff.save()
                return redirect('settings')

        else:
            messages.info(request, 'Password validation failed')
            return redirect('register')
    else:        
        return render(request, 'register.html')

def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        user = auth.authenticate(username=username, password=password)

        if user is not None:
            auth.login(request, user)
            return redirect('dashboard')
        else:
            messages.info(request, 'Invalid credentials')
            return redirect('login')
    else:
        return render(request, 'login.html')

@login_required(login_url='login')
def logout(request):
    auth.logout(request)
    return redirect('/')

@login_required(login_url='login')
def settings(request):
    user_profile = Staff.objects.get(user=request.user)
    # username = Staff.objects.get(user=request.user.username)

    if request.method == 'POST':
        if request.FILES.get('img') == None:
            image = user_profile.profileimg
            fname = request.POST['fname']
            lname = request.POST['lname']
            email = request.POST['email']
            position = request.POST['position']
            dept = request.POST['dept']

            user_profile.profileimg = image
            user_profile.fname = fname
            user_profile.lname = lname
            user_profile.email = email
            user_profile.position = position
            user_profile.dept = dept
            user_profile.save()

        if request.FILES.get('img') != None:
            image = request.FILES.get('img')
            fname = request.POST['fname']
            lname = request.POST['lname']
            email = request.POST['email']
            position = request.POST['position']
            dept = request.POST['dept']

            user_profile.profileimg = image
            user_profile.fname = fname
            user_profile.lname = lname
            user_profile.email = email
            user_profile.position = position
            user_profile.dept = dept
            user_profile.save()

        return redirect('login')
    return render(request, 'settings.html', {'user_profile': user_profile})

@login_required(login_url='login')
def userprofile(request):
    # user_object = User.objects.get(username=request.user)
    user_profile = Staff.objects.get(user=request.user)

    context = {
        'user_profile': user_profile
    }
    return render(request, 'userprofile.html', context)

def userassets(request):
    user_profile = Staff.objects.get(user=request.user)

    user_asset = AssetsIssuance.objects.filter(asset_assignee=user_profile)
    return render(request, 'userassets.html', {'user_profile': user_profile, 'user_asset': user_asset})

@login_required(login_url='login')
def dashboard(request):
    user_profile = Staff.objects.get(user=request.user)

    staff = Staff.objects.all()
    staff_count = staff.count()

    assets = Assets.objects.all()
    assets_count = assets.count()

    assignments = AssetsIssuance.objects.all()
    assignments_count = assignments.count()

    if request.method == 'POST':
        todo = request.POST['new_todo']


        new_todo = Todo.objects.create(todo=todo)
        new_todo.save()



    todos = Todo.objects.all()

    context = {'navbar': 'dashboard', 'staff_count': staff_count, 'assets_count': assets_count, 'todos': todos, 'assignments_count': assignments_count, 'user_profile': user_profile}

    return render(request, 'dashboard.html', context)

def assetlist(request):
    assets = Assets.objects.all()
    return render(request, 'assetlist.html', {'assets': assets, 'navbar': 'assetlist'})

@login_required(login_url='login')
def userprofiles(request):
    staffs = Staff.objects.all()
    return render(request, 'userprofiles.html', {'staffs': staffs, 'navbar': 'userprofiles'})

def assignments(request):
    assignments = AssetsIssuance.objects.all()
    return render(request, 'assignments.html', {'navbar': 'assignments', 'assignments': assignments})

def addasset(request):
    categories = Categories.objects.all()

    if request.method == 'POST':
        if request.FILES.get('asset-img') == None:
            asset_id = request.POST['asset-id']
            asset_name = request.POST['asset-name']
            asset_category = request.POST['asset-category']
            asset_manufacturer = request.POST['asset-manufacturer']
            date_purchased = request.POST['date-purchased']

            
            new_asset = Assets.objects.create(asset_id=asset_id, asset_name=asset_name, asset_category=asset_category, asset_manufacturer=asset_manufacturer, date_purchased=date_purchased)
            new_asset.save()


        if  request.FILES.get('asset-img') != None:
            asset_image = request.FILES.get('asset-img')
            asset_id = request.POST['asset-id']
            asset_name = request.POST['asset-name']
            asset_category = request.POST['asset-category']
            asset_manufacturer = request.POST['asset-manufacturer']
            date_purchased = request.POST['date-purchased']

            
            new_asset = Assets.objects.create(asset_image=asset_image, asset_id=asset_id, asset_name=asset_name, asset_category=asset_category, asset_manufacturer=asset_manufacturer, date_purchased=date_purchased)
            new_asset.save()


        return redirect('assetlist')
    return render(request, 'addasset.html', {'categories': categories})

def assignasset(request):

    if request.method == 'POST':
        form = AssignmentForm(request.POST)
        if form.is_valid():
            form.save()
        return redirect('/assignments')
    else:
        form = AssignmentForm()
        context = {
            'form': form
        }
        return render(request, 'assignasset.html', context)


def todoDelete(request,id):
    todo = Todo.objects.get(id=id)
    todo.delete()
    return redirect('dashboard')

def deleteAsset(request, id):
    asset = Assets.objects.get(id=id)
    asset.delete()
    return redirect('assetlist')

def deleteStaff(request, id):
    staff = Staff.objects.get(id=id)
    staff.delete()
    return redirect('userprofiles')

# def searchStaff(request):
#     if request.method == 'POST':
#         searched = request.POST['searched']
#         staff = Staff.objects.filter(name__contains = searched)

#         return render(request, )
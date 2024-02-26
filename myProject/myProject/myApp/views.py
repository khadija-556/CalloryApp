from django.shortcuts import render, HttpResponse, redirect
from .forms import *
from django.contrib.auth import authenticate,login,logout

def SignupPage(request):
    if request.method == "POST":
        form = UserForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('loginPage')
    else:
        form = UserForm()
    return render(request, "signup.html", {'form': form })

def loginPage(request):
    if request.method == "POST":
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data.get("username")
            password = form.cleaned_data.get("password")
            user = authenticate(username= username, password= password)
            login(request, user)
            return redirect("homePage")
    else:
        form = LoginForm()
    return render(request, "login.html", {'form':form})

def homePage(request):
    return render(request, "home.html")

def logoutPage(request):
    logout(request)
    return redirect("loginPage")

def updateProfile(request):
    user = request.user
    user_instance = User.objects.get(id=user.id)
    obj=0
    try:
        obj = UserProfile.objects.get(user=user_instance)
    except:
        pass

    if request.method == "POST" and obj:
        form = ProfileUpdateForm(request.POST,instance=obj)
        if form.is_valid():
            form.save()
            return redirect('profilePage')                                
    elif request.method == "POST":
        form = ProfileUpdateForm(request.POST)
        if form.is_valid():
            form2=form.save(commit=False)
            form2.user = request.user
            form2.save()
            return redirect('profilePage')

    elif obj:
        form = ProfileUpdateForm(instance=obj)
    else:
        form = ProfileUpdateForm()



    return render(request, "updateProfile.html",{'form':form})
                                 
   

def profilePage(request):

    user = request.user
    info = 0 
    msg = 0 
    BMR=0
    try:
        info = UserProfile.objects.get(user= user)

        if info.gender == "male":
            BMR = 66.47 + (13.75*info.weight) + (5.003*info.height) - (6.755*info.age)
        else:
            BMR = 655.1 + (9.563*info.weight) + (1.850*info.height) - (4.676*info.age)

        info.BMR = BMR 
        info.save()
    except:
        msg = "Please Update Your Profile First"
    
    return render(request,"profile.html", {'info': info, 'msg':msg,'BMR':BMR})

def calloryadd(request):
    if request.method == 'POST':
        form=calloryForm(request.POST)
        if form.is_valid():
            form2=form.save(commit=False)
            form2.user = request.user
            form2.save()
            return redirect('profilePage')
    else:
        form = calloryForm()

    return render(request, "calloryAdd.html", {'form':form})

def dashboard(request):
    munni=request.user
    sum=0
    needCal=0
    bmr= 0
    item = []
    if request.method == "POST":
        date=request.POST.get("Date")

        bmr = UserProfile.objects.get(user=request.user).BMR
        obj=callory.objects.filter(user=munni)
        item= obj.filter(date=date)
        for i in item:
            sum=sum+i.callory
    
        needCal=bmr-sum



    return render(request,'dashboard.html',{'sum':sum,'needCal':needCal,'bmr':bmr  })

from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login
from .forms import ExtendedUserCreationForm, UserProfil,OtvetForm
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import logout as django_logout

@login_required
def logout(request):
    django_logout(request)
    return  HttpResponseRedirect('/login')




# Create your views here.


#def startapp(request):
#    if request.method == 'POST':
#        fullname = request.POST['fullname']
#        age = request.POST['age']
#        email = request.POST['email']
#        specialite = request.POST['specialite']
#        language = request.POST['language']
#        vibor_test = Vibor_test.objects.all() 
#        vb = [vibor_test]  
#        user = User.objects.create(fullname=fullname, age=age, email=email, 
#                                specialite=specialite, language=language)
#        user.save()
#        print('lalalal')
#        return redirect('/admin',{'vb': vibor_test})
#    else:
#        return render(request, 'index.html')

#def startapp(request): 
#    context ={}
#    form = User(request.POST) 
#    if form.is_valid():
#        form.save()
#        return test(request)
#        
#    else:
#        return render(request, "index.html", context ) 
#  
#def test(request):
#        #survey = Otvet.objects.all().order_by('?')[:1]
#        return render(request, 'test.html', {"survey":survey})        
#
#def next(request):
#    pass






def startapp(request):
    
    if request.method == 'POST':

        form = ExtendedUserCreationForm(request.POST)
        profile_form = UserProfil(request.POST)

        if form.is_valid() and profile_form.is_valid():
            user = form.save()

            profile = profile_form.save(commit=False)
            profile.user = user   

            profile.save()
            email = form.cleaned_data.get('email')
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=password)
            login(request, user)
            

            return redirect('/login')
    else:
        form = ExtendedUserCreationForm()
        profile_form = UserProfil()
    context = {'form': form, 'profile_form': profile_form}
    return render(request, 'registeration.html', context)

def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            return profile(request)

    else:
        form = AuthenticationForm()
    context = { 'form': form}
    return render(request, 'login.html', context)




@login_required    
def profile(request, *args, **kwargs):    
    if request.method == 'POST':

        form = OtvetForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.user = request.user
            post.save()
            
            form = OtvetForm()
            
    else:
        form = OtvetForm()
    context = {'form': form,
                'stimuls':OtvetForm().fields }
    return render(request, 'home.html', context)
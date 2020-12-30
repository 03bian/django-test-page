from django.shortcuts import render
from .forms import UserBasicInfoForm, UserAdditionalInfoForm
from django.contrib.auth import authenticate,login,logout
from django.http import HttpResponseRedirect,HttpResponse
from django.urls import reverse
from django.contrib.auth.decorators import login_required


def main(request):
    return render(request,'shopApp/main_page.html')

@login_required()
def shop_creator(request):
    return render(request,'shopApp/shop_creator_page.html')




@login_required()
def user_logout(request):
    logout(request)
    return HttpResponseRedirect(reverse('main'))



def register(request):
    registered=False
    if request.method=="POST":
        userbasicinfo_form = UserBasicInfoForm(data=request.POST)
        useradditionalinfo_form = UserAdditionalInfoForm(data=request.POST)

        if userbasicinfo_form.is_valid() and useradditionalinfo_form.is_valid():

            user_basic=userbasicinfo_form.save()
            user_basic.set_password(user_basic.password)
            user_basic.save()

            user_extended = useradditionalinfo_form.save(commit=False)
            user_extended.user=user_basic

            if 'profile_pic' in request.FILES:
                user_extended.profile_pic=request.FILES['profile_pic']

            user_extended.save()

            registered=True
        
        else:
            print(userbasicinfo_form.errors, useradditionalinfo_form.errors)
    else:
        userbasicinfo_form = UserBasicInfoForm()
        useradditionalinfo_form = UserAdditionalInfoForm()
    
    return render(request, 'shopApp/register_page.html', {'userbasicinfo_form': userbasicinfo_form, 'registered': registered, 'useradditionalinfo_form': useradditionalinfo_form})



def user_login(request):
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(username=username, password=password)

        if user:
            if user.is_active:
                login(request,user)
                return HttpResponseRedirect(reverse('main'))

            else:
                return HttpResponse("You're account is not active")

        else:
            print("Sb tried to login and failed!")
            print("Username: {} Password {}   was used".format(username, password))
            return HttpResponse("invalid login!")
    else:
        return render(request, 'shopApp/login_page.html', {})



            


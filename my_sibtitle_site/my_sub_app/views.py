from django.shortcuts import render,redirect
from my_sub_app.forms import Sign_up
from django.core.mail import send_mail
import random
from django import forms
# Create your views here.

def home(request):
    return render(request,"my_sub_app/home.html")

def categories(request):
    return render(request,'my_sub_app/categories.html')

def english(request):
    return render(request,'my_sub_app/cat_eng.html')

def hindi(request):
    return render(request,'my_sub_app/cat_hin.html')

def punjabi(request):
    return render(request,'my_sub_app/cat_pun.html')

def comedy(request):
    return render(request,'my_sub_app/cat_com.html')

def sci_fi(request):
    return render(request,'my_sub_app/cat_sci-fi.html')

def adventure(request):
    return render(request,'my_sub_app/cat_adv.html')

def signup_thanks(request):
    return render(request,'my_sub_app/signup_thanks.html')

def signup(request):
    form=Sign_up()

    if request.method=="POST":
        form=Sign_up(request.POST)
        if form.is_valid():
            # print(form.cleaned_data['name'])
            rec_mail=(form.cleaned_data['email'])
            form.save()
            print(rec_mail)
            send_mail("Thanks for Registering","You are successfully registered.Welcome to the family.\nGreetings\nVarun Saini\nWeb Developer",'imvarun23@gmail.com',[rec_mail,],fail_silently=True)
            return redirect(signup_thanks)
        # else:
        #     raise forms.ValidationError("incorrect filed form")
    return render(request,'my_sub_app/signup.html',{"form":form})



# def signup(request):
#     form=Sign_up()
#     a=random.randint(10000,99999)
#     if request.method=="POST":
#         form=Sign_up(request.POST)
#         if form.is_valid():
#             # print(form.cleaned_data['name'])
#             rec_mail=(form.cleaned_data['email'])
#             redirect(signupotp)
#             form.save()
#             print(rec_mail)
#             send_mail("Thanks for Registering","Your OTP for Completing registering Signup process is : %d.Welcome to the family.\nGreetings\nVarun Saini\nWeb Developer"%a,'imvarun23@gmail.com',[rec_mail,],fail_silently=False)
#             return redirect(signup_thanks)
#         # else:
#         #     raise forms.ValidationError("incorrect filed form")
#     return render(request,'my_sub_app/signup.html',{"form":form})

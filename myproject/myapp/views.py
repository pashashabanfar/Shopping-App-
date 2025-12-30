from django.shortcuts import render, redirect
from django.http import HttpResponse
import datetime
from django.contrib.auth.models import User
from django.contrib.auth import login
from .forms import SignupForm, ProfileForm
from myapp.models import Employee
from . import forms
from django.contrib.auth.decorators import login_required
from myapp.models import Profile

# Create your views here.
@login_required
def electronics(request):
    elec_products = {
        "Product1": "Mac",
        "Product2": "iPhone",
        "Product3": "Dell"
    }
    return render(request, 'templatesApp/ShoppingApp/product.html', context=elec_products)

@login_required
def toys(request):
    toy_products = {
        "Product1": "Remote Car",
        "Product2": "Helicopter",
        "Product3": "Gun"
    }
    return render(request, 'templatesApp/ShoppingApp/product.html', context=toy_products)

@login_required
def shoes(request):
    shoe_products = {
        "Product1": "Nike",
        "Product2": "Adidas",
        "Product3": "Eco"
    }
    return render(request, 'templatesApp/ShoppingApp/product.html', context=shoe_products)

@login_required
def index(request):
    return render(request, 'templatesApp/ShoppingApp/index.html')

@login_required
def displayEmployee(request):
    employees = Employee.objects.all()
    empDict = {"employee": employees}
    return render(request, 'templatesApp/Employee/EmployeeTemp.html', empDict)

@login_required
def insertEmployee(request):
    if request.method == "POST":
        first_name = request.POST.get("firstName")
        last_name = request.POST.get("lastName")
        salary = request.POST.get("salary")
        email = request.POST.get("email")


        Employee.objects.create(
            firstName = first_name,
            lastName = last_name,
            salary = salary,
            email = email
        )
        return redirect('displayEmployee')
    return render(request, 'templatesApp/Employee/insertEmployeeTemp.html')

@login_required
def updateEmployee(request, id):
    target_customer = Employee.objects.get(id=id)
    if request.method == 'POST':
        target_customer.firstName = request.POST.get("firstName")
        target_customer.lastName = request.POST.get("lastName")
        target_customer.salary = request.POST.get("salary")
        target_customer.email = request.POST.get("email")

        target_customer.save()
        return redirect('displayEmployee')

    return render(
        request,
        'templatesApp/Employee/updateEmployee.html',
        {'employee': target_customer}
    )


@login_required
def deleteEmployee(request, id):
    target_customer = Employee.objects.get(id = id)
    if request.method == 'POST':
        target_customer.delete()
        return redirect('displayEmployee')
    return render(request, 'templatesApp/Employee/deleteEmployee.html', {'employee': target_customer})


@login_required
def userRegistrationForm(request):
    form = forms.UserRegistrationForm
    if request.method == 'POST':
        userInfo = forms.UserRegistrationForm(request.POST)
        if userInfo.is_valid():
            print("First Name: ", userInfo.cleaned_data['firstName'])
    return render(request, 'templatesApp/Form/userRegistration.html', {'form': form})

def signup_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        age = request.POST['age']
        gender = request.POST['gender']

        user = User.objects.create_user(
            username = username,
            password = password,
            first_name = first_name,
            last_name = last_name,

        )
        Profile.objects.create(
            name=user,
            gender=gender,
            age=age
        )
        return redirect("login")

    return render(request, "registration/signup.html")
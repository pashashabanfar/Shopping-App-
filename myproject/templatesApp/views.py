from django.shortcuts import render

# Create your views here.
def renderTemplate(request):
    info = {"name":"Pasha"}
    return render(request, 'templatesApp/firstTemplate.html', context=info)

def renderInformation(request):
    info = {"id": "1", "name":"Pasha", "country": "Canada"}
    return render(request, 'templatesApp/EmployeeTemp.html', context=info)
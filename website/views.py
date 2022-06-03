from django.shortcuts import render, redirect
from website.models import Employees, LegalServices, Clients
from website.forms import ConsultationsForm
from django.http import HttpResponse


def test_page(request):
    return render(request, 'test.html')


def home_page(request):
    context = {'service': LegalServices.objects.all()}
    return render(request, 'home.html', context)


def about_page(request):
    context = {
        'employees': Employees.objects.all(),
        'about_options': {'ЗА НАС': 'LogoAbout', 'СФЕРИ НА ДЕЙНОСТ': 'AriasHeder', 'ЕКИП': 'TeamHeder'},
    }
    return render(request, 'about.html', context)


def clients_page(request):
    return render(request, 'clients.html')


def contacts_page(request):
    return render(request, 'contacts.html')


def consultation_page(request):
    if request.method == "POST":
        if ConsultationsForm(request.POST, request.FILES).is_valid():
            ConsultationsForm(request.POST, request.FILES).save()
            # return redirect('home')
    # GET
    context = {
        'consultations_form': ConsultationsForm(),
    }
    return render(request, 'consultation.html', context)
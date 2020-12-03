from django.contrib import messages
from django.shortcuts import render, redirect
from django.views.generic import TemplateView
from django.views.generic.edit import FormView
from roads.forms import CitizenAppealForm
# Create your views here.


def index(request):
    return render(request, "../templates/home.html")


def citizen(request):
    form = CitizenAppealForm(request.POST or None)
    if request.method == 'POST':
        if form.is_valid():
            form.FIO = form.cleaned_data['FIO']
            form.organisation = form.cleaned_data['organisation']
            form.address = form.cleaned_data['address']
            form.email = form.cleaned_data['email']
            form.text = form.cleaned_data['text']
            form.save()
            messages.success(request, f'Информация была обновлена')
            return redirect('home')
    return render(request, "../templates/citizen.html", {'form': form})

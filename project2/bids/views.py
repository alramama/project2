from django.shortcuts import render

from django.views import View
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from .models import Bid

class FilmBaseView(View):
    model = Bid
    fields = '__all__'
    success_url = reverse_lazy('bids:all')

class FilmListView(FilmBaseView, ListView):
    """View to list all bids.
    Use the 'film_list' variable in the template
    to access all Film objects"""

class FilmDetailView(FilmBaseView, DetailView):
    """View to list the details from one film.
    Use the 'film' variable in the template to access
    the specific film here and in the Views below"""

class FilmCreateView(FilmBaseView, CreateView):
    """View to create a new film"""

class FilmUpdateView(FilmBaseView, UpdateView):
    """View to update a film"""

class FilmDeleteView(FilmBaseView, DeleteView):
    """View to delete a film"""
from django.http import FileResponse

def index1(request):
    if request.method=='POST':
        upload1 = request.FILES['Bid']
        object = Bid.objects.create(upload=upload1)
        object.save()
    context = Bid.objects.all()
    return render(request,'bid_list.html',{'context':context})

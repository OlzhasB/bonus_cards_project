from django.shortcuts import render, redirect
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.core.paginator import Paginator
from django.urls import reverse_lazy
from django.contrib import messages
from django.contrib.messages.views import SuccessMessageMixin
from search_views.filters import BaseFilter
from django.contrib.auth.mixins import LoginRequiredMixin
from search_views.views import SearchListView
from .models import Card
from .forms import CardForm, CardSearchForm, CardGenerateForm
from datetime import datetime
from dateutil.relativedelta import relativedelta
from random import randint

def home(request):
    cards = Card.objects.all()
    paginator = Paginator(cards, 5)
    page = request.GET.get('page')
    cards = paginator.get_page(page)
    return render(request, 'cards_model/home.html', {'object_list': cards})


class CardDetailView(DetailView):
    queryset = Card.objects.all()
    context_object_name = 'object'
    template_name = 'cards_model/detail.html'


class CardCreateView(SuccessMessageMixin, LoginRequiredMixin, CreateView):
    model = Card
    form_class = CardForm
    template_name = 'cards_model/create.html'
    success_url = reverse_lazy('card:home')
    login_url = '/login'
    success_message = 'Card created succesfully!'


class CardUpdateView(SuccessMessageMixin, LoginRequiredMixin, UpdateView):
    model = Card
    template_name = 'cards_model/update.html'
    fields = ['active']
    success_url = reverse_lazy('card:home')
    login_url = '/login'
    success_message = ('Card updated successfully!')


class CardDeleteView(LoginRequiredMixin, DeleteView):
    model = Card
    success_url = reverse_lazy('card:home')
    login_url = '/login'
    def get(self, request, *args, **kwargs):
        messages.success(request, 'Card deleted succesfully!')
        return self.post(request, *args, **kwargs)


class CardFilter(BaseFilter):
    search_fields = {
        'number' : { 'operator' : '__exact', 'fields' : ['number'] },
        'series' : { 'operator' : '__exact', 'fields' : ['series'] },
        'active' : { 'operator' : '__exact', 'fields' : ['active'] },
    }

class CardSearchList(SearchListView):
    model = Card
    template_name = "cards_model/search.html"
    context_object_name = 'objects_list'
    form_class = CardSearchForm
    filter_class = CardFilter



def generate(request):
    form = CardGenerateForm()
    return render(request, 'cards_model/generate.html', {'form': form})



def generateCards(request):

    series = request.POST.get('series')


    amount = request.POST.get('amount')


    period = request.POST.get('period')


    for i in range(int(amount)):
        Card.objects.create(dateOfExpiration=datetime.now() + relativedelta(months=int(period)), totalSum=0, active=1,
                                   number=generateCardNumber(), series=series)

    response = redirect('/cards/')
    return response


def generateCardNumber():
    result = ''
    for i in range(8):
        if i == 0:
            result += str(randint(1, 9))
        else:
            result += str(randint(0, 9))
        if i == 3:
            result += ' '
    return result
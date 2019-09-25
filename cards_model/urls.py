from django.urls import path
from .views import home, CardDetailView, CardCreateView, CardDeleteView, CardSearchList, generate, generateCards, deactivateCard, activateCard

urlpatterns = [
    path('', home, name='home'),
    path('add/', CardCreateView.as_view(), name='add'),
    path('detail/<int:pk>/', CardDetailView.as_view(), name='detail'),
    path('delete/<int:pk>/', CardDeleteView.as_view(), name='delete'),
    path('search/', CardSearchList.as_view(), name='search'),
    path('generate/', generate, name='generate'),
    path('generateCards/', generateCards, name='generateCards'),
    path('activateCard/<int:pk>/', activateCard, name='activateCard'),
    path('deactivateCard/<int:pk>/', deactivateCard, name='deactivateCard'),
    # path('generate/', )
]
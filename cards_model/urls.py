from django.urls import path
from .views import home, CardDetailView, CardCreateView, CardUpdateView, CardDeleteView, CardSearchList, generate, generateCards

urlpatterns = [
    path('', home, name='home'),
    path('add/', CardCreateView.as_view(), name='add'),
    path('detail/<int:pk>/', CardDetailView.as_view(), name='detail'),
    path('update/<int:pk>/', CardUpdateView.as_view(), name='update'),
    path('delete/<int:pk>/', CardDeleteView.as_view(), name='delete'),
    path('search/', CardSearchList.as_view(), name='search'),
    path('generate/', generate, name='generate'),
    path('generateCards/', generateCards, name='generateCards'),
    # path('generate/', )
]
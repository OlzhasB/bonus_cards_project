from django.contrib import admin
from django.urls import path, include
from .views import home_view, login_view, logout_view



urlpatterns = [
    path('admin/', admin.site.urls),
    path('login/', login_view, name='login'),
    path('logout/', logout_view, name='logout'),
    path('cards/', include(('cards_model.urls', 'card'))),
    path('', home_view, name='home'),
]

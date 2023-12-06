from django.urls import path
from .views import index, about, contactsView

urlpatterns = [
    path('', index, name='home'),
    path('about/', about, name='about'),
    path('contacts/', contactsView, name='contacts'),
    # path('login/', login, name='login')
]
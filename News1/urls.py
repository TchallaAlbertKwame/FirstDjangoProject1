from django.urls import path
from .views import Newsp, Home, Contact, NewsDate,Register,addUser,modelform

urlpatterns = [
    path('', Home, name='Home'),
    path('News/', Newsp, name='News'),
    path('newsdate/<int:year>', NewsDate, name='newsdate'),
    path('Contact/', Contact, name='Contact'),
    path('Register/', Register, name='Register'),
    path('addUser/', addUser, name='addUser'),
    path('modalform/', modelform, name='form'),

]

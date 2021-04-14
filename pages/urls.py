
from django.urls import path
from pages import views
urlpatterns = [
    path('',views.Home,name='home'),
    path('About/',views.About,name='about'),
    path('services/',views.services,name='services'),
    path('contact/',views.contact,name='contact'),
]

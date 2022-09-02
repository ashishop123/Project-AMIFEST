from django.contrib import admin
from django.urls import path
from FEST import views

urlpatterns = [
    path('admin/', admin.site.urls),

    path('',views.home,name='home'),

    path('contact', views.contact, name='contact'),

    path('about', views.about, name='about'),

    path('upcoming', views.upcoming, name='upcoming'),

    path('happening', views.happening, name='happening'),

    path('popular', views.popular, name='popular'),

    path('register', views.register, name='register' )

    
]
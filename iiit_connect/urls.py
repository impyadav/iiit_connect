from django.conf.urls import url
from . import views

urlpatterns = [
    
    # url(r'^simpleemail/(?P<emailto>[\w.%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,4})/',views.sendSimpleEmail, name = 'sendSimpleEmail')
     url(r'^massemail/(?P<emailto1>[\w.%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,4})/(?P<emailto2>[\w.%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,4})',views.sendMassEmail, name = 'sendMassEmail')
]
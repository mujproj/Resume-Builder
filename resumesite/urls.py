from django.urls import path
from resumesite import views
from .views import *

urlpatterns = [
    path('', views.home, name='home'),
    path('resume', views.resume, name='resume'),
]

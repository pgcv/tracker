from django.conf.urls import url
from django.urls import path
from . import views 


urlpatterns = [
    url('signup', views.signup, name='su'),
    url('signup_form_submission', views.signup_form_submission, name='signup_form_submission')
]


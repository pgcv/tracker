from django.conf.urls import include, url
from django.contrib import admin
from django.urls import path
from input import views as input_views
from django.contrib.auth.views import LoginView
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('admin/', admin.site.urls),
    url('index/', input_views.index,name='index'),
    url('signup/', input_views.signup,name='signup'),
    url('signup_form_submission', input_views.signup_form_submission, name='signup_form_submission'),
    url('signin', input_views.signin, name='signin'),
    url('upload/',input_views.upload,name='upload'),
    url('uploadprofile/',input_views.uploadprofile,name='uploadprofile'),
    url('signout', input_views.signout, name='signout'),


    
]

if settings.DEBUG:
	urlpatterns+=static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
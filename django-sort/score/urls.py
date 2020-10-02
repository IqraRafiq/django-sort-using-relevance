from django.urls import include, path
from django.contrib.auth.decorators import login_required
from . import views

urlpatterns = [
    path('',views.index,name="home"),
    path('sign_up/',views.SignUpView.as_view(),name="signup")
]
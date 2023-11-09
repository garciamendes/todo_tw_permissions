# Django
from django.urls import path

# Third party
from dj_rest_auth.views import LoginView
from dj_rest_auth.views import LogoutView

urlpatterns = [
    path('login', LoginView.as_view(), name='login'),
    path('logout', LogoutView.as_view(), name='logout')
]

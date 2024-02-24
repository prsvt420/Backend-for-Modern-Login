from django.urls import path

from users.services import LogoutService
from users.views import AuthFacade

app_name = 'users'

urlpatterns = [
    path('login/', AuthFacade().login_or_register_user, name='login-register'),
    path('logout/', LogoutService.as_view(), name='logout'),
]

from django.conf.urls import url
from django.contrib.auth.views import LoginView, LogoutView

from .views import home

urlpatterns = [
    url(r'home$', home, name="employee_home"),
    url(r'login$',
        LoginView.as_view(template_name="employee/login_form.html"),
        name="employee_login"),
    url(r'logout$',
        LogoutView.as_view(),
        name="employee_logout"),
]

from django.contrib.auth.views import LoginView
from django.contrib import messages
from .forms import CustomLoginForm

class CustomLoginView(LoginView):
    form_class = CustomLoginForm
    template_name = 'login.html'
    redirect_authenticated_user = True
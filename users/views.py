from django.contrib.auth.views import LoginView
from django.contrib import messages
from .forms import CustomLoginForm

class CustomLoginView(LoginView):
    form_class = CustomLoginForm
    template_name = 'login.html'

    def form_invalid(self, form):
        messages.error(self.request, "Usuario o contraseña incorrectos.")
        return super().form_invalid(form)
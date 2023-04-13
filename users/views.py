from django.shortcuts import render

# Create your views here.

# new to create my account page
from django.contrib.auth import get_user_model
from django.views.generic import UpdateView

# new to redirect to my account page after changed password
from django.urls import reverse_lazy
from allauth.account.views import PasswordChangeView

from .forms import CustomUserChangeForm

class MyAccountPageView(UpdateView):
    model = get_user_model()
    form_class = CustomUserChangeForm
    template_name = 'account/my_account.html'

    def get_object(self):
        return self.request.user


# new to redirect to my account page after changed password
class CustomPasswordChangeView(PasswordChangeView):
    success_url = reverse_lazy('my-account')

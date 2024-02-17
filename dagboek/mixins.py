from django.contrib.auth import get_user_model
from django.shortcuts import redirect
from django.urls import reverse

class CustomLoginRequiredMixin:
    def dispatch(self, request, *args, **kwargs):
        request.session['next'] = self.request.path
        if not request.user.is_authenticated:
            return redirect(reverse('user:login'))
        return super().dispatch(request, *args, **kwargs)
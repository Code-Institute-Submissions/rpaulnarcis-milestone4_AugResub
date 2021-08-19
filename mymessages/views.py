from django.shortcuts import redirect
from django.views.generic import ListView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse
from .models import Message



class ChatView(LoginRequiredMixin, ListView):
    def get_queryset(self):
        queryset = Message.objects.filter(user=self.request.user)
        return queryset

    def post(self, request, *args, **kwargs):
        text = request.POST.get("text")

        if text:
            Message.objects.create(user=request.user, text=text)
        return redirect(reverse('chat'))

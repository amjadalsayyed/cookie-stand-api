from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import ListView, DetailView, UpdateView, CreateView, DeleteView
from django.urls import reverse_lazy
from .models import Cookie_Stand


class Cookie_StandListView(LoginRequiredMixin, ListView):
    template_name = "cookie_stand/cookie_stand_list.html"
    model = Cookie_Stand
    context_object_name = "cookie_stand"


class Cookie_StandDetailView(LoginRequiredMixin, DetailView):
    template_name = "cookie_stand/cookie_stand_detail.html"
    model = Cookie_Stand


class Cookie_StandUpdateView(LoginRequiredMixin, UpdateView):
    template_name = "cookie_stand/cookie_stand_update.html"
    model = Cookie_Stand
    fields = "__all__"


class Cookie_StandCreateView(LoginRequiredMixin, CreateView):
    template_name = "cookie_stand/cookie_stand_create.html"
    model = Cookie_Stand
    fields = "__all__" # "__all__" for all of them


class Cookie_StandDeleteView(LoginRequiredMixin, DeleteView):
    template_name = "cookie_stand/cookie_stand_delete.html"
    model = Cookie_Stand
    success_url = reverse_lazy("cookie_stand_list")

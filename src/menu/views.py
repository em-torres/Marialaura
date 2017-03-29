from django.core.exceptions import ImproperlyConfigured
from django.contrib import messages
from django.http import Http404
from django.views.generic.detail import DetailView
from django.views.generic.list import ListView
from django.shortcuts import render, get_object_or_404, redirect
from django.utils import timezone

from .models import Menu, MenuWeek


class MenuListView(ListView):
    model = Menu
    ordering = 'menu_week'

    def get_context_data(self,*args, **kwargs):
        context = super(MenuListView, self).get_context_data(*args,**kwargs)
        context['today'] = timezone.now().date()
        return context

class MenuDetailView(DetailView):
    model = Menu

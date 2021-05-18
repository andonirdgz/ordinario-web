from django.shortcuts import render, get_object_or_404, get_list_or_404
from .models import Hobby
from .forms import HobbyForm
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy


class HobbiesListView(ListView):
    model = Hobby


class HobbyCreateView(CreateView):
    model = Hobby
    form_class = HobbyForm
    success_url = reverse_lazy('hobbies:hobbies')


class HobbyUpdateView(UpdateView):
    model = Hobby
    form_class = HobbyForm
    template_name_suffix = "_update_form"

    def get_success_url(self):
        return reverse_lazy('hobbies:update', args=[self.object.id]) + '?ok'


class HobbyDeleteView(DeleteView):
    model = Hobby
    template_name_suffix = "_confirm_delete"
    success_url = reverse_lazy('hobbies:hobbies')

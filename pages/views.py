from django.urls import reverse_lazy
from django.http  import request
from django.contrib import messages
from django.contrib.messages.views import SuccessMessageMixin
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView

from dagboek.mixins import CustomLoginRequiredMixin

from .models import *

class EntryListView(CustomLoginRequiredMixin, ListView):
  model = Entry

  def get_queryset(self, **kwargs):
    queryset = super(EntryListView, self).get_queryset()
    queryset = Entry.objects.filter(author=self.request.user.id) #.order_by("-entry_date")
    return queryset

class EntryDetailView(DetailView):
  model = Entry

class EntryCreateView(SuccessMessageMixin, CreateView):
  model = Entry
  fields = ["title", "content", "tags"]

  success_message = "Created"
  success_url = reverse_lazy("entry_list")

class EntryUpdateView(SuccessMessageMixin, UpdateView):
  model = Entry
  fields = ["title", "content", "tags"]

  success_message = "Updated"
  def get_success_url(self):
      return reverse_lazy(
          "entry_detail",
          kwargs={"pk": self.entry.id}
      )

class EntryDeleteView(SuccessMessageMixin, DeleteView):
  model = Entry

  success_message = "Goodbye"
  success_url = reverse_lazy("entry_list")

  def delete(self, request, *args, **kwargs):
    messages.success(self.request, self.success_message)
    return super().delete(request, *args, **kwargs)
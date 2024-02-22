from django.urls import reverse_lazy
from django.http import request
from django.shortcuts import redirect
from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.messages.views import SuccessMessageMixin
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView

from .models import *
from .forms import EntryForm

class EntryListView(LoginRequiredMixin, ListView):
  model = Entry

  def get_queryset(self, **kwargs):
    queryset = super(EntryListView, self).get_queryset()
    queryset = Entry.objects.filter(author=self.request.user.id) #.order_by("-entry_date")
    return queryset

class EntryDetailView(LoginRequiredMixin, DetailView):
  model = Entry

class EntryCreateView(LoginRequiredMixin, SuccessMessageMixin, CreateView):
  model = Entry
  form_class = EntryForm

  success_message = "Created"

  def post(self, request, *args, **kwargs):
    print(request.POST)

    form = self.form_class(request.POST)
    # data = request.POST
    if form.is_valid():
        title = form.cleaned_data.get('title')
        content = form.cleaned_data.get('content')
        tags = form.cleaned_data.get('tags')
        entry = Entry.objects.create(title = title, content = content, tags = tags, author = request.user)
        entry.save()

        return redirect(
          'diary:entry_detail',
          pk = entry.id
        )
    else:
      return render(request, 'diary:entry_list', {form: form})


class EntryUpdateView(LoginRequiredMixin, SuccessMessageMixin, UpdateView):
  model = Entry
  form_class = EntryForm
  success_message = "Updated"
  
  def get_success_url(self):
      return reverse_lazy(
          "entry_detail",
          kwargs={"pk": self.entry.id}
      )

class EntryDeleteView(LoginRequiredMixin, SuccessMessageMixin, DeleteView):
  model = Entry

  success_message = "Goodbye"
  success_url = reverse_lazy("entry_list")

  def delete(self, request, *args, **kwargs):
    messages.success(self.request, self.success_message)
    return super().delete(request, *args, **kwargs)
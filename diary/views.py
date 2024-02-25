from django.urls import reverse_lazy
from django.http import request
from django.contrib import messages
from django.core.paginator import Paginator
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.messages.views import SuccessMessageMixin
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView

from .models import *
from .forms import EntryForm

class EntryListView(LoginRequiredMixin, ListView):
  model=Entry

  def get(self, request, *args, **kwargs):
    entries=Entry.objects.filter(author=self.request.user.id)

    paginator=Paginator(entries,10)
    page=request.GET.get('page',1)

    new_page=paginator.get_page(page)
    return render(request, 'diary/entry_list.html', {'entries': new_page})

class EntryDetailView(LoginRequiredMixin, DetailView):
  model=Entry

  def get(self, request, *args, **kwargs):
    pk=self.kwargs.get('pk')

    if pk:
      entry=get_object_or_404(Entry, author=self.request.user, pk=pk)

      # after 404
      next_entry=Entry.objects.filter(author=self.request.user, id__gt=entry.id).order_by('id').first()
      if next_entry:
        next_entry=next_entry.id

      previous_entry=Entry.objects.filter(author=self.request.user, id__lt=entry.id).order_by('-id').first()
      if previous_entry:
        previous_entry=previous_entry.id

      return render(request, 'diary/entry_detail.html', { 'entry': entry, 'previous': previous_entry, 'next': next_entry })

class EntryCreateView(LoginRequiredMixin, SuccessMessageMixin, CreateView):
  model=Entry
  form_class=EntryForm

  success_message="Created"

  def post(self, request, *args, **kwargs):

    form=self.form_class(request.POST)
    # data=request.POST
    if form.is_valid():
        title=form.cleaned_data.get('title')
        content=form.cleaned_data.get('content')
        tags=form.cleaned_data.get('tags')
        entry=Entry.objects.create(title=title, content=content, tags=tags, author=self.request.user)
        entry.save()

        return redirect(
          'diary:entry_detail',
          pk=entry.id
        )
    else:
      return render(request, 'diary:entry_create', {form: form})

class EntryUpdateView(LoginRequiredMixin, SuccessMessageMixin, UpdateView):
  model=Entry
  form_class=EntryForm
  success_message="Updated"

  def post(self, request, *args, **kwargs):
    pk=self.kwargs.get('pk')
    form=self.form_class(request.POST)

    if pk:
      entry=get_object_or_404(Entry, author=self.request.user, pk=pk)
      
    # data=request.POST
    if entry and form.is_valid():
        title=form.cleaned_data.get('title')
        content=form.cleaned_data.get('content')
        tags=form.cleaned_data.get('tags')

        entry.title=title
        entry.content=content
        # clear previous tags
        entry.tags.clear()
        entry.tags.add(*tags)
        entry.update_date=datetime.datetime.now()
        entry.save()
 
        return redirect(
          'diary:entry_detail',
          pk=entry.id
        )
    else:
      return render(request, 'diary:entry_list', {form: form})

  def get(self, request, *args, **kwargs):
    pk=self.kwargs.get('pk')

    if pk:
      entry=get_object_or_404(Entry, author=self.request.user, pk=pk)
      return render(request, 'diary/entry_form.html', { 'entry': entry })

  def get_success_url(self):
      return reverse_lazy(
          'diary:entry_detail',
          kwargs={"pk": self.entry.id}
      )

class EntryDeleteView(LoginRequiredMixin, SuccessMessageMixin, DeleteView):
  model=Entry

  success_message="Goodbye"
  success_url=reverse_lazy("diary:entry_list")

  def get(self, request, *args, **kwargs):
    pk=self.kwargs.get('pk')

    if pk:
      entry=get_object_or_404(Entry, author=self.request.user, pk=pk)
      return render(request, 'diary/entry_confirm_delete.html', {'entry': entry })

  def delete(self, request, *args, **kwargs):
    pk=self.kwargs.get('pk')

    if pk:
      entry=get_object_or_404(Entry, author=self.request.user, pk=pk)
      messages.success(self.request, self.success_message)
      return super().delete(request, *args, **kwargs)
from django.shortcuts import render
from django.views.generic import TemplateView, ListView, DetailView, CreateView, UpdateView, DeleteView
from dromdeals import models
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required
from dromdeals import forms
from django.urls import reverse_lazy


# Create your views here.

# About page view
class AboutView(TemplateView):
    template_name = "about.html"

# Product page list
class ProductListView(ListView):
    model = models.PostProduct

    def get_queryset(self):
        return models.PostProduct.objects.all()
    

# Product detail view
class ProductDetailView(DetailView):
    model = models.PostProduct


# Create Product view
class CreateProductView(LoginRequiredMixin, CreateView):
    login_url = '/login/'
    redirect_field_name = 'dromdeals/post_detail.html' 

    form_class = forms.PostProduct

    model = models.PostProduct



# Update product view
class ProductUpdateView(UpdateView):
    login_url = '/login/'
    redirect_field_name = 'dromdeals/post_detail.html' 

    form_class = forms.PostProduct

    model = models.PostProduct


# Product delete view
class ProductDeleteView(LoginRequiredMixin, DeleteView):
    model = models.PostProduct
    success_url = reverse_lazy('post_list')
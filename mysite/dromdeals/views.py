from django.shortcuts import render
from django.utils import timezone
from django.views.generic import TemplateView, ListView, DetailView, CreateView, UpdateView, DeleteView
from dromdeals import models
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required
from dromdeals import forms
from django.urls import reverse_lazy
from django.shortcuts import redirect, get_object_or_404, render


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


# Draft list view
class DraftListView(LoginRequiredMixin, ListView):
    login_url = '/login/'
    redirect_field_name = 'dromdeals/post_list.html'



############################### PRODUCT COMMENTS #######################################

@login_required
def post_publish(request, pk):
    post = get_object_or_404(models.PostProduct, pk=pk)
    post.publish
    return redirect('post_detail' ,pk=pk)


@login_required
def add_comments_to_product_post(request, pk):

    post = get_object_or_404(models.PostProduct, pk=pk)

    if request.method =="POST":
        form = CommentForm(request.POST)

        if form.is_valid():
            comment = form.save(commit=False)
            comment.post = post
            comment.save()
            return redirect('post_detail', pk=post.pk)
    else:
        form = CommentForm()

    return (request, 'dromdeals/comment_from.html', {'form': form})


@login_required
def comment_approve(request, pk):
    comment = get_object_or_404(Comment, pk=pk)
    comment.approve()
    return redirect('post_detail', pk = comment.post.pk)


@login_required
def comment_remove(request,pk):
    comment = get_object_or_404(Comment, pk=pk)
    post_pk = comment.post.pk
    comment.delete()
    return redirect('post_detail', pk=post_pk)

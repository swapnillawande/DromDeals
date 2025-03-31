from django.contrib import admin
from django.urls import path
from dromdeals import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.ProductListView.as_view(), name="post_list"),
    path('about/', views.AboutView.as_view(), name="about_page"),
    path('post/<int:pk>/', views.ProductDetailView.as_view(), name='post_detail'),
    path('post/new/', views.CreateProductView.as_view(), name='post_new'),
    path('post/<int:pk>/edit/', views.ProductUpdateView.as_view(), name='post_edit')


]

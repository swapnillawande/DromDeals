from django.contrib import admin
from django.urls import path
from dromdeals import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.ProductListView.as_view(), name="post_list"),
    path('about/', views.AboutView.as_view(), name="about_page"),
    path('post/<int:pk>/', views.ProductDetailView.as_view(), name='post_detail'),
    path('post/new/', views.CreateProductView.as_view(), name='post_new'),
    path('post/<int:pk>/edit/', views.ProductUpdateView.as_view(), name='post_edit'),
    path('post/<int:pk>/remove/', views.ProductDeleteView.as_view(), name='post_remove'),
    path('post/<int:pk>/comments/', views.add_comments_to_product_post, name='add_comments_to_post'),
    path('comment/<int:pk>/approve/', views.comment_approve, name='comment_approve'),
    path('comment/<int:pk>/remove/', views.comment_remove, name='comment_remove'),
    path('post/<int:pk>/publish/', views.post_publish, name='post_publish'),



]

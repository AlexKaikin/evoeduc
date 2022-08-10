from django.urls import path

from apps.core import views

urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
    path('category/<slug:slug>/', views.CategoryView.as_view(), name='category'),
    path('post/<slug:slug>/', views.PostDetailView.as_view(), name='post'),
]

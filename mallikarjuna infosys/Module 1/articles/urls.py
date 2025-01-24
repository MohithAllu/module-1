from django.urls import path
from .views import CustomLoginView, edit_article, home
from articles import views

urlpatterns = [
    path('accounts/profile/', home, name='home'),
    path('accounts/profile/login/', CustomLoginView.as_view(), name='login'),
     path('accounts/profile/login/create/', views.create_article, name='create_article'),
    path('accounts/profile/login/edit/<int:article_id>/', views.edit_article, name='edit_article'),
    ]

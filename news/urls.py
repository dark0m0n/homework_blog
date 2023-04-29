from django.urls import path, include
from news import views

urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
    path('article/<int:pk>/', views.text, name='article'),
    path('createarticle/', views.AddArticle.as_view(), name='create_article'),
]

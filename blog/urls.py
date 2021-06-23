from django.urls import path
from . import views

urlpatterns = [
<<<<<<< HEAD
<<<<<<< HEAD
    path('', views.post_list, name='post_list'),
    path('post/<int:pk>/', views.post_detail, name='post_detail'),
    path('author/<username>/', views.author_perfil, name='author_perfil'),
<<<<<<< HEAD
    path('drafts/', views.post_draft_list, name='post_draft_list'),
=======
    path('', views.post_list, name='post_list')
>>>>>>> parent of b750a96 (Update URLs)
=======
    path('', views.post_list, name='post_list')
>>>>>>> parent of b750a96 (Update URLs)
=======
>>>>>>> parent of 390d1b9 (Rascunhos Blog)
]
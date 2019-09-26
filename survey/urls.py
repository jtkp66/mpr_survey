from django.urls import path
from .views import (
    PostCreateView,
    PostDetailView,
)
from . import views

urlpatterns = [
    path('', views.index, name='survey-home'),
    path('survey-new2', views.post_new, name='survey-new2'),
    path('<int:post_id>', views.post, name='survey2'),
    path('new', PostCreateView.as_view(), name='post-create'),
    # path('new2/', views.post_new, name='post_new'),
    path('<int:pk>/', PostDetailView.as_view(), name='post_detail'),
    path('<int:pk>/edit/', views.post_edit, name='post_edit'),
]

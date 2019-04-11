from django.urls import path

from . import views

urlpatterns = [
    path('', views.ClosetListView.as_view()),
    path('user_profile/', views.user_profile_list),
    path('user_profile/<int:pk>/', views.user_profile_detail),
]

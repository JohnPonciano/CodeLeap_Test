from django.urls import path
from .views import CareerListCreateView, CareerDetailView, RegisterView, LoginView

urlpatterns = [
    path('careers/', CareerListCreateView.as_view(), name='career-list-create'),
    path('careers/<int:pk>/', CareerDetailView.as_view(), name='career-detail'),
    path('register/', RegisterView.as_view(), name='api-register'),
    path('login/', LoginView.as_view(), name='api-login'),
]

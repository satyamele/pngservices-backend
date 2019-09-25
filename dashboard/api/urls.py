from django.urls import path

from .views import (
    CustomerListView,
    CustomerDetailView,
    CustomerCreateView,
    CustomerUpdateView,
    CustomerDeleteView
)
urlpatterns = [
path('', CustomerListView.as_view()),
    path('create/', CustomerCreateView.as_view()),
    path('<pk>', CustomerDetailView.as_view()),
    path('<pk>/update/', CustomerUpdateView.as_view()),
    path('<pk>/delete/', CustomerDeleteView.as_view())
]

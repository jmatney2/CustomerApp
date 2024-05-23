"""URLs for the Customers app"""

from django.urls import path

from . import views

urlpatterns = [
    path("", views.IndexView.as_view(), name="index"),
    path("add/", views.AddCustomerView.as_view(), name="add"),
]

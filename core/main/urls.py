from django.urls import path
from .views import HomeListView, AboutListView, ContactListView, ProductsListView

urlpatterns = [
    path('', HomeListView.as_view(), name='home'),
    path('about/', AboutListView.as_view(), name='about'),
    path('contact/', ContactListView.as_view(), name='contact'),
    path('products/', ProductsListView.as_view(), name='products'),
]
from django.urls import path
from .views import *


urlpatterns = [
  path('register', register, name="register"),
  path('my-login', my_login, name="my-login"),
  path('user-logout', user_logout, name="user-logout"),

  path('', dashboard, name='dashboard'),

  path('clients/', clients, name='clients'),
  path('client/<str:pk>/', client, name='client'), 


  path('invoices/', InvoicesListView.as_view(), name='invoices'),
  path('invoice/<str:pk>/', InvoiceDetailView.as_view(), name='invoice'),

  path('create/', createInvoice, name='createInvoice'),
  path('update_invoice/<str:pk>/', updateInvoice, name='updateInvoice'),
  path('delete_invoice/<str:pk>/', deleteInvoice, name='deleteInvoice'),


]

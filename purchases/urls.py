from django.urls import path
from .views import BuyTicketView, OrderListView
from ticketing.views import ListEventViews

urlpatterns = [
    path('events/', ListEventViews.as_view(), name='list-events'),
    path('purchase/', BuyTicketView.as_view(), name='buy-ticket'),
    path('orders/', OrderListView.as_view(), name='order-list'),
]


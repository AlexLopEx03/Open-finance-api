from django.urls import path

from .views import stock_view

urlpatterns = [
    path('<str:ticker>/', stock_view)
]
from django.urls import path
from . import views

urlpatterns = [
    path('', views.HomePageView.as_view(), name='home_page_url'),
    path('<int:id>/', views.ProductDatailView.as_view(), name='product_detail'),
    path('', views.CustomerCreateViev.as_view(), name='customer_create'),
    path('order_create/', views.OrderCreateView.as_view(), name='order_create'),
]

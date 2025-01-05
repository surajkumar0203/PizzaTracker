from django.urls import path
from myapp.views import index,order,order_pizza
urlpatterns = [
    path('',index,name="index"),
    path('<ordered_id>/',order,name="order_status"),
    path('order_pizza/<pizza_id>/',order_pizza,name="order_pizza")
]
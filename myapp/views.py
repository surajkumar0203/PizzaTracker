from django.shortcuts import render,redirect
from myapp.models import Pizza,Order
def index(request):
    pizzas=Pizza.objects.all()
    orders=Order.objects.all()
    return render(request, 'myapp/index.html',context={'pizzas':pizzas,'orders':orders})


def order(request,ordered_id):
    try:
        ordered_pizzas=Order.objects.get(order_id=ordered_id)
    except Order.DoesNotExist:
        return redirect("/")
    return render(request, 'myapp/order_status.html',context={'orders':ordered_pizzas})


def order_pizza(request,pizza_id):
    pizzas=Pizza.objects.get(id=pizza_id)
    Order.objects.create(pizza=pizzas,user=request.user,amount=pizzas.price)
    return redirect('/')
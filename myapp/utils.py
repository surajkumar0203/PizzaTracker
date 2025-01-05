from myapp.models import Order


def give_order_details(order_id):
    order_mapper={
        'Order Recieved':20,
        'Baking':40,
        'Baked':60,
        'Out of Delivery':80,
        'Order Deliverd':100
    }
    try:
        order = Order.objects.get(order_id=order_id)
        return {
            'order_id': order.order_id,
            'amount': order.amount,
            'status': order.status,
            'date':str(order.created_at),
            'progress_percentage': order_mapper[order.status]
        }
    except Order.DoesNotExist:
        return 'Order not found'
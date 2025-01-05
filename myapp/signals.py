from myapp.models import Pizza,Order
from django.dispatch import receiver
from django.db.models.signals import post_save
from channels.layers import get_channel_layer
from asgiref.sync import async_to_sync
from myapp.utils import give_order_details


@receiver(post_save, sender=Order)
def order_status_handler(sender,instance,created, **kwargs):
    if not created:
        channel_layer=get_channel_layer()
        data = give_order_details(instance.order_id)
        async_to_sync(channel_layer.group_send)(
            f'order_progress_{instance.order_id}',
            {
                'type':'order.status',
                'value':data
            }
        
        )
# yeni user oluşturulduğunda neler alabileceğini, onun tanımı yapılır
from django.dispatch import receiver
from django.db.models.signals import post_save
from django.contrib.auth import get_user_model
# get_user_model:aktif user modelini gösteriri
# setting.py>auth modelini temsil eder

from profiles.models import Profile

# user üzerinde kayıt yapıldıktan sonra(post_save)
# user fonk. tetiklenir
User= get_user_model()

@receiver(post_save, sender= User )
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        # instance: kaydedilen nesneyi temsil eder.
        Profile.objects.create(user= instance)

# veri şemalarının tanımlanacak kısmı

from django.db import models
from django.contrib.auth.models import AbstractUser 
# AbstractUser:özelleştirmek için tanımlanmış

# özelleşştirilmiş user modelini tanımlama
class CustomUser(AbstractUser):
    pass 

# customuser'i orj. bırakıp diğer işlemlerin burada yapılacağı kısım
class Profile(models.Model):
    user= models.OneToOneField(CustomUser, on_delete=models.CASCADE)
    # kullanıcılar arası takipleşme - modelin kendisini temsil eder
    # symmetrical :takipççi biirini tkp ettiği zaman takip ettiği kişiyi takip etmek zorunda değil!
    # related_name: profiledeki isim üzeirnden bağlı old profile erişimi sağlar. 
    followers= models.ManyToManyField('self', 
                                      through='FollowRelation',
                                      symmetrical=False,
                                      related_name='followings')
    
    def __str__(self):
        return f"{self.user.username} {self.pk}"

class FollowRelation(models.Model):
    follower= models.ForeignKey(Profile, on_delete=models.CASCADE,
                                related_name='followed_by')
    following= models.ForeignKey(Profile, on_delete=models.CASCADE,
                                 related_name='follows')
    #  otomatik olarak o anki tarihe eşitlesin
    created= models.DateTimeField(auto_now_add=True)

    class Meta:
        # followerfollowing ilişkisinin unique olamsını sağlar.
        # 1+ olmasını önler. (aynı takipçi- aynı kullanıcı için geçerli)
        unique_together= ('follower', 'following')

    def __str__(self):
        return f"{self.follower.user.username} follows {self.following.user.username}"




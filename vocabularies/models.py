from django.db import models
from profiles.models import Profile

"""kullanıcıların kendi sözlüklerini oluşturabildikleri,
sözcükelrin içersinde yeni kelimeleri ekleme
farklı kategorilerile atayabildikleri kısım
kullanıcılaın farklı kullanıcıların kullandığı kelimeleri görüp kendine ekleyebbilir"""

#kulalnıcıların sözcüklerini temsil eden model
# related_name: verilen isim profile üzerinden erişmeyi sağlar
class Vocabulary(models.Model):
    profile= models.ForeignKey(Profile, on_delete=models.CASCADE,
                               related_name="vocabularies")
    #kategori adını belirtir
    name= models.CharField(max_length=150)
    #blank desc. boş bırakılabilsin diye
    description= models.TextField(blank=True)

    #vocabulary kayıtlarının admin panelinde nasıl görüneceğini gösteren kısım
    def __str__(self):
        #önce isim, sonra kime ait
        return f"{self.name} ({self.profile.user.username})"
    
#kelimeleri temsil eden model
class Word(models.Model):
    #belirli voc.ait olmalı
    #ilişkilendirildiği tüm kelimeleri almak için related_name kullandık.
    vocabulary= models.ForeignKey(Vocabulary, on_delete=models.CASCADE,
                                  related_name='words')
    #kelimeleri tutmak için;
    text= models.CharField(max_length=150)
    #kendi dilimzideki anlamını tutmak için
    meaning= models.CharField(max_length=150)
    #textte verilen kelimenin örnek cümlede tutulması için;
    example_sentence= models.TextField()

    #worddek kayıtların adminde göstermek için
    def __str__(self):
        return self.text
    





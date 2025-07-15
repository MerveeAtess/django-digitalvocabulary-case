# 📘 Digital Vocabulary Case

Bu proje, kullanıcıların kendi İngilizce kelimelerini ekleyip tekrar edebileceği dijital bir sözlük uygulamasıdır. Django ve Django Rest Framework (DRF) ile geliştirilmiştir.

# 🎯 Projenin Amacı

Dil öğreniminde kişiselleştirilmiş kelime çalışmaları yapmak isteyen kullanıcılar için, hem bireysel hem de sosyal bir platform sunmayı amaçlar.

Kullanıcılar için:
* Kendi kelime ve anlamlarını sisteme kaydedebilir,
* Diğer kullanıcıların sözlüklerine göz atabilir,
* Ve kendi kelimeleri üzerinden çoktan seçmeli testler çözebilir.
  
# 🧩 Uygulama Yapısı

# 🔹 `profiles`
* Kullanıcı profili oluşturma ve yönetme
* Token tabanlı giriş ve kimlik doğrulama sistemi

# 🔹 `vocabulary`
* Kullanıcıların kendi İngilizce kelimelerini ve anlamlarını ekleyebildiği sözlük modülü
* Diğer kullanıcıların sözlüklerini görüntüleyebilme

# 🔹 `exercise`
* Kullanıcının sözlüğünden rastgele kelimelerle oluşturulan çoktan seçmeli quiz sistemi
* Doğru cevap + yanlış seçeneklerle interaktif alıştırmalar

# 🚀 Projede Kullanılan Teknolojiler
- Python
- Django
- Django Rest Framework
- SQLite 
- Postman
- Heroku 

# 🔄 Serializer Yapısı
Bu projede Django Rest Framework Serializer yapısı, model ile API arasındaki veri dönüşümünü kontrol etmek için kullanılmıştır.

Serializer'lar sayesinde:
* Model nesneleri JSON formatına çevrildi (ve tersi),
* Giriş verileri için validasyon kuralları tanımlandı,
* Her kullanıcıya ait verilerin güvenli şekilde yönetimi sağlandı.

# 🛡️ Yetkilendirme ve Güvenlik

Projede `IsOwnerOrReadOnly` yetkilendirmesi kullanılarak, kullanıcıların yalnızca **kendi kelimelerini düzenleyebilmesi** sağlanmıştır.  
Giriş ve kayıt işlemlerinden sonra token ile kimlik doğrulama yapılır.

# 🔐 Kimlik Doğrulama ve Token Kullanımı
Kullanıcıların güvenli giriş yapabilmesi için Token Authentication yöntemi kullanılmıştır.
Kullanıcılar kayıt veya giriş yaptıktan sonra kendilerine özel bir token alır ve sonraki API isteklerinde bu token ile kimlik doğrulaması yaparlar.

Kullanımı:
* Giriş sonrası API'den dönen token alınır.
* API çağrılarında HTTP header’a bu formatta eeklenir;
  Authorization: Token <your_token>

# ☁️ Deploy: Heroku Kullanımı
Projeyi hızlıca canlıya alabilmek ve dış dünyayla paylaşabilmek için Heroku platformunu tercih edildi.

Heroku’nun avantajları:
* Django projeleri için kolay ve hızlı deploy imkanı
* Anlık test ve paylaşım için uygun ortam
* Git tabanlı deploy ile kodun doğrudan GitHub’dan yayınlanabilmesi

Bu sayede projenin API uç noktaları gerçek bir sunucuda çalışır hale geldi.































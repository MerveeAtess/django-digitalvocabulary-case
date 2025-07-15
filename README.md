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
- SQLite (varsayılan)
- Postman (API testi)
- Heroku (deploy - isteğe bağlı)

# 🔄 Serializer Yapısı
Bu projede Django Rest Framework Serializer yapısı, model ile API arasındaki veri dönüşümünü kontrol etmek için kullanılmıştır.

Serializer'lar sayesinde:
* Model nesneleri JSON formatına çevrildi (ve tersi),
* Giriş verileri için validasyon kuralları tanımlandı,
* Her kullanıcıya ait verilerin güvenli şekilde yönetimi sağlandı.

# 🛡️ Yetkilendirme ve Güvenlik

Projede `IsOwnerOrReadOnly` yetkilendirmesi kullanılarak, kullanıcıların yalnızca **kendi kelimelerini düzenleyebilmesi** sağlanmıştır.  
Giriş ve kayıt işlemlerinden sonra token ile kimlik doğrulama yapılır.


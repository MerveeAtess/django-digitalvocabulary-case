from rest_framework.generics import ListCreateAPIView,RetrieveUpdateDestroyAPIView
from rest_framework.permissions import IsAuthenticated
from rest_framework.views import APIView
from rest_framework.response import Response

from vocabularies.serializers import VocabularySerializer, WordSerializer
from vocabularies.models import Vocabulary, Word

from profiles.models import Profile

from django.shortcuts import get_object_or_404

from vocabularies.permissions import IsOwnerOrReadonly, IsOwnerOfVocabularyOrReadOnly

# ListCreateAPIView:query üzerinden listeleme yapmamızı sağlar, yeni vt kayıtları oluşturur

# kullanıcıların kendi sözlüklerini görüntüleyebildiği,
#  yeni sözlük oluşturmasını gösteren model

class VocabularyListCreateView(ListCreateAPIView):
   # vocabulary modeline ait
    serializer_class= VocabularySerializer

    # filtrelerine göre queryset yapma
    def get_queryset(self):
        # urlden gelen queryparamdan alır
        # kendi sözlüklerimizi görüntülemek yerine bu profile_idye göre olan kullanıcıyı alır
        profile_id= self.request.query_params.get('profile_id')

        if profile_id:
            profile= get_object_or_404(Profile, id=profile_id)
        else:
            profile= self.request.user.profile
            
        profile= self.request.user.profile
        # get_object_or_404(Profile, user=self.request.user) yazılabilirdi

        # vt da arama yapmak için
        # profile=profile isteği gönderen profille aynı olsun
        queryset= Vocabulary.objects.filter(profile=profile)

        return queryset
    
    # serializerin ListCreateAPIView tarafından save metodu çalıştırılmadan önce çalıştırılan metod
    # kaydedilmeden önce bu kod çalışacak
    def perform_create(self, serializer):
        serializer.save(profile= self.request.user.profile)
    
# tekil vocabulary üzerinde işlem yapmak için(VocabularyDetailView)
class VocabularyDetailView(RetrieveUpdateDestroyAPIView):
    serializer_class=VocabularySerializer
    queryset= Vocabulary.objects.all()

    # tüm kullanıcılar kullanamasın diye(silme/güncelleme yapamaz başka kullanıcıların)
    permission_classes= [IsOwnerOrReadonly , IsAuthenticated]
    # urls.py'da gösterebilmek için
    lookup_field='id'

class WordListCreateView(ListCreateAPIView):
    serializer_class= WordSerializer

    # url üzerinden gelen vocabulary(id) nin kaydının olup olmadığını getirsin
    def get_queryset(self):
        vocabulary_id= self.kwargs.get('vocabulary_id')

        # doğrulama yapmak için
        vocabulary= get_object_or_404(Vocabulary, id= vocabulary_id)
        
        return Word.objects.filter(vocabulary=vocabulary)
   
    def perform_create(self, serializer):
        vocabulary_id= self.kwargs.get('vocabulary_id')
        vocabulary= get_object_or_404(Vocabulary, id= vocabulary_id,
                                      profile= self.request.user.profile)

        serializer.save(vocabulary=vocabulary )
   
# silme/güncelleme/tekil olarak yapılan işlemleri belirt
class WordDetailView(RetrieveUpdateDestroyAPIView):
    serializer_class= WordSerializer
    queryset= Word.objects.all()
    permission_classes= [IsOwnerOfVocabularyOrReadOnly, IsOwnerOfVocabularyOrReadOnly ]

    # genericviewin quearyset üzerinden ilgili objeyi seçmeyi sağlar
    def get_object(self):
        vocabulary_id= self.kwargs.get('vocabulary_id')
        word_id= self.kwargs.get('word_id')

        word= get_object_or_404(Word, id=word_id, vocabulary_id=vocabulary_id)
        
        # izni kontrol etme, izne saip mi değil mi parametrelerini alır
        self.check_object_permissions(self.request, word)
        return word

# bir kullanıcının uygulamada kayıtlı olan diğer kullanıcının oluşturduu,
# sözlüğü kendi hesabına kopyalamasını sağlayan metot
# apiview kullanmamızın nedeni: yapılan işlemlerin doğrudan model etrafında değil de 
# ayrı ayrı özelleştiren kısım old. için kullandık
class CopyVocabularyView(APIView):

    # vocabulary_id:tanımlanan urlden gelecek
    def post(self, request, vocabulary_id):

        # kopyalanmadan önceki vocabulary
        original_vocabulary= get_object_or_404(Vocabulary, id= vocabulary_id)

        # oluşturmak istenen voc. özellikleri girilir
        copied_vocabulary= Vocabulary.objects.create(

            # apiye isteği atan kullanıcıyı verdik
            profile= request.user.profile,
            # kopyaladığımızı belirttik
            name= f"Copy of {original_vocabulary.name}",
            description= original_vocabulary.description,

        )
        # original'deki tüm kelimeleri almak için
        words = Word.objects.filter(vocabulary= original_vocabulary)
        for word in words:
            Word.objects.create(
                vocabulary= copied_vocabulary,
                text= word.text,
                meaning= word.meaning,
                example_sentence= word.example_sentence
            )
        return Response ({
            "success" : "Kelimeler başarıyla kopyalandı."
        })

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from django.shortcuts import get_object_or_404

from profiles.models import Profile

from vocabularies.models import Word

import random

# kullanıcların sözlükleri üzerinden soru oluşturmasını sağlayan model
class QuestionView(APIView):

    def get(self, request):
        #soru soracak kişinin profilini alma 
        #almak istenen profile kaydının kriterini alma
        profile= get_object_or_404(Profile, user=request.user)

        #profile ait tüm sözlüklerin tüm kelimelerini değ. tutmak
        words= Word.objects.filter(vocabulary__profile= profile)

        #4 şıklı bir soru oluşturmak için kelime sayısı 4ten az olmamalı
        if words.count() < 4:
            return Response({
                "error" : "Yeterince kelime bulunamadı. Lütfen en az 4 kelime ekleyiniz."},
                status= status.HTTP_400_BAD_REQUEST )
        
        words_list= list(words)
        # rastgele eleman seçme
        selected_word= random.choice(words_list)
        # sadece anlamını getirsin
        options= [selected_word.meaning]

        while len(options) < 4:
            wrong_options= random.choice(words_list).meaning

            # aynı random kelimeler gelmesin diye
            if wrong_options not in options:
                options.append(wrong_options)

        #options nesnesindeki kelimelerin yerlerini karıştır
        random.shuffle(options)

        question_data= {
            "question" : selected_word.text,
            "options" : options,
            "correct answer" : selected_word.meaning
        }

        return Response(question_data)



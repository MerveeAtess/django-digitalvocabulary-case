from rest_framework import serializers
from vocabularies.models import Vocabulary, Word


class VocabularySerializer(serializers.ModelSerializer):
    #hangi modele referens alcağını gösterir
    
    class Meta:
        model= Vocabulary
        #serializer oluşturulurken kullanılacak fields
        fields= ('id', 'name', 'description')

class WordSerializer(serializers.ModelSerializer):
    # vocabulary,models.py'daki word classını tetiklesin diye
    # post isteğinde doğrudan url üzerinden alsın
    vocabulary= serializers.PrimaryKeyRelatedField(read_only= True)

    class Meta:
        model= Word
        fields='__all__'

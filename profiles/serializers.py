from rest_framework import serializers,validators
from django.contrib.auth.password_validation import validate_password
from profiles.models import CustomUser, Profile


class RegisterSerializer(serializers.ModelSerializer):
    #özelleştirmek istediklerimiz
    email= serializers.EmailField(validators= [validators.UniqueValidator(
        queryset= CustomUser.objects.all())])
    
    # validators=[validate_password]: setting.py> şifre doğrulama tekniklerini bu field'a uygular
    password= serializers.CharField(write_only= True, required=True, 
                                   validators=[validate_password])
   
    class Meta:
        model= CustomUser
        fields= ('id', 'username', 'email', 'password')

    #save metodu çalıştırıldığında;
    # validated_data: serializerda doğrulanmış veriyi tetikler
    def create(self, validated_data):
        # create_user() : sağlanan şifrenin hashlenmesini sağlar
        user= CustomUser.objects.create_user(
            username= validated_data['username'],
            email= validated_data['email'],
            password= validated_data['password']
        )

        return user 
    
class UserSerializer(serializers.ModelSerializer):

    class Meta:
        model= CustomUser
        fields= ('id', 'username')

class ProfileSerializer(serializers.ModelSerializer):
    # sadece UserSerializer bilgilerini getirsin
    user= UserSerializer()

    class Meta:
        model= Profile
        fields= ('id', 'user')

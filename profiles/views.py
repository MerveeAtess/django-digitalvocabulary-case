from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import permissions
from rest_framework.generics import ListAPIView
from rest_framework import status

from profiles.serializers import RegisterSerializer,UserSerializer, ProfileSerializer
from profiles.models import Profile, FollowRelation

from django.shortcuts import get_object_or_404

#kullanıcıların kayıt yaparken kullanacağı isteği(request) temsil eder.
class RegisterView(APIView):
    permission_classes= (permissions.AllowAny,)
    
    #kayıt=post işlemi
    def post(self, request):
        serializer= RegisterSerializer(data= request.data)
        # serializer içinde sağlanan bilgilerin koşullara uygun mu değil mi?
        serializer.is_valid(raise_exception= True)

        user= serializer.save()
        #kendisinde tanımlı olan fields buradan alır.
        user_serializer= UserSerializer(user)
        return Response(user_serializer.data)

# usersearchview: bir kullanıcının diğer kullanıcıları username ile aratmasını
# followuserview: bir userın diğerini takip etmesi için
# unfollowuserview: takip edeni çıkmak için
# followedlistview: takip edenleri listelemek için 


######### usersearchview #######
#listapiview yapmamızın sebebi: kullanıcıların diğer kullanıcıları username ile aratmasını sağlar
# list dönecek.düzenleme silme gibi işlemler yapılmayacak!
class ProfileSearchView(ListAPIView):
    serializer_class= ProfileSerializer
    """kullanıcının her seferinde tüm kullanıcılarını almayı sağlar
    queryset= Profile.objects.all()"""

    def get_queryset(self):
        username= self.request.query_params.get('username', '')
      
        #paramtre sağlanmışsa
        if username:
            # icontains: büyük-küçük harften bağımsız olarak username aratsın
            return Profile.objects.filter(user__username__icontains= username)
        
        # sağlanmazsa boş query_set döndür
        return Profile.objects.none()
    
####### followuserview #######
# özeleştirme yapmak için apiview kullanılıyor
class FollowProfileView(APIView):

    #takip etme işlemi post metodu ile yapılır
    # username: doğrudan url içinden alınır, takip etmek istenilen user
    def post(self, request, username):
        profile_to_follow= get_object_or_404(Profile, user__username=username)
        
        #kişi kendini takip etmesin diye
        if request.user.profile== profile_to_follow:
            return Response({"error": "Kendini takip edemezsin"},
                            status=status.HTTP_400_BAD_REQUEST)
        
        #zaten takip ediliyorsa tekrar yapmaya gerek yok. eğer yoksa oluşturur
        FollowRelation.objects.get_or_create(follower= request.user.profile, following= profile_to_follow)
        return Response({
            "success": "Başarıyla takip edilmiştir."
        })

###### unfollowuserview ######

class UnfollowProfileView(APIView):
    def post(self, request, username):
        profile_to_unfollow= get_object_or_404(Profile, user__username=username)

         #takip ediliyor mu?
         # following: unfollow yapılacak kişi
         # follower= unfollow yapan kişi(biz)
        follow_relation= FollowRelation.objects.filter(follower= request.user.profile,
                                                   following=profile_to_unfollow)
        if follow_relation.exists():
            follow_relation.delete()
            return Response({
                "success": "Kullanıcı başarıyla takipten çıkıldı"
            })
        else:
            return Response({
                "error":"Bu kullanıcıyı takip etmiyorsunuz"
            },
            status=status.HTTP_400_BAD_REQUEST)

########## followedlistview ######
# aktif profilleri inceler
class FollowedListView(ListAPIView):
    serializer_class= ProfileSerializer

    # queryset direkt yazmak yerine;
    def get_queryset(self):

        # isteği yapan kullanıcının profilini göster
        user_profile= self.request.user.profile
        return user_profile.followers.all()
    
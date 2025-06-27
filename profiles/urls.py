from django.urls import path
#JSON WEB AUTHENTICATION -PROFİLES'DA OLACAĞI İÇİN 
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

from profiles.views import RegisterView,ProfileSearchView,FollowProfileView, UnfollowProfileView,FollowedListView

urlpatterns = [
    path('register/', RegisterView.as_view(), name= 'register'),
    #kullanıcı bilgileri
    path('token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    #tokenin süresibitmeden istek atabileceğimiz kısım
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),

    path('search/', ProfileSearchView.as_view(), name='search-profile'),
    path('follow/<str:username>/', FollowProfileView.as_view(), name='follow-profile'),
    path('unfollow/<str:username>/', UnfollowProfileView.as_view(), name='unfollow-profile'),
    path('followed-list/', FollowedListView.as_view(), name='followed-list'),
         
]

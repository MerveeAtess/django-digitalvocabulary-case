from rest_framework import permissions


#tüm kullanıcılar kullanamasın diye(silme/güncelleme yapamaz başka kullanıcıların)
# IsOwnerOrReadonly: nesnein sahibi mi eğer değilse sadece okuma işlemi yapsın
class IsOwnerOrReadonly(permissions.BasePermission):

    def has_object_permission(self, request, view, obj):

        # SAFE_METHODS: 'GET', 'HEAD', 'OPTIONS'ları tanımlar
        #bunlarla yapılan istekte sunucu tarafınada değişiklik yapılmadığı için güvenli
        if request.method in permissions.SAFE_METHODS:
            return True
        else :
            #doğrulama yapması gerekir
            return obj.profile.user== request.user
        
class IsOwnerOfVocabularyOrReadOnly(permissions.BasePermission):
        def has_object_permission(self, request, view, obj):

            if request.method in permissions.SAFE_METHODS:
                return True
            
            return obj.vocabulary.profile.user== request.user




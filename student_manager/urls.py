from django import views
from django.contrib import admin
from django.urls import path,include
from rest_framework_simplejwt.views import TokenObtainPairView,TokenRefreshView  

urlpatterns = [
    path('admin/', admin.site.urls),
    path('gettoken/',
        TokenObtainPairView.as_view(),
         name ='token_obtain_pair'),
    path('refreshtoken/',
         TokenRefreshView.as_view(),
         name ='token_refresh'),    
    path('',include('crud_api.urls')),
]

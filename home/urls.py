from django.urls import path
from home.views import index , RegisterApi , LoginApi , person
# from rest_framework_simplejwt.views import (
#     TokenObtainPairView,
#     TokenRefreshView,
# )


urlpatterns = [

    path('index/',index),
    path('personapi/',person.as_view()),
    path('register/',RegisterApi.as_view()),
    path('login/',LoginApi.as_view()),
    # path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    # path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
] 
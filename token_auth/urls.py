from django.contrib import admin
from django.urls import path
from rest_framework.routers import DefaultRouter
from api import views
from django.urls import include
# from rest_framework.authtoken.views import obtain_auth_token
from api.auth import CustomAuthToken

router = DefaultRouter()

router.register('studentapi',views.StudentModelViewSet,basename='student')
urlpatterns = [
    path('admin/', admin.site.urls),
    path('',include(router.urls)),
    path('auth/',include('rest_framework.urls',namespace='rest_framework')),
    # path('gettoken/',obtain_auth_token)
    # there are 2 ways to get/create token using command lins as below:
    # 1. python manage.py drf_create_token username
    # 2. get token is used to get/create token using comand as below:
    #  http POST http://127.0.0.1:8000/gettoken/ username="username" password="password"

    path('gettoken/',CustomAuthToken.as_view())
    # above url is used to get email and pk in response along with token by creating auth.pys
]

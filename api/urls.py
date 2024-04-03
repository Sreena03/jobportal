from django.urls import path
from rest_framework.authtoken.views import ObtainAuthToken
from api import views
from rest_framework.routers import DefaultRouter
router=DefaultRouter()

router.register("v2/task",views.Jobviewsetview,basename="name")

urlpatterns = [
    path("token/",ObtainAuthToken.as_view()),
    path("register/",views.Signup.as_view(),name='reg')
]+router.urls


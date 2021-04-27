from  django.urls import path,include
from .views import taskviewclass
from rest_framework.routers import DefaultRouter
router=DefaultRouter()

router.register('task',taskviewclass,basename='student')

urlpatterns=[
    path('',include(router.urls)),
    path('<int:pk>/',include(router.urls)),
]
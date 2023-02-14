from django.urls import path, include
from rest_framework import routers 
from .views import PersonaViewSet, PersonaSerializer
from .imc import IMCView


router = routers.DefaultRouter()
router.register('', PersonaViewSet, 'persona')


urlpatterns = [
        path('', include(router.urls)),
        path('imc/<str:nombre>/', IMCView.as_view(), name = 'imc-persona')
        

        ]
        

from rest_framework import viewsets, serializers
from rest_framework.views import APIView
from .models import Persona


class PersonaSerializer(serializers.ModelSerializer):

    class Meta:
        model  = Persona
        fields = ('id', 'nombre', 'altura', 'peso')


class PersonaViewSet(viewsets.ModelViewSet):
    queryset         = Persona.objects.all()
    serializer_class = PersonaSerializer

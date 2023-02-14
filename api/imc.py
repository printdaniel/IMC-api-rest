from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status 
from .models import Persona
from .views import PersonaSerializer


class IMCView(APIView):

    def get(self, request, nombre):
        try:
            persona = Persona.objects.get(nombre=nombre)
        except Persona.DoesNotExist:
            return Response({'error': 'Persona no encontrada'}, status=status.HTTP_404_NOT_FOUND)

        peso = persona.peso
        altura = persona.altura
        imc = round(peso / (altura**2),1)

        return Response({'imc': imc}, status=status.HTTP_200_OK)

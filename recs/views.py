from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Recomendation
from .serializers import RecomendationSerializer

class RecomendationAPIView(APIView):
    def get(self, request):
        reason_text = request.query_params.get('reason_text')
        if reason_text:
            try:
                recomendation = Recomendation.objects.get(reason_text=reason_text)
                return Response({'recomendation_text': recomendation.recomendation_text}, status=status.HTTP_200_OK)
            except Recomendation.DoesNotExist:
                return Response({'error': 'No recommendation found for the given reason_text'}, status=status.HTTP_404_NOT_FOUND)
        return Response({'error': 'reason_text parameter is required'}, status=status.HTTP_400_BAD_REQUEST)

# Create your views here.
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import LiveNews
from .serializers import LiveNewsSerializer


class LiveNewsView(APIView):
    def get(self, request):
        news = LiveNews.objects.all()
        serializer = LiveNewsSerializer(news,many=True)
        return Response({"live-news": serializer.data})

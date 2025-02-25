from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import ShortenedURL
from .serializers import ShortenedURLSerializer

class URLShortenerView(APIView):

    def post(self, request):
        original_url = request.data.get('original_url')
        if not original_url:
            return Response({'error': 'URL is mandatory'}, status=status.HTTP_400_BAD_REQUEST)

        try:
            existing_url = ShortenedURL.objects.get(original_url=original_url)
            if existing_url.original_url:
                serializer = ShortenedURLSerializer(existing_url)
                return Response(serializer.data, status=status.HTTP_201_CREATED)
        except ShortenedURL.DoesNotExist:
            url_obj = ShortenedURL.objects.create(original_url=original_url)
            serializer = ShortenedURLSerializer(url_obj)
            return Response(serializer.data, status=status.HTTP_201_CREATED)

class RedirectView(APIView):

    def get(self, request, short_code):
        try:
            url_obj = ShortenedURL.objects.get(short_code=short_code)
            url_obj.access_count += 1
            url_obj.save()
            return Response({"redirect_to": url_obj.original_url})
        except ShortenedURL.DoesNotExist:
            return Response({'error': 'URL not found.'}, status=status.HTTP_404_NOT_FOUND)

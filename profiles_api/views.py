from rest_framework.views import APIView
from rest_framework.response import Response


class HelloApiView(APIView):
    """Test Api view"""

    def get(self, request):
        """Returns a list of APIVIEW features"""

        an_apiview = [
            'Uses HTTP methods as functions(get, post, delete, patch, put)',
            'Is similar to a traditional django view',
            'GIves you the most control over your application logic',
            'Is mapped manually to urls'

        ]

        return Response({'message': 'Hello', 'an_apiview': an_apiview})

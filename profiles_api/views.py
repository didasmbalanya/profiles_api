from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from . import serializers


class HelloApiView(APIView):
    """Test Api view"""

    serializer_class = serializers.HelloSerializer

    def get(self, request):
        """Returns a list of APIVIEW features"""

        an_apiview = [
            'Uses HTTP methods as functions(get, post, delete, patch, put)',
            'Is similar to a traditional django view',
            'GIves you the most control over your application logic',
            'Is mapped manually to urls'

        ]

        return Response({'message': 'Hello ', 'an_apiview': an_apiview})

    def post(self, request):
        """Returns a name with with a greeting"""

        serializer = self.serializer_class(data=request.data)

        if serializer.is_valid():
            name = serializer.validated_data.get('name')
            message = f'hello {name}'
            return Response({'message': message})
        else:

            print("<<<<<<<<<<<< serializer.errors >>>>>>>>>>>> \n", serializer.errors, " \n <<<<<<<<<<<<")
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def put(self, request):
        """Updating an object"""
        serializer = self.serializer_class(data=request.data)

        return Response({'message': 'Put update a whole entity'})

    def patch(self, request, pk=None):
        """"update a few properties of an item"""
        return Response({'message': 'Patch'})

    def delete(self, request, pk=None):
        """delete an object"""
        print("\n Callllling")
        return Response({'method': "DELETE"})

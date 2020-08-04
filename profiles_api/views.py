from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status, viewsets, filters
from rest_framework.authentication import TokenAuthentication

from . import models, permissions, serializers


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


class HelloViewSet(viewsets.ViewSet):
    """Test Api view set"""

    serializer_class = serializers.HelloSerializer

    def list(self, request):
        """return a hello message"""
        a_viewset = [
            'uses actions: (create, list, retrieve,update, partial update and destroy',
            'automatically maps to URLs using ROuters',
            'provides more functionality with less code'
        ]
        return Response({'message': 'Hello view set', 'a_viewset': a_viewset})

    def create(self, request):
        """create a new hello message"""
        serializer = self.serializer_class(data=request.data)

        if serializer.is_valid():
            name = serializer.validated_data.get('name')
            message = f'Hello {name}!'
            return Response({'message': message})
        else:
            return Response(serializer.errors, status.HTTP_400_BAD_REQUEST)

    def retrieve(self, request, pk=None):
        """Hangle getting an object by ID"""
        return Response({'HTTP_METHOD': f'GET {pk}'})

    def update(self, request, pk=None):
        """Handle updating an object by ID"""
        return Response({'HTTP_METHOD': f'PUT {pk}'})

    def partial_update(self, request, pk=None):
        """Handle updating part of the entity by ID"""
        return Response({'HTTP_METHOD': f'PATCH {pk}'})

    def destroy(self, request, pk=None):
        """Handle delete an entity"""
        return Response({'HTTP_METHOD': f'DELETE {pk}'})


class UserProfileViewSet(viewsets.ModelViewSet):
    """Handle creating and updating profiles"""

    serializer_class = serializers.UserProfileSerialzer
    queryset = models.UserProfile.objects.all()
    authentication_classes = (TokenAuthentication,)
    permission_classes = (permissions.UpdateOwnProfile, )
    filter_backends = (filters.SearchFilter,)
    search_fields = ('name', 'email',)

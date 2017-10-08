from json import dumps, loads
from rest_framework import status, viewsets
from rest_framework.decorators import detail_route
from rest_framework.response import Response

from . import models, serializers


class CubeViewSet(viewsets.ModelViewSet):
    """
    ViewSet for Cube
    """
    queryset = models.Cube.objects.all()
    serializer_class = serializers.CubeSerializer

    @detail_route(methods=['post'])
    def requestUpdate(self, request, *args, **kwargs):
        """
            Request Update
        """
        cube = self.get_object()
        serializer = serializers.UpdateSerializer(
            data=request.data,
            dimension=cube.dimension
        )
        if not serializer.is_valid():
            return Response({'errors': serializer.errors}, status.HTTP_400_BAD_REQUEST)

        data = serializer.data
        x = data['x'] - 1
        y = data['y'] - 1
        z = data['z'] - 1
        w = data['w']

        matrix = loads(cube.matrix)
        matrix[x][y][z] = w
        cube.matrix = dumps(matrix)
        cube.save()
        return Response(matrix, status.HTTP_200_OK)

    @detail_route(methods=['post'])
    def requestQuery(self, request, *args, **kwargs):
        """
            Request Query
        """
        cube = self.get_object()
        serializer = serializers.QuerySerializer(
            data=request.data,
            dimension=cube.dimension
        )
        if not serializer.is_valid():
            return Response({'errors': serializer.errors}, status.HTTP_400_BAD_REQUEST)

        data = serializer.data
        x1 = data['x1'] - 1
        y1 = data['y1'] - 1
        z1 = data['z1'] - 1
        x2 = data['x2']
        y2 = data['y2']
        z2 = data['z2']

        matrix = loads(cube.matrix)
        suma = 0
        for x in range(x1, x2):
            for y in range(y1, y2):
                for z in range(z1, z2):
                    suma += matrix[x][y][z]
        return Response(suma, status.HTTP_200_OK)

from json import dumps
from rest_framework import serializers
from cube import models


class CubeSerializer(serializers.ModelSerializer):
    """
        Cube Serializer
    """

    class Meta:
        model = models.Cube
        fields = ('id', 'dimension', 'matrix',)
        read_only_fields = ('id', 'matrix',)

    def validate_dimension(self, value):

        if value < 1 or value > 50:
            raise serializers.ValidationError("Dimension range 1<=N<=50")
        return value

    def create(self, validated_data):
        n = validated_data['dimension']
        matrix = [[[0 for k in range(n)] for j in range(n)] for i in range(n)]
        validated_data['matrix'] = dumps(matrix)
        dimension = models.Cube.objects.create(**validated_data)
        return dimension


class UpdateSerializer(serializers.Serializer):
    """
        Update Serializer
    """
    x = serializers.IntegerField()
    y = serializers.IntegerField()
    z = serializers.IntegerField()
    w = serializers.IntegerField()

    def __init__(self, *args, **kwargs):
        self.dimension = kwargs.pop('dimension', None)
        super(UpdateSerializer, self).__init__(*args, **kwargs)

    def validate(self, data):
        if data['x'] > self.dimension or + \
            data['y'] > self.dimension or + \
                data['z'] > self.dimension:
            raise serializers.ValidationError("x,y,z must not be greater than N")

        if data['x'] < 0 or +\
            data['y'] < 0 or +\
                data['z'] < 0:
            raise serializers.ValidationError("x,y,z must be greater equal to 1")

        return data


class QuerySerializer(serializers.Serializer):
    """
        Query Serializer
    """
    x1 = serializers.IntegerField()
    y1 = serializers.IntegerField()
    z1 = serializers.IntegerField()
    x2 = serializers.IntegerField()
    y2 = serializers.IntegerField()
    z2 = serializers.IntegerField()

    def __init__(self, *args, **kwargs):
        self.dimension = kwargs.pop('dimension', None)
        super(QuerySerializer, self).__init__(*args, **kwargs)

    def validate(self, data):

        if data['x1'] > self.dimension or + \
            data['y1'] > self.dimension or + \
                data['z1'] > self.dimension or + \
                data['x2'] > self.dimension or + \
                data['y2'] > self.dimension or + \
                data['z2'] > self.dimension:
            raise serializers.ValidationError("x1,y1,z1,x2,y2,z2 must not be greater than N")

        if data['x1'] > data['x2']:
            raise serializers.ValidationError("x1 must not be greater than x2")

        if data['y1'] > data['y2']:
            raise serializers.ValidationError("y1 must not be greater than y2")

        if data['z1'] > data['z2']:
            raise serializers.ValidationError("z1 must not be greater than z2")

        return data

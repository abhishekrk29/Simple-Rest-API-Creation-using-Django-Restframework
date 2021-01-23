from rest_framework import serializers

class TestSerializers(serializers.Serializer):
    zip=serializers.CharField(max_length=20)
    city=serializers.CharField(max_length=20)
    age=serializers.IntegerField()

    def __str__(self):
        return "Test Serializer Object"
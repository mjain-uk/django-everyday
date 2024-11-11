from rest_framework import serializers
from basiccrud.models import Todo

class TodoSerializer(serializers.Serializer):
    name = serializers.CharField(max_length = 50, required = True)
    id = serializers.CharField(read_only=True)

    def create(self, validated_data):
        name = validated_data['name']
        return Todo.objects.create(name= name)
    
    def update(self, instance, validated_data):
        instance.name = validated_data['name']
        instance.save() 
        return instance

    
class TodoModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = Todo
        fields = ['name', 'id']
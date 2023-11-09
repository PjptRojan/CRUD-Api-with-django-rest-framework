from rest_framework import serializers
from .models import Student

# Validators:
def starts_with_r(value):
    if value[0].lower() != 'r':
        raise serializers.ValidationError('Name must start with r')

class StudentSerializer(serializers.Serializer):
    name = serializers.CharField(max_length=100, validators=[starts_with_r])
    roll = serializers.IntegerField()
    city = serializers.CharField(max_length=50)
    
    def create(self, validated_data):
        return Student.objects.create(**validated_data)
    
    def update(self, instance, validated_data):
        instance.name = validated_data.get('name', instance.name)
        instance.roll = validated_data.get('roll', instance.roll)
        instance.city = validated_data.get('city', instance.city)
        instance.save()
        return instance
    

    #Field Level Validation:
    def validate_roll(self, value):
        if value >= 200:
            raise serializers.ValidationError('Seat full')
        return value
    
    #Object Level Validation(multiple fields validation at once):
    def validate(self, data):
        nm = data.get('name')
        ct = data.get('city')
        if nm.lower() == 'rojina' and ct.lower() != 'bhaktapur':
            raise serializers.ValidationError('City must be Bhaktapur')
        return data
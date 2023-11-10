from rest_framework import serializers
from .models import Student


class StudentSerializer(serializers.ModelSerializer):
   # Validators:
   def starts_with_r(value):
    if value[0].lower() != 'r':
        raise serializers.ValidationError('Name must start with r')
   name = serializers.CharField(validators = [starts_with_r])

   class Meta:
    model = Student
    fields = ['name', 'roll', 'city']    

    #Field Level Validation:
   def validate_roll(self, value):
        if value >= 200:
            raise serializers.ValidationError('Seat full')
        return value
    
    #Object Level Validation(multiple fields validation at once):
   def validate(self, data):
        nm = data.get('name')
        ct = data.get('city')
        if nm.lower() == 'minisha' and ct.lower() != 'bhaktapur':
            raise serializers.ValidationError('City must be Bhaktapur')
        return data
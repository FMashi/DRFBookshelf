from rest_framework import serializers
from rest_framework.exceptions import ValidationError
from .models import CustomUser

class UserSerializer(serializers.ModelSerializer):
   class Meta:
       model = CustomUser
       fields = ['username', 'email', 'password']
       extra_kwargs = {'password': {'write_only': True}}


   def create(self, validated_data):
       user = CustomUser(
           username=validated_data['username'],
           email=validated_data['email'],
           faculty=validated_data.get('faculty'),
            semester=validated_data.get('semester'),
            city=validated_data.get('city'),
            gender=validated_data.get('gender')
       )
       user.set_password(validated_data['password'])
       user.save()
       return user


    
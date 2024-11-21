from django.contrib.auth.models import User
from rest_framework import serializers
from .models import Book,Review

class UserRegisterserializer(serializers.ModelSerializer):

    password=serializers.CharField(write_only=True)
    class Meta:
        model=User
        fields=['id','username','email','password']

    def create(self, validated_data):
        user=User.objects.create_user(
            username=validated_data['username'],
            email=validated_data['email'],
            password=validated_data['password']
        )
        return user
    
class Bookserializer(serializers.ModelSerializer):
    average_rating=serializers.FloatField(read_only=True)
    class Meta:
        model=Book
        fields=['id','title','author','isbn','genre','cover_image','date','average_rating']

class Reviewserializer(serializers.ModelSerializer):
    class Meta:
        model=Review
        fields=['id','book','user','rating','content','created_at','updated_at']
        read_only_fields=['user']

    def validate_ratings(self,value):
        if value <1 or value >5:
            raise serializers.ValidationError('rating must be between 1 to 5')
        return value
from rest_framework import serializers
from django.contrib.auth.models import User
from django.core.mail import send_mail
import random
from home.models import Person , Color , Color_Shades


class ColorShadesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Color_Shades
        fields = ['color_shades']

    def to_representation(self, instance):
        representation = super(ColorShadesSerializer, self).to_representation(instance)
        if instance.id ==1:
            representation['color_shades'] = 'Baby Pink'
        return representation

class ColorSerializer(serializers.ModelSerializer):
    shades = ColorShadesSerializer()
    class Meta:
        model = Color
        fields = ['color_name' , 'shades']
        # depth = 1


class PersonSerializer(serializers.ModelSerializer):
    color =  ColorSerializer()
    class Meta:
        model = Person
        fields = "__all__"
        # depth = 1

    def validate(self, data):
        if data['age'] < 18:
            raise serializers.ValidationError('age should be equal or greater than 18')
        return data


class RegisterSerializer(serializers.Serializer):
    username =  serializers.CharField()
    email =  serializers.EmailField()
    password = serializers.CharField()

    def validate(self,data):
        if data['username']:
            if User.objects.filter(username = data['username']).exists():
                raise serializers.ValidationError('username already exists!.. Try new')
            
        if data['email']:
            if User.objects.filter(email = data['email']).exists():
                raise serializers.ValidationError('email already exists!.. Try new')

        return data 
         
    def create(self, validated_data):
        user = User.objects.create(username =  validated_data['username'],email = validated_data['email'] , password = validated_data['password'])
        user.set_password(validated_data['password'])
        user.save()
        return validated_data
        print(validated_data)

class LoginSerializer(serializers.Serializer):
    username = serializers.CharField()
    password = serializers.CharField()

    def validate(self, data):
        if not data['username']:
            raise serializers.ValidationError("please enter the usename")
        
        if not data['password']:
            raise serializers.ValidationError("please enter the password")

        return data


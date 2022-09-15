from rest_framework import serializers
from django.contrib.auth import get_user_model

from core.models import Book, CheckOutHistory

User = get_user_model()
    

class UserSerializer(serializers.ModelSerializer):

    password = serializers.CharField(write_only=True)

    def create(self, validated_data):
        user = User.objects.create_user(
            email=validated_data['email'],
            username=validated_data['username'],
            password=validated_data['password'],
        )

        return user
    
    def update(self, instance, validated_data):
        password = validated_data.pop('password')
        user = super().update(instance, validated_data)
        if password:
            user.set_password(password)
            user.save()
        return user

    class Meta:
        model = User
        fields = ('id', 'email', 'username', 'password')
    
class BookSerializer(serializers.ModelSerializer):
    available_count = serializers.SerializerMethodField()
    
    class Meta:
        model = Book
        fields =('id', 'title', 'author', 'total_count', 'available_count')
    
    def get_available_count(self, instance):
        return instance.available_count

class CheckOutSerializer(serializers.ModelSerializer):

    class Meta:
        model = CheckOutHistory
        fields = ('id', 'book', 'student', 'quantity', 'created_at', 'updated_at', 'returned_at', )
        read_only_fields = ('created_at', 'updated_at', )
    
    def validate(self, attrs):
        attrs = super().validate(attrs)
        if attrs['book'].available_count < attrs['quantity']:
            raise serializers.ValidationError('Quantity should be less than the available quantity')
        return attrs
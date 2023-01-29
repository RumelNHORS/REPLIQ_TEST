from Api.models import AssetsModel, CheckIn, CheckOut, CheckOutAndReturn, DeviceLog, Company
from rest_framework import serializers

#For User Creations
from django.contrib.auth.models import User
from rest_framework import serializers, validators

class RegisterSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('username', 'password', 'email', 'first_name', 'last_name')
        
        extra_kwargs = {
            'password': {'write_only': True},
            'email':{
                'required': True,
                'allow_blank': False,
                'validators': [
                    validators.UniqueValidator(
                        User.objects.all(), "A User With that Email already exists"
                    )
                ]
            }
        }
        
    def create(self, validated_data):
        username = validated_data.get('username')
        password = validated_data.get('password')
        email = validated_data.get('email')
        first_name = validated_data.get('first_name')
        last_name = validated_data.get('last_name')
        
        user = User.objects.create(
            username = username,
            password = password,
            email = email,
            first_name = first_name,
            last_name = last_name
        )
        
        return user
        

class AssetSerializer(serializers.ModelSerializer):
    class Meta:
        model = AssetsModel
        fields = '__all__'

class CheckInSerializer(serializers.ModelSerializer):
    class Meta:
        model = CheckIn
        fields = '__all__'
        
class CheckOutSerializer(serializers.ModelSerializer):
    class Meta:
        model = CheckOut
        fields = '__all__'
        
class CheckOutAndReturnSerializer(serializers.ModelSerializer):
    class Meta:
        model = CheckOutAndReturn
        fields = '__all__'

class DeviceLogSerializer(serializers.ModelSerializer):
    class Meta:
        model = DeviceLog
        fields = '__all__'

class CompanySerializer(serializers.ModelSerializer):
    class Meta:
        model = Company
        fields = '__all__'
from rest_framework import serializers
from heart_disease.models import Heart
from django.contrib.auth.models import User
from rest_framework.validators import UniqueValidator
from django.contrib.auth.password_validation import validate_password
from cancer.models import Cancer
from user.models import Profile
from blood_cell.models import Blood_Cell


class BloodCellListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Blood_Cell
        fields = '__all__'

class HeartDiseaseListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Heart
        fields = '__all__'


class CancerListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cancer
        fields = '__all__'

class RegisterSerializer(serializers.ModelSerializer):
    email = serializers.EmailField(
        required=True,
        validators=[UniqueValidator(queryset=User.objects.all())]
    )

    password = serializers.CharField(write_only=True, required=True, validators=[validate_password])
    password2 = serializers.CharField(write_only=True, required=True)

    class Meta:
        model = User
        fields = ('username', 'password', 'password2', 'email')
        extra_kwargs = {
        }

    def validate(self, attrs):
        if attrs['password'] != attrs['password2']:
            raise serializers.ValidationError({"password": "Password fields didn't match."})

        return attrs

    def create(self, validated_data):
        user = User.objects.create(
            username=validated_data['username'],
            email=validated_data['email'],
        )

        user.set_password(validated_data['password'])
        user.save()
        Profile.objects.create(user=user, username=user.username)

        return user
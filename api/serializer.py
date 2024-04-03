from rest_framework import serializers
from Myapp.models import User,Job

class Login(serializers.Serializer):
    username=serializers.CharField()
    password = serializers.CharField()

class Userserializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id','username','password','email']
        read_only_fields = ['id']

    def create(self,validated_data):
        return User.objects.create_user(**validated_data)



class Jobserializer(serializers.ModelSerializer):
    class Meta:
        model = Job
        fields = "__all__"

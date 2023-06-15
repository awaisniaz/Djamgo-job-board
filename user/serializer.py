from adminuser.models import User
from rest_framework import serializers
class User_Serilalizerr(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('password','email','first_name','last_name','type','username')
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        user = User.objects.create_user(**validated_data)
        return user

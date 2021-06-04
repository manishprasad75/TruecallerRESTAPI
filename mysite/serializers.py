from rest_framework import serializers
from .models import UserSpam, UsersContact


class UserContactSerializer(serializers.ModelSerializer):
    class Meta:
        model = UsersContact
        fields = '__all__'


class UserSpamSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserSpam
        fields = '__all__'
        # unique_together = ('user', 'phone')
    
    def validate(self, data):
        # import pdb
        # pdb.set_trace()
        phone = data.get('phone')
        user = data.get('user')

        itm = UserSpam.objects.filter(phone=phone, user=user).first()
        if itm is not None:
            raise serializers.ValidationError('You already marked it!!')
        return data


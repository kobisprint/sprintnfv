from django.contrib.auth import get_user_model

from rest_framework import serializers

from .models import virtual_machine_type_id, virtual_machine_instance_type_id

User = get_user_model()

class VMSerializer(serializers.ModelSerializer):

    assigned = serializers.SlugRelatedField(
        slug_field=User.USERNAME_FIELD, read_only=True)

    class Meta:
        model = virtual_machine_type_id
        fields = ('id', 'assigned', 'virtual_machine_type_name')

class VMISerializer(serializers.ModelSerializer):

    assigned = serializers.SlugRelatedField(
        slug_field=User.USERNAME_FIELD, read_only=True)

    class Meta:
        model = virtual_machine_instance_type_id
        fields = ('id', 'assigned', 'virtual_machine_type_name')

class UserSerializer(serializers.ModelSerializer):
    full_name = serializers.CharField(source='get_full_name', read_only=True)

    class Meta:
        model = User
        fields = ('id', User.USERNAME_FIELD, 'full_name', 'is_active', )

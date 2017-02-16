from django.contrib.auth import get_user_model

from rest_framework import filters, viewsets, authentication, permissions

from .serializers import VMSerializer, UserSerializer
from .models import virtual_machine_type_id, virtual_machine_instance_type_id

User = get_user_model()

# Create your views here.

class DefaultsMixin(object):
    """Default settings for view authentication, permissions, filtering,
    and pagination."""

    authentication_classes = (
        authentication.BasicAuthentication,
        authentication.TokenAuthentication,
)
    permission_classes = (
        permissions.IsAuthenticated,
)
    paginate_by = 25
    paginate_by_param = 'page_size'
    max_paginate_by = 100

class VMViewSet(DefaultsMixin, viewsets.ModelViewSet):
    model = virtual_machine_type_id
    serializer_class = VMSerializer
    queryset = virtual_machine_type_id.objects.all()

class VMIViewSet(DefaultsMixin, viewsets.ModelViewSet):
    model = virtual_machine_instance_type_id
    serializer_class = VMSerializer
    queryset = virtual_machine_instance_type_id.objects.all()

class UserViewSet(DefaultsMixin, viewsets.ReadOnlyModelViewSet):
    """API endpoint for listing users."""

    lookup_field = User.USERNAME_FIELD
    lookup_url_kwarg = User.USERNAME_FIELD
    queryset = User.objects.order_by(User.USERNAME_FIELD)
    serializer_class = UserSerializer

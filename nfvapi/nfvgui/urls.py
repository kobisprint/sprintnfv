from rest_framework.routers import DefaultRouter

from . import views


router = DefaultRouter()
router.register(r'virtual_machine_type_id', views.VMViewSet)
router.register(r'virtual_machine_instance_type_id', views.VMViewSet)
router.register(r'users', views.UserViewSet)


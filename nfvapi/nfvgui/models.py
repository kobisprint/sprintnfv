from __future__ import unicode_literals
from django.conf import settings
from django.db import models
from django.utils.translation import ugettext_lazy as _

# Create your models here.

class virtual_machine_type_id(models.Model):
    """Parameters for this VM"""
    
    STATUS_GO = 1
    STATUS_NOGO = 2

    STATUS_CHOICES =(
        (STATUS_GO, _('Ready to deploy')),
        (STATUS_NOGO, _('Not ready to deploy')),
    )

    virtual_machine_type_name = models.CharField(max_length=200)
    cpu_cores_required = models.CharField(max_length=200)
    ram_required = models.CharField(max_length=200)
    minimum_network_required = models.CharField(max_length=200)
    maximum_network_required = models.CharField(max_length=200)
    virtual_network_function_instance_type_id = models.CharField(max_length=200)
    cpu_pin = models.CharField(max_length=200)
    cross_socket_pin = models.CharField(max_length=200)

    def __str__(self):
        """Return a human readable representation of the model instance."""
        return "{}".format(self.name)

class virtual_machine_instance_type_id(models.Model):
    
    STATUS_GO = 1
    STATUS_NOGO = 2

    STATUS_CHOICES =(
        (STATUS_GO, _('Ready to deploy')),
        (STATUS_NOGO, _('Not ready to deploy')),
    )

    virtual_machine_instance_type_name = models.CharField(max_length=200)
    management_ip_address = models.CharField(max_length=200)
    image_name = models.CharField(max_length=200)
    image_location = models.CharField(max_length=200)
    configuration_script = models.CharField(max_length=200)
    version_number = models.CharField(max_length=200)
    virtual_machine_type_id = models.CharField(max_length=200)
    minimum_number_of_instances = models.CharField(max_length=200)
    maximum_number_of_instances = models.CharField(max_length=200)
    instantiation_playbook = models.CharField(max_length=200)
    recover_playbook = models.CharField(max_length=200)
    scale_out_playbook = models.CharField(max_length=200)
    scale_in_playbook = models.CharField(max_length=200)

    def __str__(self):
        """Return a human readble representation of the model instance."""
        return "{}".format(self.name)


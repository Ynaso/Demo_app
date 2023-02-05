from rest_framework import serializers
from .models import it_is_fine

class serial_ok(serializers.ModelSerializer):
    class Meta:
        model = it_is_fine
        fields = ('field1_e', 'field2_p')
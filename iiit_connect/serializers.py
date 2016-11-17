from rest_framework import serializers
from .models import EmailInvitation

class EmailInvitationSerializer(serializers.ModelSerializer):

	class Meta :

		model = EmailInvitation
		fields = '__all__'
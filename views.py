from  django.shortcuts import get_object_or_404
from django.shortcuts import render

# Create your views here.
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import EmailInvitation
from .serializers import EmailInvitationSerializer


#list of all invitation list or create new one
#invitation/
class InvitationList(APIView):

	def get(self , request):
		invitation = EmailInvitation.objects.all()
		serializer = EmailInvitationSerializer( invitation , many = True)
		return Response(serializer.data)

	def post(self):
		pass
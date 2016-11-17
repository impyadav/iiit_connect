from  django.shortcuts import get_object_or_404
from django.shortcuts import render

# Create your views here.
from django.core.mail import send_mass_mail
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



def sendMassEmail(request,emailto1,emailto2) :
     msg1 = ('sub1','msg1','201451041@iiitvadodara.ac.in',['pyadav223141@gmail.com'])
     msg2 = ('sub2','msg2','201451041@iiitvadodara.ac.in',['201451011@iiitvadodara.ac.in'])
     res = send_mass_mail((msg1,msg2),fail_silently = False)
     return HttpResponse('%s'%res)
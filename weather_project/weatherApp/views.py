from django.shortcuts import render
import urllib.request
import json
# Create your views here.
def index(request):
    if request.method=="POST":
        city = request.POST['city']
        source = urllib.request.urlopen('http://api.openweathermap.org/data/2.5/weather?q='+ city +'&units=metric&appid=a1084d042c5690e9eb120753a498a3a7').read()
        list_of_data = json.loads(source)
        data = {
            "country_code": str(list_of_data['sys']['country']),
            "coordinate": str(list_of_data['coord']['lon'])+" , "+str(list_of_data['coord']['lat']),
            "temp":str(list_of_data['main']['temp'])+" °C",
            "pressure":str(list_of_data['main']['pressure']),
            "humidity":str(list_of_data['main']['humidity']),
            "main":str(list_of_data['weather'][0]['main']),
            "description":str(list_of_data['weather'][0]['description']),
            "icon":list_of_data['weather'][0]['icon'],
            "city":str(list_of_data['name'])
        }
        print(data)
    else:
        data={}
    return render(request,'weatherApp/index.html',data)
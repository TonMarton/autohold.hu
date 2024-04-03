from django.contrib import admin
from cars.models import Car, Kiemelt_szoveg
import os
from django.conf import settings
from django.core.urlresolvers import reverse
from django.views import generic
from django.views.decorators.http import require_POST
from jfu.http import upload_receive, UploadResponse, JFUResponse
from django.shortcuts import render, redirect
from cars.models import Car, Kiemelt_szoveg
from django.views import generic
import random
from django.core.files.storage import FileSystemStorage
import json
import string
from django.http import JsonResponse
from django.core import serializers

def index(request):
    if request == None:
        query = '0'
    else:
        query = request.GET.get('q')
    if query:
        cars = Car.objects.filter(kiemeltajánlat=False, név__icontains=query)
        specialCars = Car.objects.filter(kiemeltajánlat=True, név__icontains=query)
    else:
        cars = Car.objects.filter(kiemeltajánlat=False)
        specialCars = Car.objects.filter(kiemeltajánlat=True)

    for index,car in enumerate(cars):
        car.hajtás = formatString(str(car.ár))
        if car.image_locations is None:
            print('lul')
        else:
            if type(car.image_locations) == str:
                dataObject = json.loads(car.image_locations)
            else:
                dataObject = car.image_locations
            if dataObject == []:
                print('lul')
            else:
                car.image_locations = dataObject[0]['url']

    for index,car in enumerate(specialCars):
        car.hajtás = formatString(str(car.ár))
        if car.image_locations is None:
            print('lul')
        else:
            if type(car.image_locations) == str:
                dataObject = json.loads(car.image_locations)
            else:
                dataObject = car.image_locations
            if dataObject == []:
                print('lul')
            else:
                car.image_locations = dataObject[0]['url']

    if Kiemelt_szoveg.objects.all()[0]:
        szöveg = Kiemelt_szoveg.objects.all()[0].szöveg

    return render(request, 'cars/includes/car_card.html', {
        'cars': cars,
        'specialCars': specialCars,
        'query': query,
        'kiemelt_szöveg': szöveg,
        })

def impresszum(request):
    return render(request, 'cars/includes/impresszum.html')

def auto(request, pk):
    if Car.objects.filter(pk=pk).exists():
        car = Car.objects.get(pk__iexact=pk)
        price = formatString(str(car.ár))
        if not car.image_locations is None:
            image_locations = json.loads(car.image_locations)
        else:
            image_locations = []
        image_urls = []
        for index, image in enumerate(image_locations):
            image_urls.append(image['url'])
        return render(request, 'cars/includes/details.html', {
            'car': car,
            'image_urls': image_urls,
            'ár': price,
             })
    else:
        return redirect('index')

# 123456789
def formatString(string):
    length = len(string)
    if length > 3:
        newString = formatString(string[:length-3]) + ' ' + string[length-3:]
        return newString
    return string

@require_POST
def upload( request ):
    files = request.FILES.getlist('files[]')
    results = []
    for file in files:
        name = initName(file.name, getFormat(file.name))
        dltName = undotify(name)
        fs = FileSystemStorage(settings.MEDIA_ROOT + "/carinstanceimages/")
        filename = fs.save(name, file)
        dltName = undotify(name)
        results.append({
            'name' : name,
            'size' : file.size,
            'url': settings.MEDIA_URL + "carinstanceimages/" + name,
            'thumbnailUrl': settings.MEDIA_URL + "carinstanceimages/" + name,
            'deleteUrl': reverse('jfu_delete', kwargs = { 'pk': dltName }),
            'deleteType': 'POST',
        })
    return UploadResponse( request, results)

def getCars( request ):
    cars = Car.objects.all()
    if not cars:
        return JSONResponse({'error':'there are no cars on the server'},status=400)
    carObjects = []
    cars = Car.objects.all()
    for car in cars:
        carId = car.pk
        carName = car.név
        carObjects.append({'id': carId, 'name':carName})
    data = {'cars': carObjects}
    json_data = json.dumps(data)
    resp = JsonResponse(json_data,safe=False)
    resp['Access-Control-Allow-Origin'] = '*'
    return resp

# this function should return the form data of the car with the requested id
def carFormData(request, pk):
    if Car.objects.filter(pk=pk).exists():
        values = serializers.serialize('json', Car.objects.filter(pk__iexact=pk))
        resp = JsonResponse( values ,safe=False)
        resp['Access-Control-Allow-Origin'] = '*'
        return resp
    resp2 = JsonResponse(None, safe = False)
    resp2['Access-Control-Allow-Origin'] = '*'
    return resp2

@require_POST
def upload_delete( request, pk ):
    success = True
    fullName = dotify(pk)
    try:
        fs = FileSystemStorage(settings.MEDIA_ROOT + "/carinstanceimages/")
        fs.delete(fullName)
    except Car.DoesNotExist:
        success = False
    return JFUResponse( request, success )

# gets the whole file name and only returns the part starting with the '.', the extension
def getFormat(string):
    for index, c in enumerate(string):
        if c == '.':
            return string[index:]

# does the undotify but backwards
def dotify(string):
    for index,c in enumerate(string):
        if (c == '0'):
            indX = index + 5
            if (string[index:indX] == "0DOT0"):
                return string[:index] + "." + string[indX:]
    return '0'

# returns the same string but with the '.' replaced with '0DOT0' (to be able to pass it into urls)
def undotify(string):
    for index,c in enumerate(string):
        if (c == '.'):
            return string[:index] + "0DOT0" + string[(index+1):]
    return '0'

def randomString():
    name = ''.join(random.choice(string.ascii_uppercase + string.digits) for _ in range(10))
    return name

# creates the name again and again until it is unique, even if it has a very small chance not to be (recursive)
def initName(string, fileType):
    name = randomString() + fileType
    if os.path.exists(settings.MEDIA_ROOT + "/carinstanceimages/" + name):
        return initName(string, fileType)
    return name

from django.contrib import admin
from cars.views import upload, upload_delete
from cars.models import Car, Kiemelt_szoveg
import os
from django.conf import settings
from django.core.urlresolvers import reverse
from django.views import generic
from django.views.decorators.http import require_POST
from jfu.http import upload_receive, UploadResponse, JFUResponse
from django.conf.urls import url
from cars.forms import CarForm

class CarAdmin(admin.ModelAdmin):
    list_display = ['__str__' ,'kiemeltajánlat']
    form = CarForm

    def get_urls(self):
        urls = super(CarAdmin, self).get_urls()
        my_urls = [
            url( r'upload/', upload, name = 'jfu_upload' ),
            url( r'^delete/(?P<pk>\d+)$', upload_delete, name = 'jfu_delete' ),
        ]
        return my_urls + urls

admin.site.register(Kiemelt_szoveg)
admin.site.register(Car, CarAdmin)

from django.conf. urls import url
from .  import views
from cars.views import upload, upload_delete, getCars, carFormData

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^auto/(?P<pk>\d+)$', views.auto, name="auto"),
    url(r'^impresszum$', views.impresszum, name='impresszum'),
    url( r'upload/', upload, name = 'jfu_upload' ),
    url( r'^delete/(?P<pk>\w+)$', upload_delete, name = 'jfu_delete' ),
    url( r'getCars$', getCars, name = 'get_cars' ),
    url( r'getCar/(?P<pk>\w+)$', carFormData, name = 'get_form_data' ),
]


from django.contrib import admin
from django.urls import path
from topper import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path("indices/",views.indices,name='indices'),
    path("globals/",views.globals,name='globals'),
    path("advdec/",views.advdec,name='advdec'),
    path("topmost/",views.topmost,name='topmost'),

    path("",views.home)
]

from django.contrib import admin
from django.urls import path
from topper import views
from topper.news.views import mynews
urlpatterns = [
    path('admin/', admin.site.urls),
    path("",views.home,name='home'),
    path("indices/",views.indices,name='indices'),
    path("globals/",views.globals,name='globals'),
    path("advdec/",views.advdec,name='advdec'),
    path("topmost/",views.topmost,name='topmost'),
    path("news/<int:id>",mynews,name='news'),


    path('excel/',views.csv,name="downloadexcel"),

 



]

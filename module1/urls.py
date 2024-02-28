from django.contrib import admin
from django.urls import path
from .views import *

urlpatterns = [
    # path('admin/', admin.site.urls),
    path('hello/',hello1,name='hello'),
    path('',newhomepage,name='NewHomepage'),
    path('travelpackage/',travelpackage,name='travelpackage'),
    path('p/',print1,name='print1'),
    path('print/',print_to_console,name='print_to_console'),
    path('h/',randomcall,name='randomcall'),
    path('random/',randomlogic,name='randomlogic'),
    path('dat/',getdate1,name='getdate1'),
    path('j/',dattime,name='dattime'),
    path('register/',Register,name='Register'),
    path('Registerpage/',Registerpage,name='Registerpage'),
    path('pie/',pie_chart,name='pie_chart'),
    path('card/',carcards,name='cards'),
    path('weather/',weatherpagecall,name='weatherpagecall'),
    path('weatherlogic/',weatherlogic,name='weatherlogic'),
    path('Feedbackcall/', Feedbackcall, name='Feedbackcall'),
    path('Feedbackform/', Feedbackform, name='Feedbackform'),
    path('login/', login, name='login'),
    path('login1/', login1, name='login1'),
    path('signup/', signup, name='signup'),
    path('signup1/', signup1, name='signup1'),
    path('logout/', logout, name='logout'),
]
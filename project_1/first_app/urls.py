from django.urls import path
# from views import contactfrom
from.import views 

urlpatterns = [
    path("courses/",views.courses),
    path("about/",views.about),
    path("",views.Home),
    


]

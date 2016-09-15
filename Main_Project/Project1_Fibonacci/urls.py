from django.conf.urls import url
from django.conf.urls.static import static

from . import views


urlpatterns = [ 
    #Home
    url(r'^$', views.homepage, name="homepage"),
    url(r'^fibonacci/$', views.fibonacci_response, name="calculate_fibonacci")
]
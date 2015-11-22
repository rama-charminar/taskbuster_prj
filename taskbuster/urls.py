from django.conf.urls import include, url
from taskbuster.views import Rama,rama,List,index

urlpatterns = [
	url(r'^Rama/$', Rama, name='Rama'),
	url(r'^rama/$', rama, name='rama'),
	url(r'^List/$',List,name='List'),
	url(r'^index/$',index,name='index'),
	
]
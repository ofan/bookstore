from django.conf.urls import patterns, include, url
from django.contrib import admin
admin.autodiscover()

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
     url(r'^$', 'bookstore.views.home', name='home'),
	 url(r'^mainpage$', 'bookstore.views.mainpage', name='mainpage'),
   	 url(r'^login$' , 'bookstore.views.login' , name='login'),
	 url(r'^signup$' , 'bookstore.views.signup', name='signup'),
	 url(r'^processLogin$', 'bookstore.views.processLogin' , name='processLogin'),
     url(r'^credentials$' , 'bookstore.views.credentials' , name='credentials'),	
	# url(r'^bookstore/', include('bookstore.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
     #url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls))
)

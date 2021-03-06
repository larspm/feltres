"""feltres URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.9/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.contrib import admin

import resultater.views

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^xml/(?P<år>[0-9]{4})/(?P<klubb>[^/]+)/(?P<skytter>[^/]+)$', resultater.views.stevner_xml, name='stevner-xml'),
    url(r'^xml/(?P<år>[0-9]{4})/(?P<klubb>[^/]+)$',                    resultater.views.stevner_xml, name='stevner-xml'),
    url(r'^xml/(?P<år>[0-9]{4})$',                               resultater.views.stevner_xml, name='stevner-xml'),
    url(r'^xml/$',                                               resultater.views.stevner_xml, name='stevner-xml'),
    url(r'^(?P<stevnenr>[0-9]+).xlsx$',                          resultater.views.stevne_xlsx, name='stevne-xlsx'),
    url(r'^(?P<stevnenr>[0-9]+).xml$',                           resultater.views.stevner_xml, name='stevne-xml'),
    url(r'^(?P<stevnenr>[0-9]+)/$',                              resultater.views.stevne_html, name='stevne-html'),
    url(r'^$',                                                   resultater.views.index)
]

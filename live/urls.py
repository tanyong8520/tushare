"""live URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
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
from django.conf.urls import url, include
from django.contrib import admin

from base import urls as base_urls
from callloans import urls as callloans_urls
from classified import urls as classified_urls
from macroeconomic import urls as macroeconomic_urls
from newsinfo import urls as newsinfo_urls
from reference import urls as reference_urls
from transaction import urls as transaction_urls
from quartz import urls as quartz_urls

urlpatterns = [
    url(r'^base/', include(base_urls)),
    url(r'^callloans/',include(callloans_urls)),
    url(r'^classified/',include(classified_urls)),
    url(r'^macroeconomic/',include(macroeconomic_urls)),
    url(r'^newsinfo/',include(newsinfo_urls)),
    url(r'^reference/',include(reference_urls)),
    url(r'^transaction/',include(transaction_urls)),
    url(r'^admin/', admin.site.urls),
    url(r'^quartz/', include(quartz_urls)),
]

import quartz.jobs
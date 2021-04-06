from django.conf.urls import url
from django.contrib import admin

from . import views
from blog import views as blogviews
from about import views as aboutviews

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^blog/', blogviews.blog),
    url(r'^about/', aboutviews.about),
    url(r'^$', views.index),
]

from django.conf import settings
from django.conf.urls import include, url
from django.conf.urls.static import static
from django.contrib import admin


from .views import (MenuListView,
                    MenuDetailView,
                    #MenuPreOrder,
                    )

urlpatterns = [
    url(r'^$', MenuListView.as_view(), name='menu'),
    url(r'^(?P<pk>\d+)/$', MenuDetailView.as_view(), name='menu_detail'),
    #url(r'^preorder/$', MenuPreOrder, name='preorder'),
]

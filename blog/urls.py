from django.conf.urls import url

from blog import views

app_name = 'blog'

urlpatterns = [

    # /blog/
    url(r'^$', views.IndexView.as_view(), name='index'),

    # blog/product/entry
    url(r'^product/entry/$', views.ProductEntry.as_view(), name='product-entry'),

    # blog/product/2
    url(r'^product/(?P<pk>[0-9]+)/$', views.ProductUpdate.as_view(), name='product-update'),

    # blog/product/(?P<pk>[0-9]+)/delete
    url(r'^album/(?P<pk>[0-9]+)/delete$', views.ProductDelete.as_view(), name='product-delete'),

]
"""atosopdr URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
"""
# Django imports
from django.conf import settings
from django.conf.urls import include, url
from django.conf.urls.static import static
from django.contrib import admin
from django.contrib.auth import views as auth_views

# Views imports
from airbnbatos.views import index, model_form_upload, DocumentsList, export_csv, total_reviews_per_room

urlpatterns = [
    # Examples:
    url(r'^home/', index, name='home'),

    # provide the most basic login/logout functionality
    url(r'^login/$', auth_views.login,
        {'template_name': 'core/login.html'},
        name='core_login'),
    url(r'^logout/$', auth_views.logout, name='core_logout'),

    # urls for functionality
    url(r'^formupload/$', model_form_upload, name='upload_form'),
    url(r'^documents/$', DocumentsList.as_view(), name='documents_list'),
    url(r'^ajax/exportcsv/$', export_csv, name='exportcsv'),
    url(r'^charts/totalreviews$', total_reviews_per_room, name='total_reviews_rooms'),

    # enable the admin interface
    url(r'^admin/', admin.site.urls),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

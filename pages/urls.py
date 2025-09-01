from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('technology/', views.technology, name='technology'),
    path('applications/', views.applications, name='applications'),
    path('partners/', views.partners, name='partners'),
    path('about/', views.about, name='about'),
    path('contact/', views.contact, name='contact'),
    path('privacy/', views.privacy, name='privacy'),
    path('sitemap.xml', views.sitemap_xml, name='sitemap_xml'),
    path('robots.txt', views.robots_txt, name='robots_txt'),
]

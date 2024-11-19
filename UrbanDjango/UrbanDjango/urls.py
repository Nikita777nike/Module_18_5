"""
URL configuration for UrbanDjango project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
#from task2.views import functemplate
from django.views.generic import TemplateView
#from task4.views import home_page, game_page, cart_page
from task5.views import sign_up_by_django , sign_up_by_html
#urlpatterns = [
 #   path('admin/', admin.site.urls),
 #   path('', functemplate),
 #   path('page2/', TemplateView.as_view(template_name='class_template.html'))
  #  ]

'''urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home_page),
    path('page1/', game_page),
    path('page2/', cart_page)
]'''
urlpatterns = [
    path("admin/", admin.site.urls),
    path('', sign_up_by_django),
    path('sing/', sign_up_by_html),
]


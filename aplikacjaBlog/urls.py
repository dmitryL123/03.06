from django.urls import path

from aplikacjaBlog import views

app_name = "aplikacjaBlog"

urlpatterns = [
    path('', views.post_list, name='post_list')
]
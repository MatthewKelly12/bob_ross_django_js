from django.conf.urls import url
from src import views


urlpatterns = [
    url(r'^$', views.index, name='home'),
	url(r'^birthdays/', views.show_birthdays, name='birthdays'),
]
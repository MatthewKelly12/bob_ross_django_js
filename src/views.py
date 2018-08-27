from django.shortcuts import render
from django.http import JsonResponse
from .models import Birthday

def index(request):
	return render(request, 'src/index.html')

def show_birthdays(request):
	print("bday called")
	birthdays = Birthday.objects.all().values()
	bday_list = list(birthdays)
	return JsonResponse(bday_list, safe=False)
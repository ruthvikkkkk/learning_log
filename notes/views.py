from django.shortcuts import render

# Create your views here.

def whatnotes(request):
	return render(request, 'notes/whatnotes.html')
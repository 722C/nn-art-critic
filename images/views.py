from django.shortcuts import render, redirect
from django.http import HttpResponse

from .forms import ImageComparisonForm

# Create your views here.
def default(request):
	form = ImageComparisonForm(request.POST or None)

	if form.is_valid():
		form.save()
		return redirect('default')

	return render(request, 'images/default.html', {'form': form})

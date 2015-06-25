from django.shortcuts import render, render_to_response
from django.http import HttpResponse
from itertools import chain
from django.forms.models import modelformset_factory

from bunker.models import Bunk, UserProfile

def index(request):
	bunks = Bunk.objects.all().order_by('time')	
	context = {'bunks': bunks}
	return render(request, 'bunker/index.html', context)

def personal(request, user_id):
	profile = UserProfile.objects.get(pk=user_id)
	from_bunks = Bunk.objects.filter(from_user=profile.user).order_by('time') 
	to_bunks = Bunk.objects.filter(to_user=profile.user).order_by('time') 
	personal_bunks = list(chain(from_bunks, to_bunks))
	context = {'personal_bunks': personal_bunks, 'profile': profile}
	return render(request, 'bunker/personal.html', context)

def bunkform(request):
	BunkFormSet = modelformset_factory(Bunk)
	if request.method == 'POST':
		formset = BunkFormSet(request.POST, request.FILES)
		if formset.is_valid():
			formset.save()
			return HttpResponse("SUCCESS")
	else:
		formset = BunkFormSet(queryset=Bunk.objects.none())
	return render(request, 'bunker/bunkform.html', {"formset": formset})

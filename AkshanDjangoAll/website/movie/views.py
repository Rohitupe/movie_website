from django.views import generic
from .models import Hindi,Song
#from django.views.generic.edit import CreateView,UpdateView,DeleteView
from django.shortcuts import render,redirect

from django.contrib.auth import authenticate,login
from django.views.generic import View
from .forms import UserForm


class IndexView(generic.ListView):
	template_name='movie/index.html'
	context_object_name='all_movies'
	def get_queryset(self):
		return Hindi.objects.all()

class DetailView(generic.DetailView):
	model=Hindi
	template_name='movie/detail.html'
	context_object_name='movie'

class MovieCreate(generic.CreateView):
	model=Hindi
	fields=["name","actor","actress"]

class UserFormView(View):
	form_class=UserForm
	template_name='movie/registration_form.html'

	def get(self,request):
		form = self.form_class(None)
		return render(request,self.template_name,{'form':form})

	def post(self,request):
		form=self.form_class(request.POST)

		if form.is_valid():
			user=form.save(commit=False)
			username=form.cleaned_data['username']
			password=form.cleaned_data['password']
			user.set_password(password)
			user.save()

			user=authenticate(username=username,password=password)
			if user is not None:
				if user.is_active:
					login(request,user)
					return redirect('movie:index')

		return render(request,self.template_name,{'form':form})
			

			
	

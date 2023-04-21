from django.shortcuts import render, get_object_or_404, HttpResponseRedirect
from django.urls import reverse
from django.contrib.auth.decorators import login_required

#import relative models
from .models import Movie
from .forms import MovieForms

# Create your views here.
def index(request):
    context = {}
    return render(request, 'base.html', context)


@login_required
def create_view(request):
    context = {}
    
    form = MovieForms(request.POST or None)
    
    if form.is_valid():
        movie = form.save(commit=False)
        movie.userid = request.user
        movie.save()
        return HttpResponseRedirect('/list_view')
        
    
    context['form'] = form
    return render(request, 'create_view.html', context)


@login_required
def list_view(request):
    context = {}
    
    context['dataset'] = Movie.objects.filter(userid=request.user)
    
    return render(request, 'list_view.html', context)


@login_required
def detail_view(request, id):
    context = {}
    context['data'] = Movie.objects.get(id=id)
    return render(request, 'detail_view.html', context)


@login_required
def update_view(request, id):
    
    context = {}
    
    obj = get_object_or_404(Movie, id = id)
    # pass the object as an instance in the form
    form = MovieForms(request.POST or None, instance=obj)
    if form.is_valid():
        form.save()
        return HttpResponseRedirect(reverse('detail_view', args=[id]))
    
    #add our form dictionary to our context
    context['form'] = form
    return render(request, 'update_view.html', context)


@login_required
def delete_view(request, id):
    context = {}
    obj = get_object_or_404(Movie, id = id)
    
    if request.method == "POST":
        obj.delete()
        
        return HttpResponseRedirect('/list_view')
    
    return render(request, 'delete_view.html', context)

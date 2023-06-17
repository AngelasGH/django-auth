from django.shortcuts import render, redirect
from django.shortcuts import render, get_object_or_404, HttpResponseRedirect
from django.urls import reverse
from django.contrib.auth.decorators import login_required

# import relative models
from .models import Movie
from .forms import MovieForms

# Create your views here.


def index(request):
    context = {}
    return render(request, 'base.html', context)


@login_required
def create_view(request):
    if request.method == 'POST':
        form = MovieForms(request.POST, request.FILES)
        if form.is_valid():
            movie = form.save(commit=False)
            movie.userid = request.user
            movie.save()
            return HttpResponseRedirect('/list_view')
    else:
        form = MovieForms()

    context = {'form': form}
    return render(request, 'create_view.html', context)


@login_required
def list_view(request):

    # An empty dictionary named "context" is created to store data
    # that will be passed to the template.
    context = {}

    # The dictionary is populated with data retrieved from the database using the "Movie.objects.filter()" method.
    # This method filters the movies based on the current user's ID, which is obtained from the "request" object.
    # The resulting queryset is then stored in the dictionary with the key "dataset".
    context['dataset'] = Movie.objects.filter(userid=request.user)

    return render(request, 'list_view.html', context)


@login_required
def detail_view(request, id):

    # An empty dictionary named "context" is created to store data
    # that will be passed to the template.
    context = {}

    # The dictionary is populated with data retrieved from the database using the "Movie.objects.get()" method.
    # This method retrieves a single movie instance based on the "id" parameter passed to the detail_view.
    # The retrieved movie instance is then stored in the dictionary with the key "data".
    context['data'] = Movie.objects.get(id=id)

    return render(request, 'detail_view.html', context)


@login_required
def update_view(request, id):
    # An empty dictionary named "context" is created to store data that will be passed to the template.
    context = {}

    # The "get_object_or_404()" function is called to retrieve a movie instance with the given "id" parameter.
    # If no such instance exists, a 404 error page is displayed. The retrieved movie instance is stored in the "obj" variable.
    obj = get_object_or_404(Movie, id=id)

    if request.method == 'POST':
        # A new instance of the "MovieForms" form is created using the retrieved movie instance as the value of the "instance" parameter.
        # This will pre-populate the form fields with the existing data of the movie being updated.
        form = MovieForms(request.POST, request.FILES, instance=obj)

        # The "is_valid()" method is called on the form object to check if the submitted form data is valid.
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('detail_view', args=[id]))
    else:
        form = MovieForms(instance=obj)

    # add our form dictionary to our context
    context['form'] = form
    return render(request, 'update_view.html', context)


@login_required
def delete_view(request, id):
    # Retrieve the movie instance with the given id or show a 404 error page if it doesn't exist
    obj = get_object_or_404(Movie, id=id)

    if request.method == "POST":
        # Handle the confirmation of the delete action
        obj.delete()
        return redirect('/list_view')

    # Render the delete confirmation template
    context = {'object': obj}
    return render(request, 'delete_view.html', context)

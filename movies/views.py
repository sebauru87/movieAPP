from django.shortcuts import render, redirect

from .models import Movie
# Create your views here.

def home_page(request):
    user_query = str(request.GET.get('query', ''))
    search_result = Movie.objects.filter(name__icontains=user_query)
    stuff_for_frontend = {'search_result': search_result}
    return render(request, 'movies/movies_stuff.html', stuff_for_frontend)

def create(request):
    if request.method == 'POST':
        data = {
            'name' : request.POST.get('name'),
            'picture' : request.POST.get('picture'),
            'rating' : int(request.POST.get('rating')),
            'notes' : request.POST.get('notes')
        }
        try:
            response = Movie.objects.create(
                name=data.get('name'),
                picture=data.get('picture'),
                rating=data.get('rating'),
                notes=data.get('notes')
            )
        except Exception as e:
            print(e)
            pass

    return redirect('/')

def edit(request, movie_id):
    if request.method == 'POST':
        data = {
            'name' : request.POST.get('name'),
            'picture' : request.POST.get('picture'),
            'rating' : int(request.POST.get('rating')),
            'notes' : request.POST.get('notes')
        }
        try:
            movie_object = Movie.objects.get(id=movie_id)
            movie_object.name = data.get('name')
            movie_object.picture = data.get('picture')
            movie_object.rating = data.get('rating')
            movie_object.notes = data.get('notes')
            movie_object.save()
        except Exception as e:
            print(e)
            pass
    return redirect('/')

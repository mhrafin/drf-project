# from django.http import JsonResponse
# from django.shortcuts import render
# from watchlist_app.models import Movie


# # Create your views here.
# def movie_list(request):
#     movies = Movie.objects.all()

#     data = {"movies": list(movies.values())}

#     return JsonResponse(data=data)


# def movie_detail(request, pk):
#     movie = Movie.objects.filter(pk=pk).values()

#     data = {'movie': list(movie)}

#     return JsonResponse(data=data)
from rest_framework.exceptions import ValidationError
from django.shortcuts import get_object_or_404
from rest_framework import status

# from rest_framework.decorators import api_view
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import mixins, generics
from rest_framework import viewsets

from watchlist_app.api.permissions import IsAdminOrReadOnly, ReviewOwnerOrReadOnly
from watchlist_app.api.serializers import (
    ReviewSerializer,
    StreamPlatformSerializer,
    WatchListSerializer,
)
from watchlist_app.models import Review, StreamPlatform, WatchList


class ReviewCreate(generics.CreateAPIView):
    serializer_class = ReviewSerializer
    def get_queryset(self):
        return Review.objects.all

    def perform_create(self, serializer):
        pk = self.kwargs.get("pk")
        queryset = WatchList.objects.get(pk=pk)

        user = self.request.user

        if Review.objects.filter(watchlist=queryset, review_user=user).exists():
            raise ValidationError("You already reviewed this watch!", code=status.HTTP_403_FORBIDDEN)

        serializer.save(watchlist=queryset, review_user=user)


class ReviewList(generics.ListAPIView):
    # queryset = Review.objects.all()
    serializer_class = ReviewSerializer

    def get_queryset(self):
        pk = self.kwargs.get("pk")
        return Review.objects.filter(watchlist=pk)


class ReviewDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Review.objects.all()
    serializer_class = ReviewSerializer
    permission_classes = [ReviewOwnerOrReadOnly]


class StreamPlatformViewSet(viewsets.ModelViewSet):
    queryset = StreamPlatform.objects.prefetch_related("watchlist_set").all()    
    serializer_class = StreamPlatformSerializer
        


# class StreamPlatformList(APIView):
#     def get(self, request):
#         stream_platforms = StreamPlatform.objects.all()
#         serializer = StreamPlatformSerializer(stream_platforms, many=True)
#         return Response(serializer.data)

#     def post(self, request):
#         serializer = StreamPlatformSerializer(data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data)
#         else:
#             return Response(serializer.errors)


# class StreamPlatformDetail(APIView):
#     def get_object(self, pk):
#         return get_object_or_404(StreamPlatform, pk=pk)

#     def get(self, request, pk):
#         stream_platform = self.get_object(pk)
#         serializer = StreamPlatformSerializer(stream_platform)
#         return Response(serializer.data)

#     def put(self, request, pk):
#         stream_platform = self.get_object(pk)
#         serializer = StreamPlatformSerializer(stream_platform, data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data)
#         else:
#             return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

#     def delete(self, pk):
#         stream_platform = self.get_object(pk)
#         stream_platform.delete()
#         return Response(status=status.HTTP_204_NO_CONTENT)


class WatchListAll(APIView):
    serializer_class = WatchListSerializer

    def get(self, request):
        movies = WatchList.objects.all()
        serializer = WatchListSerializer(movies, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = WatchListSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors)


class WatchListDetail(APIView):
    serializer_class = WatchListSerializer

    def get(self, request, pk):
        try:
            movie = WatchList.objects.get(pk=pk)
        except WatchList.DoesNotExist:
            return Response(
                {"error": "Movie does not exist"}, status=status.HTTP_404_NOT_FOUND
            )
        serializer = WatchListSerializer(movie)
        return Response(serializer.data)

    def put(self, request, pk):
        movie = WatchList.objects.get(pk=pk)
        serializer = WatchListSerializer(movie, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        movie = WatchList.objects.get(pk=pk)
        movie.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


# @extend_schema(
#     request=MovieSerializer,
#     responses={200: MovieSerializer},
# )
# @api_view(["GET", "POST"])
# def movie_list(request):
#     if request.method == "GET":
#         movies = Movie.objects.all()
#         serializer = MovieSerializer(movies, many=True)
#         return Response(serializer.data)
#     if request.method == "POST":
#         serializer = MovieSerializer(data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data)


# @extend_schema(
#     request=MovieSerializer,
#     responses={200: MovieSerializer},
# )
# @api_view(["GET", "PUT", "DELETE"])
# def movie_detail(request, pk):
#     if request.method == "GET":
#         try:
#             movie = Movie.objects.get(pk=pk)
#         except Movie.DoesNotExist:
#             return Response(
#                 {"error": "Movie does not exist"}, status=status.HTTP_404_NOT_FOUND
#             )
#         serializer = MovieSerializer(movie)
#         return Response(serializer.data)

#     if request.method == "PUT":
#         movie = Movie.objects.get(pk=pk)
#         serializer = MovieSerializer(movie, data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data)
#         else:
#             return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

#     if request.method == "DELETE":
#         movie = Movie.objects.get(pk=pk)
#         movie.delete()
#         return Response(status=status.HTTP_204_NO_CONTENT)

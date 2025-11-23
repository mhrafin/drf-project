from django.urls import path
from watchlist_app.api.views import *

urlpatterns = [
    # path('list/', movie_list, name="movie-list"),
    # path('<int:pk>', movie_detail, name="movie-detail")
    path("", WatchListAll.as_view(), name="watch-list"),
    path("<int:pk>", WatchListDetail.as_view(), name="watch-list-detail"),
    path(
        "stream-platform/",
        StreamPlatformList.as_view(),
        name="stream-platform-list",
    ),
    path(
        "stream-platform/<int:pk>",
        StreamPlatformDetail.as_view(),
        name="stream-platform-detail",
    ),
    # path('stream-platform/<int:pk>')
]

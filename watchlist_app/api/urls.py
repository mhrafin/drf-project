from django.urls import path
from watchlist_app.api.views import *
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r'stream-platform', StreamPlatformViewSet)

urlpatterns = [
    # path('list/', movie_list, name="movie-list"),
    # path('<int:pk>', movie_detail, name="movie-detail")
    path("list/", WatchListAll.as_view(), name="watch-list"),
    path("<int:pk>/", WatchListDetail.as_view(), name="watch-list-detail"),
    # path(
    #     "stream-platform/",
    #     StreamPlatformList.as_view(),
    #     name="stream-platform-list",
    # ),
    # path(
    #     "stream-platform/<int:pk>",
    #     StreamPlatformDetail.as_view(),
    #     name="stream-platform-detail",
    # ),
    # path("review-list/", ReviewList.as_view(), name="review-list"),
    # path("review/<int:pk>", ReviewDetail.as_view(), name="review-detail"),
    path("<int:pk>/review-list/", ReviewList.as_view(), name="review-list"),
    path("<int:pk>/review-create/", ReviewCreate.as_view(), name="review-create"),
    path("review/<int:pk>/", ReviewDetail.as_view(), name="review-detail"),
]

urlpatterns += router.urls
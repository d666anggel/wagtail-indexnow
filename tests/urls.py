from django.urls import include, path

urlpatterns = [
    path("", include("wagtail_indexnow.urls")),
]

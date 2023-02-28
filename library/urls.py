from django.urls import path
from rest_framework import routers

from library import views

# Register router for DRF urls
router = routers.SimpleRouter()
router.register(r"author", views.AuthorAllView),
router.register(r"books", views.BooksAllView),
router.register(r"reader", views.ReaderAllView),

urlpatterns = [
] + router.urls

urlpatterns += router.urls

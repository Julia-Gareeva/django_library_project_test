from rest_framework import routers

from library import views

# Register router for DRF urls
router = routers.SimpleRouter()
router.register(r"author", views.AuthorView),
router.register(r"books", views.BooksView),
router.register(r"reader", views.ReaderView),

urlpatterns = [
] + router.urls

urlpatterns += router.urls

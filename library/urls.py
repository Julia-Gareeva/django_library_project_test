from rest_framework import routers
from django.urls import path

from library import views
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

# Register router for DRF urls
router = routers.SimpleRouter()
router.register(r"author", views.AuthorView),
router.register(r"books", views.BooksView),
router.register(r"reader", views.ReaderView),

urlpatterns = [
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
] + router.urls

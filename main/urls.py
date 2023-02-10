from django.urls import path
from .views import BookListCreateReadAPIView

urlpatterns = [
    path('', BookListCreateReadAPIView.as_view())]
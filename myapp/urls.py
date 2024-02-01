
from django.urls import path

from myapp.views import BookView

urlpatterns = [
    path('book', BookView.as_view()),
]

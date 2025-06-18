from django.urls import path
from . import views


urlpatterns = [
    path("books/",views.BookListView.as_view()),

    path("greet/<name>/", views.greet),

]
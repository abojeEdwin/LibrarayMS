from django.urls import path
from . import views


urlpatterns = [
    path("books/",views.BookListView.as_view()),
    path("authors/",views.add_author, name="add_author"),

    path("get/authors/",views.get_authors, name="get_authors"),

    path("authors/<int:pk>/", views.update_author, name="update_author"),
    path("delete/authors/<int:pk>", views.delete_author, name="delete_author"),

    path("greet/<name>/", views.greet),

]
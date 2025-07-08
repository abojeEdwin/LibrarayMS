from django.urls import path, include
from rest_framework_nested import routers
from . import views
from .views import BookImageViewSets, BookViewSets

router = routers.DefaultRouter()
router.register('books', views.BookViewSets, 'books')
router.register('images', BookImageViewSets, 'book-images')
book_image_router = routers.NestedDefaultRouter(router, 'books', lookup='book')

book_image_router.register("images", BookImageViewSets, 'image-detail')

urlpatterns = [
            # path("books_book/",views.BookListView.as_view()),
            # path("authors/",views.add_author, name="add_author"),
            # path("get/authors/",views.get_authors, name="get_authors"),
            # path("authors/<int:pk>/", views.update_author, name="update_author"),
            # path("delete/authors/<int:pk>", views.delete_author, name="delete_author"),
            path('',include(router.urls)),
            path('',include(book_image_router.urls)),

            path("authors/" , views.AddAuthorView.as_view(), name = "add_author"),
            path("authors/<int:pk>", views.GetUpdateDeleteAuthorView.as_view(),name='get_update_and_delete'),
            #
            path("images/<int:pk>", views.image_detail, name="images-detail"),

            path("borrow-books/<int:pk>", views.borrow_book, name="borrow-book"),

]

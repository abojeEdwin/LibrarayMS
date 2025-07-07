from django.urls import path, include
from . import views
from .views import BookImageViewSets, BookViewSets
from rest_framework_nested import routers


#
router = routers.DefaultRouter()

router.register('books', BookViewSets, 'books')

book_image_router = routers.NestedSimpleRouter(router, 'books', lookup='book')
router.register('books', views.BookViewSets, 'books')

router.register('images', views.BookImageViewSets, 'book-image')

# book_image_router = router.NestedDefaultRouter(router,'books',lookup='book')
#
book_image_router.register("images", BookImageViewSets, 'book-images')

urlpatterns = [
            path("books/",views.BookListView.as_view()),
            # path("authors/",views.add_author, name="add_author"),

            # path("get/authors/",views.get_authors, name="get_authors"),

            # path("authors/<int:pk>/", views.update_author, name="update_author"),
            # path("delete/authors/<int:pk>", views.delete_author, name="delete_author"),

            path('',include(router.urls)),

            path('',include(book_image_router.urls)),

            path("authors/" , views.AddAuthorView.as_view(), name = "add_author"),
            path("authors/<int:pk>", views.GetUpdateDeleteAuthorView.as_view()),
            #
            path("images/<int:pk>", views.image_detail, name="image-detail"),

            path("borrow-books/<int:pk>", views.borrow_book, name="borrow-book"),


            # path("greet/<name>/", views.greet),

]

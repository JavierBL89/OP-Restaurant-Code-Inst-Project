from . import views
from django.urls import path

urlpatterns = [
    path ('', views.HomePage.as_view(), name='home'),
    # path ('book_table', views.BookTable.as_view(), name='book_table')
]
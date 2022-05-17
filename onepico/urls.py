from . import views
from django.urls import path

urlpatterns = [
    path ('', views.HomePage.as_view(), name='home'),
    path ('cancelation', views.BookingCancelation.as_view(), name='cancelation'),
    # path ('book_table', views.BookTable.as_view(), name='book_table')
]
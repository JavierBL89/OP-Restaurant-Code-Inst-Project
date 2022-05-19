from . import views
from django.urls import path

urlpatterns = [
    path ('', views.HomePage.as_view(), name='home'),
    path ('cancelation', views.BookingSearch.as_view(), name='booking_search'),
    path ('booking canceled', views.BookingCancelation.as_view(), name='cancel_booking'),
    # path ('book_table', views.BookTable.as_view(), name='book_table')
]
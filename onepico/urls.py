from . import views
from django.urls import path

urlpatterns = [
    path ('', views.HomePage.as_view(), name='home'),
    path ('cancelations', views.BookingSearch.as_view(), name='booking_search'),
    path ('cancel booking/<int:pk>', views.BookingCancelation.as_view(), name='cancel_booking'),
    path ('cancelation confirmation', views.CancelationConfirmation.as_view(), name='cancelation_confirmation'),
    # path ('book_table', views.BookTable.as_view(), name='book_table')  
]
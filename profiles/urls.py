from . import views
from django.urls import path

urlpatterns = [
    # path ('manage_bookings/', views.manage_bookings.as_view(), name='manage_bookings'),
    path ('profile/', views.Profile.as_view(), name='profile'),
    path ('delete_profile/<int:user_id>/', views.delete_profile, name='delete_profile'),
]
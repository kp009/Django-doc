from django.urls import path
from .views import home  # Ensure this view exists

urlpatterns = [
    path('', home, name='home'),  # Make sure this is defined
]

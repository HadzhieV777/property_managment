from django.urls import path

from .views import PropertyListAndCreateView, PropertyDetailsAndUpdateView

urlpatterns = (
    path('', PropertyListAndCreateView.as_view(), name='api list or create property'),
    path('<int:pk>/', PropertyDetailsAndUpdateView.as_view(), name='api details or update property')
)

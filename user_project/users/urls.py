from django.urls import path
from .views import UploadCSVAPIView

urlpatterns = [
    path('upload-csv/', UploadCSVAPIView.as_view(), name='upload-csv'),
]

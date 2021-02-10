from django.urls import path
from .views import JobOfferList, JobOfferDetail

urlpatterns = [
    path("jobs", JobOfferList.as_view()),
    path("jobs/<int:pk>", JobOfferDetail.as_view()),
]

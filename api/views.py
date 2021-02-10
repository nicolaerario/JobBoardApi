from rest_framework import generics
from jobs.models import JobOffer
from .serializers import JobOfferSerializer


class JobOfferList(generics.ListCreateAPIView):
    queryset = JobOffer.objects.all()
    serializer_class = JobOfferSerializer


class JobOfferDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = JobOffer.objects.all()
    serializer_class = JobOfferSerializer

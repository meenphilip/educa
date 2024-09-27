from rest_framework import generics
from courses.models import Subject
from courses.api.serializers import SubjectSerializer


# list subjects
class SubjectListView(generics.ListAPIView):
    queryset = Subject.objects.all()
    serializer_class = SubjectSerializer


# Detail of a single subject
class SubjectDetailView(generics.RetrieveAPIView):
    queryset = Subject.objects.all()
    serializer_class = SubjectSerializer

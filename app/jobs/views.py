from django.shortcuts import render

from .models import Job
from .serializers import JobSerializer

from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
# Create your views here.


class ApplyJobView(APIView):
    """
    List all snippets, or create a new snippet.
    """

    def get(self, request, format=None):
        snippets = Job.objects.all()
        serializer = JobSerializer(snippets, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = JobSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

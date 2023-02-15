from django.shortcuts import render

from rest_framework.views import APIView
from . models import *
from rest_framework.response import Response
from . serializer import *

# Create your views here.

class CourseView(APIView):
    serializer_class = CourseSerializer

    def get(self, request):
        #courses= [{"id": course.id, "name": course.name, "detail": course.detail}
        #          for course in Course.objects.all()]
        #return Response(courses)

        courses = Course.objects.all()
        serializer = CourseSerializer(courses, many=True)

        return Response(serializer.data)

    def post(self, request):
        serializer = CourseSerializer(data=request.data)
        if (serializer.is_valid(raise_exception=True)):
                serializer.save()
                return Response(serializer.data)

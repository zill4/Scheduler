from django.shortcuts import render

from scheduler.models import Schedule
from rest_framework import generics
from rest_framework.response import Response
from rest_framework.reverse import reverse
 
from scheduler.serializer import ScheduleSerializer
 
 
class ScheduleList(generics.ListCreateAPIView):
    queryset = Schedule.objects.all()
    serializer_class = ScheduleSerializer
 
    def perform_create(self, serializer):
        serializer.save(user=self.request.user)
 
 
class ScheduleDetail(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = ScheduleSerializer
 
    def get_queryset(self):
        return Schedule.objects.all().filter(user=self.request.user)
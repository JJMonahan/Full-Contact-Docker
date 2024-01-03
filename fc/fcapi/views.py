from django.shortcuts import render
from rest_framework.response import Response
from rest_framework import viewsets
from .models import Contact, Note, Role, Company, Job, Log
from .serializers import (
    ContactSerializer,
    NoteSerializer,
    RoleSerializer,
    CompanySerializer,
    JobSerializer,
    LogSerializer,
)

class ContactViewSet(viewsets.ModelViewSet):
    queryset = Contact.objects.all().order_by('lname','fname')
    serializer_class = ContactSerializer

class NoteViewSet(viewsets.ModelViewSet):
    queryset = Note.objects.all()
    serializer_class = NoteSerializer

class RoleViewSet(viewsets.ModelViewSet):
    queryset = Role.objects.all()
    serializer_class = RoleSerializer

class CompanyViewSet(viewsets.ModelViewSet):
    queryset = Company.objects.all()
    serializer_class = CompanySerializer

class JobViewSet(viewsets.ModelViewSet):
    queryset = Job.objects.all()
    serializer_class = JobSerializer

class LogViewSet(viewsets.ModelViewSet):
    queryset = Log.objects.all()
    serializer_class = LogSerializer



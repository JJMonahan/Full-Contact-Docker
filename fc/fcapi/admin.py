from django.contrib import admin
from django import forms
from .models import Contact, Note, Role, Company, Job, Log

# Register your models with the admin site
@admin.register(Contact)
class ContactAdmin(admin.ModelAdmin):
    list_display = ('lname', 'fname', 'email', 'phone', 'created', 'updated')

@admin.register(Note)
class NoteAdmin(admin.ModelAdmin):
    list_display = ('created', 'last_update', 'content')

@admin.register(Role)
class RoleAdmin(admin.ModelAdmin):
    list_display = ('name','company')

@admin.register(Company)
class CompanyAdmin(admin.ModelAdmin):
    list_display = ('name', 'address', 'description', 'url', 'mapurl', 'created', 'updated')

@admin.register(Job)
class JobAdmin(admin.ModelAdmin):
    list_display = ('company', 'title', 'url', 'created', 'updated')

@admin.register(Log)
class LogAdmin(admin.ModelAdmin):
    list_display = ('created', 'last_update', 'content')



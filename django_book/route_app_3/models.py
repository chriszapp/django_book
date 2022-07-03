from tabnanny import verbose
from django.db import models

class UserProfile(models.Model):

    name = models.CharField(max_length = 50, verbose_name = 'Name')
    login = models.CharField(max_length = 25, verbose_name = 'Login')
    password = models.CharField(max_length = 100, verbose_name = 'Password')
    phone = models.CharField(max_length = 20, verbose_name = 'Phone Number')
    born_date = models.DateField(verbose_name = 'Born Date', null = True, default = None, blank = True)
    last_connection = models.DateTimeField(verbose_name = 'Date of the Last Connection', null = True, default = None, blank = True)
    email = models.EmailField(verbose_name = 'Email')
    years_seniority = models.IntegerField(verbose_name = 'Seniority', default = 0)
    date_created = models.DateField(verbose_name = 'Date of Birthday', auto_now_add = True)

class Project(models.Model):
    title = models.CharField(max_length = 50, verbose_name = 'Title')
    description = models.CharField(max_length = 100, verbose_name = 'Description')
    client_name = models.CharField(max_length = 1000, verbose_name = 'Client name')

class Task(models.Model):
    title = models.CharField(max_length = 50, verbose_name = 'Title')
    description = models.CharField(max_length = 1000, verbose_name = 'Description')
    time_elapsed = models.IntegerField(verbose_name = "Elapsed Time", null = True, default = None, blank = True)
    importance = models.IntegerField(verbose_name = 'Importance')
    project = models.ForeignKey(Project, on_delete=models.CASCADE, verbose_name = 'Project', null = True, default = None, blank = True, )
    app_user = models.ForeignKey(UserProfile, on_delete=models.CASCADE, verbose_name = 'User')

class Supervisor(UserProfile):
    specialization = models.CharField(max_length = 50, verbose_name = 'Specialization')

class Developer(UserProfile):
    supervisor_id = models.ForeignKey(Supervisor, on_delete=models.CASCADE, verbose_name = 'Supervisor')
from django.db import models

# Create your models here.

#class Member(models.Model):
    #firstname = models.CharField(max_length=255)
    #lastname = models.CharField(max_length=255)
    #email = models.EmailField(blank=True, null=True)
    #date_of_birth = models.DateField(blank=True, null=True)
    #phone_number = models.CharField(max_length=20, blank=True, null=True)
    #address = models.CharField(max_length=255, blank=True, null=True)
    #city = models.CharField(max_length=100, blank=True, null=True)
    #state = models.CharField(max_length=100, blank=True, null=True)
    #postal_code = models.CharField(max_length=20, blank=True, null=True)
    #joining_date = models.DateField(blank=True, null=True)
    #membership_type = models.CharField(max_length=50, blank=True, null=True)
    #membership_status = models.CharField(max_length=50, blank=True, null=True)

class Applicant(models.Model):
    firstname = models.CharField(max_length=255)
    lastname = models.CharField(max_length=255)
    email = models.EmailField(blank=True, null=True)
    date_of_birth = models.DateField(blank=True, null=True)
    phone_number = models.CharField(max_length=20, blank=True, null=True)
    address = models.CharField(max_length=255, blank=True, null=True)
    city = models.CharField(max_length=100, blank=True, null=True)
    state = models.CharField(max_length=100, blank=True, null=True)
    postal_code = models.CharField(max_length=20, blank=True, null=True)
    joining_date = models.DateField(blank=True, null=True)
    membership_type = models.CharField(max_length=50, blank=True, null=True)
    membership_status = models.CharField(max_length=50, blank=True, null=True)
    employment_status = models.CharField(max_length=50, blank=True, null=True, choices=(('Pending', 'Pending'), ('Approved', 'Approved'), ('Rejected', 'Rejected')))
    years_of_experience = models.PositiveIntegerField(blank=True, null=True)
    education_level = models.CharField(max_length=100, blank=True, null=True)

class PromotedEmployee(models.Model):
    firstname = models.CharField(max_length=255)
    lastname = models.CharField(max_length=255)
    email = models.EmailField(blank=True, null=True)
    
    def __str__(self):
        return self.firstname, self.lastname, self.email

class Task(models.Model):
    taskname = models.CharField(max_length=200, null=False, blank=False)
    taskdescription = models.CharField(max_length=200, null=False, blank=False)
    date_of_submission = models.DateField(blank=True, null=True)

    def __str__(self):
        return self.taskname

class product(models.Model):
    name = models.CharField(max_length=255)
    phone_number = models.CharField(max_length=20, blank=True, null=True)
    date_of_issue = models.DateField(blank=True, null=True)
    
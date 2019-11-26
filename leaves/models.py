from django.db import models
from django.core.validators import RegexValidator
from pim.models import Personal_details
# Create your models here.

class Leavestructure(models.Model):
    alphanumeric = RegexValidator(r'^[0-9a-zA-Z]*$', 'Only alphanumeric characters are allowed.')
    shortname = models.CharField(max_length=3,validators=[alphanumeric])
    leavestructure = models.CharField(max_length=50,validators=[alphanumeric])
    leavedescription = models.CharField(max_length=100)
    experincefrom = models.IntegerField()
    experienceto = models.IntegerField()
    
    def __str__(self):
       return str(self.leavestructure)

class Leavetype(models.Model):
    leavetype = models.CharField(max_length=50)
    shortname = models.CharField(max_length=3)
    leavedescription = models.CharField(max_length=100)
    
    def __str__(self):
       return self.leavetype

class Linktoleavetype(models.Model):
    leave_structure = models.ForeignKey(Leavestructure,on_delete = models.CASCADE)
    leave_type = models.ForeignKey(Leavetype,on_delete = models.CASCADE)
    numberOfLeaves = models.SmallIntegerField(default=1,blank = False)

class AssignLeaveStructure(models.Model):
    empid = models.ForeignKey(Personal_details,on_delete = models.CASCADE)
    leave_structure = models.ForeignKey(Leavestructure,on_delete = models.CASCADE)
    fromDate = models.DateField(blank = False)
    toDate = models.DateField(blank = False)
    updatedDate = models.DateTimeField(blank = False)
    status = models.BooleanField(default=True)

class Holidays(models.Model):
    holidayname = models.CharField(max_length=50)
    holidayDate = models.DateField(blank = False)

    def __str__(self):
       return self.holidayname

<<<<<<< HEAD
class Upload_list(models.Model):
    document = models.FileField(upload_to='documents/',blank=True,null=False)
=======
class LeaveDetails(models.Model):
    employee = models.ForeignKey(Personal_details,on_delete = models.CASCADE)
    Fromdate = models.DateField(blank=False)
    Todate = models.DateField(blank=False)
    leave_type = models.ForeignKey(Leavetype,on_delete = models.CASCADE)
    NumberOfLeaves = models.SmallIntegerField(default=1,blank=False)
    AppliedDate = models.DateField(blank=False)
    Status = models.SmallIntegerField(default=1,blank=False)
    Reason = models.CharField(max_length=100,blank=True)
    FullorHalfday = models.SmallIntegerField(default=1,blank=False)
>>>>>>> 2b97f0d9dd5a3066a0ddb4c48d81d4d047367f7a

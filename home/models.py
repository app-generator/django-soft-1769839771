# -*- encoding: utf-8 -*-
"""
Copyright (c) 2019 - present AppSeed.us
"""

from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.utils.translation import gettext_lazy as _

# Create your models here.

class UserProfile(models.Model):

    user = models.OneToOneField(User, on_delete=models.CASCADE)

    #__PROFILE_FIELDS__

    #__PROFILE_FIELDS__END

    def __str__(self):
        return self.user.username
    
    class Meta:
        verbose_name        = _("UserProfile")
        verbose_name_plural = _("UserProfile")

#__MODELS__
class Student(models.Model):

    #__Student_FIELDS__
    first_name = models.CharField(max_length=255, null=True, blank=True)
    last_name = models.CharField(max_length=255, null=True, blank=True)
    enrollment_number = models.CharField(max_length=255, null=True, blank=True)
    date_of_birth = models.DateTimeField(blank=True, null=True, default=timezone.now)
    role = models.CharField(max_length=255, null=True, blank=True)
    username = models.CharField(max_length=255, null=True, blank=True)
    email = models.CharField(max_length=255, null=True, blank=True)
    password = models.CharField(max_length=255, null=True, blank=True)

    #__Student_FIELDS__END

    class Meta:
        verbose_name        = _("Student")
        verbose_name_plural = _("Student")


class Course(models.Model):

    #__Course_FIELDS__
    name = models.CharField(max_length=255, null=True, blank=True)
    code = models.CharField(max_length=255, null=True, blank=True)
    description = models.TextField(max_length=255, null=True, blank=True)

    #__Course_FIELDS__END

    class Meta:
        verbose_name        = _("Course")
        verbose_name_plural = _("Course")


class Enrollment(models.Model):

    #__Enrollment_FIELDS__
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    enrollment_date = models.DateTimeField(blank=True, null=True, default=timezone.now)

    #__Enrollment_FIELDS__END

    class Meta:
        verbose_name        = _("Enrollment")
        verbose_name_plural = _("Enrollment")


class Result(models.Model):

    #__Result_FIELDS__
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    marks = models.TextField(max_length=255, null=True, blank=True)

    #__Result_FIELDS__END

    class Meta:
        verbose_name        = _("Result")
        verbose_name_plural = _("Result")



#__MODELS__END

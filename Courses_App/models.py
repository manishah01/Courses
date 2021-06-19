from django.db import models
class CourseManager(models.Manager):
    def basic_validator(self, postData):
        errors = {}
        if len(postData['name']) < 5:
            errors['name'] = "COURSE NAME MUST BE ATLEAST 5 CHARACTERS"
        if len(postData['description']) < 10:
            errors['description'] = "DESCRIPTION MUST BE AT LEAST 10 CHARACTERS"
        return errors

class Course(models.Model):
    name = models.CharField(max_length=255)
    description = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    objects = CourseManager()
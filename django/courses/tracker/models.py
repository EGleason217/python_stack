from django.db import models

class CourseManager(models.Manager):
    def validate(self, form):
        errors = {}
        if len(form['name']) < 5:
            errors['name'] = 'Name field should be at least 5 characters'
        if len(form['description']) < 15:
            errors['description'] = 'Description field should be at least 15 characters'
        return errors

class CommentManager(models.Manager):
    def validator(self,postData):
        errors = {}
        if len(postData['content']) < 5:
            errors['content'] = "Comment must be at least 5 characters"
        return errors

class Courses(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    objects = CourseManager()

class Comment(models.Model):
    content = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    course = models.ForeignKey(Courses, related_name="has_comments",on_delete=models.CASCADE)

    objects = CommentManager()
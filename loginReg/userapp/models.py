from django.db import models
import re

class UserManager(models.Manager):
    def validate(self, form):
        errors = {}
        EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')
        if len(form['fname']) < 2:
            errors['fname'] = 'First Name field should be at least 2 characters'
        if len(form['lname']) < 2:
            errors['lname'] = 'Last Name field should be at least 2 characters'
        if not EMAIL_REGEX.match(form['email']):
            errors['email'] = "Email must be a valid format!"
        if len (form['password']) < 8:
            errors['password'] = "Password must be at least 8 characters!!"
        if form['password'] != form['conf_password']:
            errors ['conf_password'] = "Passwords do not match"
        return errors

class User(models.Model):
    fname = models.CharField(max_length=45)
    lname = models.CharField(max_length=45)
    email = models.EmailField()
    password = models.CharField(max_length=155)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    objects = UserManager()

class MessageManager(models.Manager):
    def validator(self, form):
        errors = {}
        if len(form ['content']) < 5:
            errors['length'] = "Message must be at least 5 characters!"
        return errors

class Message(models.Model):
    owner = models.ForeignKey(User, related_name="poster", on_delete=models.CASCADE)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    objects = MessageManager()

class CommentManager(models.Manager):
    def validator(self, form):
        errors ={}
        if len(form ['content']) < 5:
            errors['length'] = "Message must be at least 5 characters!"
        return errors

class Comment(models.Model):
    message = models.ForeignKey(Message,related_name="comments",on_delete=models.CASCADE)
    poster = models.ForeignKey(User, related_name="comments", on_delete=models.CASCADE)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    objects = CommentManager()
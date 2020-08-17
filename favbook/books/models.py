from django.db import models
import re

class UserManager(models.Manager):
    def validate(self, postData):
        errors = {}
        EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')
        if len(postData['fname']) < 2:
            errors['fname'] = 'First Name field should be at least 2 characters'
        if len(postData['lname']) < 2:
            errors['lname'] = 'Last Name field should be at least 2 characters'
        if not EMAIL_REGEX.match(postData['email']):
            errors['email'] = "Email must be a valid format!"
        if len (postData['password']) < 8:
            errors['password'] = "Password must be at least 8 characters!!"
        if postData['password'] != postData['conf_password']:
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

class BooksManager(models.Manager):
    def validate(self, form):
        errors = {}
        if len(form['title']) < 1:
            errors['title'] = 'A title for the book is required'
        if len(form['desc']) < 5:
            errors['desc'] = 'The description must be longer than 5 characters'
        return errors

class Books(models.Model):
    title = models.CharField(max_length=255)
    desc = models.TextField()
    uploaded_by = models.ForeignKey(User,related_name="books", on_delete = models.CASCADE)
    favorited_by = models.ManyToManyField(User, related_name="favorited_books")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    objects = BooksManager()

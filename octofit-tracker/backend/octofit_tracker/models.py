from djongo import models

class User(models.Model):
    email = models.EmailField(unique=True)
    name = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)

class Team(models.Model):
    name = models.CharField(max_length=255)
    members = models.JSONField()  # Store user emails as a list of strings

class Activity(models.Model):
    user = models.CharField(max_length=255)  # Store user email instead of a ForeignKey
    activity_type = models.CharField(max_length=255)
    duration = models.IntegerField()
    date = models.DateField()

class Leaderboard(models.Model):
    user = models.CharField(max_length=255)  # Store user email instead of a ForeignKey
    score = models.IntegerField()

class Workout(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()
    duration = models.IntegerField()

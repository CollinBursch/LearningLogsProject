from django.db import models

# Create your models here.
class Topic(models.Model):
    text = models.CharField(max_length=200)
    date_added = models.DateTimeField(auto_now_add=True)

#this defines what we want to return specifically return, user defined, no bs 
    def __str__(self):
        return self.text

# Creates an Fk in connection to the Topic, inner join
class Entry(models.Model):
    topic = models.ForeignKey(Topic, on_delete=models.CASCADE)
    text = models.TextField()
    date_added = models.DateTimeField(auto_now_add=True)


    def __str__(self):
        return f"{self.text[:50]}..."


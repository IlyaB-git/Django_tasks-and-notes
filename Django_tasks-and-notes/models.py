from django.db import models


class CategoriesTasks(models.Model):
    name = models.CharField(max_length=250)
    color = models.CharField(max_length=7)
    deleted = models.BooleanField(default=False)
    def __str__(self):
        return self.name


class Tasks(models.Model):
    title = models.CharField("Task's title", max_length=250)
    time = models.TimeField(null=True)
    date = models.DateField(null=True)
    details = models.TextField()
    complete = models.BooleanField(default=False)
    category = models.ForeignKey(CategoriesTasks, on_delete=models.CASCADE)
    deleted = models.BooleanField(default=False)

    def __str__(self):
        return self.title




class Notes(models.Model):
    title = models.CharField("Note's title", max_length=250)
    details = models.TextField()
    image = models.ImageField(upload_to = 'images/', null=True)
    audio = models.FileField(upload_to='audio/', null=True)
    color = models.CharField(max_length=7)
    deleted = models.BooleanField(default=False)

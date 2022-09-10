from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Task(models.Model):
    # CASCADE=if an entry is deleted all sub entries get deleted
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    # 'blank=True' is form related and allows this field to be empty
    # 'null=True' is DB related and sets the column with null value 
    description = models.TextField(null=True, blank=True)
    complete = models.BooleanField(default=False)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

    class Meta:
        ordering = ['complete']
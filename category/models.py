from django.db import models
from task.models import taskModel
# Create your models here.
class categoryModel(models.Model):
    categoryName = models.CharField(max_length=50)
    task = models.ManyToManyField(taskModel,related_name='categories')
    
    def __str__(self) -> str:
        return self.categoryName
from django.db import models


class taskModel(models.Model):
    taskTitle = models.CharField(max_length=50)
    taskDescription = models.TextField()
    is_completed = models.BooleanField(default=False)

    assign_date = models.DateTimeField(auto_now_add=True)
    
    def __str__(self) -> str:
        return self.taskTitle
    

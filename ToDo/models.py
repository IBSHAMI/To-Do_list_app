from django.db import models

class ToDo(models.Model):
    # create name and duedate fields
    name = models.CharField(max_length=100)
    duedate = models.DateField()

    # to return the name of the ToDo
    def __str__(self):
        return f"{self.name} - {self.duedate}"

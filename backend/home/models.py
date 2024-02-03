from django.db import models



class Todo(models.Model):
    title=models.CharField(max_length=100,blank=False,null=False)
    body=models.TextField(blank=True)
    created_date=models.DateTimeField(auto_now_add=True)

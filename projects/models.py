from django.db import models

class Project(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()
    tech_stack = models.CharField(max_length=255)  # e.g., Python, JavaScript
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

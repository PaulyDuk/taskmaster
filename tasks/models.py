from django.db import models
from django.utils import timezone

# Create your models here.


class Category(models.Model):
    """Model representing a task category."""
    name = models.CharField(max_length=100, unique=True)
    
    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name_plural = "Categories"


class Task(models.Model):
    """Model representing a task."""
    title = models.CharField(max_length=200)
    due_date = models.DateTimeField()
    completed = models.BooleanField(default=False)
    category = models.ForeignKey(
        Category,
        on_delete=models.CASCADE,
        related_name='tasks'
    )
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return self.title
    
    @property
    def is_overdue(self):
        """Check if the task is overdue (past due date and not completed)."""
        return not self.completed and self.due_date < timezone.now()
    
    class Meta:
        ordering = ['due_date', '-created_at']

from djongo import models
from users.models import User
 
 
class Schedule(models.Model):

    classes = models.Manager()
    print(classes.all())
    created = models.DateTimeField(auto_now_add=True)
    name = models.CharField(max_length=100, unique=True, blank=False, null=False)
    user = models.ForeignKey('users.User', related_name='schedule', on_delete=models.CASCADE, null=False)
 
    class Meta:
        ordering = ('created',)
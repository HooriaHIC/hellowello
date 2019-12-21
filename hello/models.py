from django.db import models


class Posts(models.Model):
    name = models.CharField(
        max_length=300, default="This post doesn't have a name")
    content = models.TextField()
    image = models.ImageField(upload_to='images')
    dateposted = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

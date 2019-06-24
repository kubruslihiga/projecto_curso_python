from django.db import models


class Post(models.Model):
    title = models.CharField(max_length=255)
    body = models.TextField(max_length=2000)
    created_on = models.DateTimeField(auto_now_add=True)
    last_modified = models.DateTimeField(auto_now=True)
    categories = models.ManyToManyField('Category', related_name='posts')

    def __str__(self):
        return self.title
    
    def get_categories_names(self):
        ret = []
        for c in self.categories:
            ret.append(c.name)
        return ret
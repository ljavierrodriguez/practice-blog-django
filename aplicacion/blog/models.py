from django.db import models

# Create your models here.
class Category(models.Model):

    name = models.CharField(max_length=200, blank=False, null=False)
    description = models.CharField(max_length=300, blank=True, null=True)

    def __str__(self):
        return self.name

    class Meta:
        db_table = 'categories'


class Post(models.Model):
    title = models.CharField(max_length=200, blank=False, null=False)
    description = models.CharField(max_length=300, blank=True, null=True)
    content = models.TextField(blank=False, null=False)
    published = models.DateTimeField(auto_now_add=True)
    author = models.ForeignKey(
        "auth.User", verbose_name="usuario", on_delete=models.CASCADE)
    category = models.ForeignKey(
        Category, verbose_name="categoria", on_delete=models.CASCADE)

    def __str__(self):
        return self.title

    class Meta:
        db_table = 'posts'
        ordering = ['-published']


class Comment(models.Model):
    comment = models.TextField(blank=False, null=False)
    author = models.ForeignKey(
        "auth.User", verbose_name="usuario", on_delete=models.CASCADE)
    post = models.ForeignKey(
        Post, verbose_name="post", on_delete=models.CASCADE)


    def __str__(self):
        return self.comment

    class Meta:
        db_table = 'comments'
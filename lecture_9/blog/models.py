from django.db import models

class Category(models.Model):
    name = models.CharField(max_length=50)

    class Meta:
        verbose_name_plural = "Categories"

    def __str__(self):
        return self.name

class BlogPost(models.Model):
    title = models.CharField(verbose_name='სათაური', max_length=255)
    text = models.TextField(verbose_name='ტექსტი')
    is_active = models.BooleanField(verbose_name='აქტიურია', default=True)
    created_at = models.DateTimeField(verbose_name='შექმნის თარიღი', auto_now_add=True)
    updated_at = models.DateTimeField(verbose_name='განახლების თარიღი', auto_now=True)
    website = models.URLField(verbose_name='ვებ მისამართი', null=True)
    document = models.FileField(upload_to='blog_post_documents/', null=True)
    picture = models.ImageField(upload_to='blog_post_picture/', null=True)
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True, blank=True)

    class Meta:
        verbose_name = "Blog Post"
        verbose_name_plural = "Blog Posts"

    def __str__(self):
        return self.title



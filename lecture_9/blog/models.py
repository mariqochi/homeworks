from django.db import models
from django.utils import timezone


class Author(models.Model):
    first_name = models.CharField(verbose_name='First name', max_length=100)
    last_name = models.CharField(verbose_name='Last name', max_length=100)
    email = models.EmailField(verbose_name='Email')
    birth_date = models.DateField(verbose_name='Birth date', null=True)


    @property
    def age(self):
        if self.birth_date:
            today = date.today()
            age_in_years = today.year - self.birth_date.year
            # Subtract 1 if the birthday hasn't happened yet this year
            if (today.month, today.day) < (self.birth_date.month, self.birth_date.day):
                age_in_years -= 1
            return age_in_years
        return None

    class Meta:
        verbose_name = "Author"
        verbose_name_plural = "Authors"

    def __str__(self):
        return f"{self.first_name} {self.last_name}"


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
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True, blank=True)
    authors = models.ManyToManyField(Author, related_name='blog_posts', verbose_name='Authors')


    def get_image(self):
        return self.images.all()


    class Meta:
        verbose_name = "Blog Post"
        verbose_name_plural = "Blog Posts"

    def __str__(self):
        return self.title


class BlogPostImage(models.Model):
    blog_post = models.ForeignKey(
        "BlogPost",
        related_name='images',
        verbose_name='Blog Post',
        on_delete=models.CASCADE
    )
    image = models.ImageField(verbose_name="Image", upload_to='blog_post_images/')

    class Meta:
        verbose_name = "Blog Post Image"
        verbose_name_plural = "Blog Post Images"

    def __str__(self):
        return f"{self.blog_post.title} - {self.id}"


class BlogPostCover(models.Model):
    blog_post = models.OneToOneField(
        "BlogPost",
        verbose_name='Blog Post',
        related_name='cover',
        on_delete=models.CASCADE
    )
    image = models.ImageField(verbose_name="Image", upload_to='blog_post_covers/')

    class Meta:
        verbose_name = "Blog Post Cover"
        verbose_name_plural = "Blog Post Covers"

    def __str__(self):
        return f"{self.blog_post.title} - Cover id: {self.id}"

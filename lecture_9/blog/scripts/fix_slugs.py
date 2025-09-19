from blog.models import BlogPost
from slugify import slugify

def run():
    for post in BlogPost.objects.all():
        if not post.slug:
            post.slug = slugify(post.title)

        original_slug = post.slug
        counter = 1
        while BlogPost.objects.filter(slug=post.slug).exclude(id=post.id).exists():
            post.slug = f"{original_slug}-{counter}"
            counter += 1

        post.save()

    print("All slugs have been fixed!")
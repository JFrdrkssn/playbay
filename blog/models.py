from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse
from cloudinary.models import CloudinaryField

# Blog post status, 1 is default for posts added by user
STATUS = ((0, "Draft"), (1, "Published"))


class Category(models.Model):
    """
    Model for categories on the blog.
    """
    name = models.CharField(max_length=40)

    class Meta:
        """
        Plural name for category
        """
        verbose_name_plural = 'Categories'

    def __str__(self):
        return self.name


class Post(models.Model):
    """
    Model for posts on the blog.
    """
    title = models.CharField(max_length=150, unique=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name="blog_posts")
    content = models.TextField()
    featured_image = CloudinaryField('image', default='placeholder', blank=True)
    excerpt = models.CharField(max_length=200)
    created_on = models.DateField(auto_now_add=True)
    status = models.IntegerField(choices=STATUS, default=0)
    likes = models.ManyToManyField(User, related_name='blog_likes', blank=True)
    category = models.CharField(max_length=40, default='post')

    class Meta:
        """
        Order blog posts based on time of creation.
        Descending order, newest first.
        """
        ordering = ['-created_on']

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('post_detail', args=[str(self.id)])

    # Helper method to return the total number of likes on a post
    def number_of_likes(self):
        return self.likes.count()


class Comment(models.Model):
    """
    Model for comments on the blog.
    """
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='comments')
    user = models.ForeignKey(User, editable=False, on_delete=models.CASCADE, null=True, blank=True)
    email = models.EmailField()
    body = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)

    class Meta:
        """
        Order comments based on time of creation.
        Descending order, oldest first.
        """
        ordering = ['created_on']

    def __str__(self):
        return f"{self.user} said {self.body}"

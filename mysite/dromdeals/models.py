from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.urls import reverse

# create models 

# PostProduct Model - for posting product
class PostProduct(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)  # Reference to the User model
    title = models.CharField(max_length=200)
    text = models.TextField()
    create_date = models.DateTimeField(default=timezone.now)
    photo = models.ImageField(upload_to='post_photos/', null=True, blank=True)
    approved = models.BooleanField(default=False)  # Field to track if the post is approved

    def __str__(self):
        return f"{self.title} by {self.user.username}"

    # Method to approve the post
    def approve_post(self):
        self.approved = True
        self.save()

    # Go to post details
    def get_absolute_url(self):
        return reverse("post_detail", kwargs={'pk': self.pk})



# ProductComments Model - for commenting on a product
class ProductComments(models.Model):
    post = models.ForeignKey(PostProduct, related_name='comments', on_delete=models.CASCADE)  # Link to PostProduct model
    user = models.ForeignKey(User, on_delete=models.CASCADE)  # Reference to the User model for the commenter
    text = models.TextField()
    create_date = models.DateTimeField(default=timezone.now)
    approved_comment = models.BooleanField(default=False)  # Whether the comment is approved

    def __str__(self):
        return f"Comment by {self.user.username} on {self.post.title}"

    # Method to approve the comment
    def approve_comment(self):
        self.approved_comment = True
        self.save()

    # Go back to home posts
    def get_absolute_url(self):
        return reverse("post_list")

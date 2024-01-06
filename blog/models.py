from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse

# Create your models here.
class Post(models.Model):
 image_field = models.ImageField(null=True,blank=True,upload_to="images/")
 title = models.CharField(max_length=255)
 
 author = models.ForeignKey(User, on_delete = models.CASCADE)
 body = models.TextField()
 likes = models.ManyToManyField(User,related_name='blog_poss')
 
 def total_likes(self):
    return self.likes.count()
  
 
 def __str__(self):
    return self.title + ' | ' + str(self.author)
 
 def get_absolute_url(self):
    return reverse('article', args=[str(self.id)])

class Contact(models.Model):
    username = models.CharField(max_length=255)
    email = models.EmailField(max_length=255, null=True, blank=True)
    message = models.TextField()

    def __str__(self):
        return f"{self.username} - {self.email}"

     
class Comment(models.Model):
    post = models.ForeignKey(Post, related_name="comments" ,on_delete = models.CASCADE)
    name = models.CharField(max_length=255)
    body = models.TextField()
    date_added = models.DateTimeField(auto_now_add=True)
    def __str__(self):
       return '%s -%s' % (self.post.title,self.name)
    
    
class About(models.Model):
    body = models.TextField()
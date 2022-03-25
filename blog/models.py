from django.db import models
from django.conf import settings
User = settings.AUTH_USER_MODEL


# Create your models here.
class Tag(models.Model):
    value = models.CharField(max_length=250)
    
    def __str__(self):
        return self.value


class Post(models.Model):
    STATUS_CHOICE = (
        ('DRAFT','Draft'),
        ('PUBLISHED','Published'),
        ('ARCHIVED','Archived')
    )
    
    FILED_CAT = (
        ('FASHION','fashion'),
        ('BEAUTY','beauty'),
        ('TRAVEL','travel'),
        ('FOOD + DRINK','food + drink'),
        ('SCHOOL LIFE','school life'),
        ('COLLAGE LIFE','collage life'),
        ('FAMILY','family'),
        ('FITNES','fitnes'),
        ('MUSIC','music'),
        ('REEL','reel'),
        ('MOVIES','movies'),
        ('TECHNOLOGY','technology'),
        ('FINANCE','finance'),
        ('SCIENCE','science'),
        ('NEWS','news'),
        ('PETS','pets'),
        ('OTHER','other'),
        ('NONE','none')
    )
    title = models.CharField(max_length=100)
    content = models.TextField()
    summary = models.TextField(max_length=500, blank=True, null=True)
    slug = models.SlugField(max_length=120)
    author = models.ForeignKey(User,on_delete=models.PROTECT)
    tags = models.ManyToManyField(Tag, related_name="posts")   
    status =  models.CharField( max_length=50, choices=STATUS_CHOICE,default='DRAFT')    
    created_at = models.DateTimeField(auto_now_add=True)
    modified_at = models.DateTimeField(auto_now=True)
    filed_cat = models.CharField(max_length=50, choices=FILED_CAT,default='none')
    image_blog = models.ImageField(upload_to='blog_img/',max_length=300,null=True,default=None)
    def __str__(self):
        return self.title
    
    
    class Meta:
        ordering = ['-modified_at']
from django.db import models

# Create your models here.

class Setting(models.Model):
    STATUS = (
        ('True', 'True'),
        ('False', 'False'),
    )
    title = models.CharField(max_length=200, blank=True, null=True)
    keyword = models.CharField(max_length=200, blank=True, null=True)
    description = models.TextField()
    address = models.CharField(max_length=200,blank=True, null=True)
    phone = models.IntegerField()
    fax = models.CharField(blank=True, null=True, max_length=50)
    email = models.EmailField(blank=True, null=True, max_length=50)
    smptserver = models.CharField(max_length=100, blank=True, null=True)
    smtpemail = models.EmailField(blank=True, null=True, max_length=50)
    smptpassword = models.CharField(blank=True, null=True, max_length=50)
    smptport = models.CharField(blank=True, null=True, max_length=100)
    icon = models.ImageField(blank=True, null=True, upload_to='icon/')
    facebook = models.CharField(blank=True, null=True, max_length=100)
    instagram = models.CharField(blank=True, null=True, max_length=100)
    address = models.TextField(blank=True, null=True)
    contact = models.TextField(blank=True, null=True)
    reference = models.TextField(blank=True, null=True)
    status = models.CharField(max_length=50, choices=STATUS)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title
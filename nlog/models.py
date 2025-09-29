from django.db import models



class Blog(models.Model):
    id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=150,unique=True)
    content = models.TextField()
    image = models.ImageField(upload_to="blog")
    created_at = models.DateTimeField(auto_now_add=True)


    def  __str__(self):
        return self.title
    



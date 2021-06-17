from django.db import models


class Category(models.Model):
    name = models.CharField(("Category"),max_length=50,null = True)

    def __str__(self):
        return self.name
    


class Photo(models.Model):
    title = models.CharField(("Name"), max_length=50,null = True)
    content = models.TextField(("Content"),null = True)
    photo = models.ImageField(("Image"), upload_to='photos/%Y/%m/%d/',blank = True)
    image = models.ForeignKey("Category",on_delete=models.CASCADE)

    def __str__(self):
        return self.title
    
from django.db import models
class Sex(models.Model):
    name=models.CharField(db_index=True,max_length=150)
    def __str__(self):
        return self.name

class Type(models.Model):
    name=models.CharField(db_index=True,max_length=150)
    def __str__(self):
        return self.name
class Size(models.Model):
    name=models.CharField(max_length=10)
    def __str__(self):
        return self.name
class Item(models.Model):
    name=models.CharField(max_length=255)
    description=models.TextField(max_length=600)
    price=models.FloatField()
    img=models.ImageField(upload_to="images/")
    slug = models.SlugField(unique=True, db_index=True)
    sex = models.ForeignKey(Sex, on_delete=models.CASCADE)
    type=models.ForeignKey(Type,on_delete=models.CASCADE)
    size=models.ManyToManyField("Size",related_name="size")
    def __str__(self):
        return self.name


from django.db import models
from django.contrib.contenttypes.models import ContentType
from django.contrib.auth.models import User
from django.contrib.contenttypes.fields import GenericForeignKey

class Tag(models.Model):
    label= models.CharField(max_length=255)

class TaggedItems(models.Model):
    tag= models.ForeignKey(Tag,on_delete=models.CASCADE)

    content_type=models.ForeignKey(ContentType,on_delete=models.CASCADE)
    object_id=models.PositiveIntegerField()
    #using this^ solution we are bound to primary key only integers. so this is not the suitable way.
    #if we want to know the actual object that this tag is applied to, we doo so.
    content_object=GenericForeignKey()

class LikedItems(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    content_type=models.ForeignKey(ContentType,on_delete=models.CASCADE)
    object_id=models.PositiveIntegerField()
    content_object=GenericForeignKey
    





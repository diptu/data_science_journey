from django.db import models

# Create your models here.
from django.utils.text import slugify
'''
random_string_generator is located here:
http://joincfe.com/blog/random-string-generator-in-python/
'''
from .utils import random_string_generator

def unique_slug_generator(instance, new_slug=None):
    """
    This is for a Django project and it assumes your instance
    has a model with a slug field and a title character (char) field.
    """
    if new_slug is not None:
        slug = new_slug.replace(" ", "-")
    else:
        filed = "%s-%s" % (instance.first_name, instance.last_name).replace(" ", "-")
        slug = slugify(instance.filed)

    Klass = instance.__class__
    qs_exists = Klass.objects.filter(slug=slug).exists()
    if qs_exists:
        new_slug = "{slug}-{randstr}".format(
                    slug=slug,
                    randstr=random_string_generator(size=4)
                )
        return unique_slug_generator(instance, new_slug=new_slug)
    return slug


class Employee(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    slug = models.CharField(max_length=80,unique=True,default='your full name')
    photo = models.ImageField(upload_to='profile')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def save(self, **kwargs):
        slug = "%s-%s" % (self.first_name, self.last_name)
        self.slug = unique_slug_generator(self, slug)
        super(Employee, self).save(**kwargs)
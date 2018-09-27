import os,uuid
from django.db import models
from django.contrib.auth.models import User
from django.core.validators import FileExtensionValidator

#Function to rename uploaded image.
def file_rename(instance, filename):
    upload_to = '{}'.format(instance.user)
    ext = filename.split('.')[-1]
    filename = "%s.%s" % (uuid.uuid4(), ext)
    return os.path.join(upload_to, filename)


class Item(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    item_name = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=10,decimal_places=2)
    image = models.ImageField(upload_to=file_rename, 
        validators=[FileExtensionValidator(allowed_extensions=['jpg','jpeg','png'],
        message="Unsupported format.")],null=True, blank=True)
    
    def __str__(self):
        return self.item_name
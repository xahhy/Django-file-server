from django.db import models
from django.core.files.storage import FileSystemStorage
from django.core.exceptions import ValidationError
import os
class MyFileStorage(FileSystemStorage):
    def _save(self, name, content):
        if self.exists(name):
            self.delete(name)
        return super(MyFileStorage, self)._save(name, content)

    def get_available_name(self,name):
        return name

mfs = MyFileStorage()

class FilePathModel(models.Model):
    path = models.CharField(max_length=1000)
    # match = models.CharField(max_length=1000)
    
    def save(self,*args,**kwargs):
        
        super(FilePathModel,self).save(*args,**kwargs)



    def __str__(self):
        return self.path

def upload_path(instance,filename):
    return str(instance.path)

class FilesModel(models.Model):
    description = models.CharField(max_length=128,default='description')
    path = models.ForeignKey(FilePathModel,null=True,blank=True)
    file = models.FileField(upload_to=upload_path,storage=mfs)

    def save(self,*args,**kwargs):
        super(FilesModel,self).save(*args,**kwargs)


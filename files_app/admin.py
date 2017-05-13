from django.contrib import admin
from .models import *
from .forms import *
# Register your models here.
class FilePathAdmin(admin.ModelAdmin):
    form = FilesFilePathForm

    

class FilesAdmin(admin.ModelAdmin):
    list_display = ['description','path','file','file_link']
    list_editable = ['path','file']
    def file_link(self, obj):
        if obj.file:
            return "<a href='/file/download/%s' download>Download</a>" % (obj.pk)
        else:
            return "No attachment"
    file_link.allow_tags = True
    file_link.short_description = 'File Download'   


admin.site.register(FilesModel,FilesAdmin)
admin.site.register(FilePathModel, FilePathAdmin)

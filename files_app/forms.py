from django import forms
from .models import *   

class FilesFilePathForm(forms.ModelForm):
    class Meta:
        model = FilePathModel
        fields = '__all__'

    def clean_path(self):
        filename = self.cleaned_data['path']
        if not os.path.exists(filename) or not os.path.isfile(filename):
            raise ValidationError('file does not exist')
        return filename
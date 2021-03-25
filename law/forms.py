from django import forms

from law.models import Chapter


class ChapterCreateForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(ChapterCreateForm, self).__init__(*args, **kwargs)
        self.fields['source_url'] = forms.CharField(required=False)

    class Meta:
        model = Chapter
        fields = ['act', 'number', 'name', 'source_url']

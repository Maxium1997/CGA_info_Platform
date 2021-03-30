from django import forms

from law.models import Chapter, Article


class ChapterCreateForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(ChapterCreateForm, self).__init__(*args, **kwargs)
        self.fields['number'] = forms.IntegerField(required=True,
                                                   widget=forms.NumberInput(attrs={'placeholder': self.initial.get('act').chapter_set.count()+1,
                                                                                   'class': 'form-control'}))
        self.fields['name'] = forms.CharField(required=True,
                                              widget=forms.TextInput(attrs={'class': 'form-control'}))
        self.fields['source_url'] = forms.URLField(required=False,
                                                   widget=forms.TextInput(attrs={'class': 'form-control'}))

    def save(self, commit=True):
        chapter = super(ChapterCreateForm, self).save(commit=False)
        chapter.act = self.initial.get('act')
        if commit:
            chapter.save()
        return chapter

    class Meta:
        model = Chapter
        fields = ['number', 'name', 'source_url']


class ArticleCreateForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(ArticleCreateForm, self).__init__(*args, **kwargs)
        self.fields['chapter'] = forms.ModelChoiceField(queryset=self.initial.get('act').chapter_set.all(),
                                                        required=False,
                                                        widget=forms.Select(attrs={'class': 'form-control'}))
        self.fields['priority'] = forms.CharField(widget=forms.TextInput(attrs={'placeholder': self.initial.get('act').article_set.count()+1,
                                                                                'class': 'form-control'}))
        self.fields['number'] = forms.CharField(widget=forms.TextInput(attrs={'placeholder': self.initial.get('act').article_set.count()+1,
                                                                              'class': 'form-control'}))
        self.fields['content'] = forms.CharField(required=True,
                                                 widget=forms.Textarea(attrs={'class': 'form-control'}))
        self.fields['source_url'] = forms.URLField(required=False,
                                                   widget=forms.URLInput(attrs={'class': 'form-control'}))

    def save(self, commit=True):
        article = super(ArticleCreateForm, self).save(commit=False)
        article.act = self.initial.get('act')
        if commit:
            article.save()
        return article

    class Meta:
        model = Article
        fields = ['chapter', 'priority', 'number', 'content', 'source_url']

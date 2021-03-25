from django.utils.decorators import method_decorator
from django.contrib.admin.views.decorators import staff_member_required
from django.urls import reverse_lazy
from django.views.generic import TemplateView, ListView, DetailView, CreateView, DeleteView

from .models import Act, Chapter
from .forms import ChapterCreateForm
# Create your views here.


class IndexView(TemplateView):
    template_name = 'index.html'


class ActsView(ListView):
    model = Act
    template_name = 'acts.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['acts'] = self.object_list
        return context


@method_decorator(staff_member_required, name='dispatch')
class ActCreateView(CreateView):
    model = Act
    template_name = 'act_create.html'
    fields = ['name', 'slug', 'source_url']


class ChapterDetailView(DetailView):
    model = Chapter
    template_name = 'chapter_detail.html'

    def get_object(self, queryset=None):
        object = Act.objects.get(slug=self.kwargs['slug'])
        return object

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        act = Act.objects.get(slug=self.kwargs['slug'])
        context['act'] = act
        context['chapter'] = act.chapter_set.get(number=self.kwargs['number'])
        return context


@method_decorator(staff_member_required, name='dispatch')
class ChapterCreateView(CreateView):
    model = Chapter
    template_name = 'chapter_create.html'
    fields = ['act', 'number', 'name', 'source_url']

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        act = Act.objects.get(slug=self.kwargs['slug'])
        context['act'] = act
        context['form'] = ChapterCreateForm(initial={'act': act})
        return context


@method_decorator(staff_member_required, name='dispatch')
class ChapterDeleteView(DeleteView):
    model = Act
    template_name = 'chapter_delete.html'
    success_url = reverse_lazy('acts')

    def get_object(self, queryset=None):
        object = Act.objects.get(slug=self.kwargs['slug']).chapter_set.get(number=self.kwargs['number'])
        return object

    def get_context_data(self, **kwargs):
        context = super(ChapterDeleteView, self).get_context_data(**kwargs)
        context['act'] = Act.objects.get(slug=self.kwargs['slug'])
        return context


class ActDetailView(DetailView):
    model = Act
    template_name = 'act_detail.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['act'] = self.object
        context['articles'] = self.object.article_set.all()
        return context


class ArticleDetailView(DetailView):
    model = Act
    template_name = 'article_detail.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['act'] = self.object
        context['article'] = self.object.article_set.get(number=self.kwargs['number'])
        return context

from django.shortcuts import render
from django.utils.decorators import method_decorator
from django.contrib.admin.views.decorators import staff_member_required
from django.urls import reverse_lazy
from django.views.generic import TemplateView, ListView, DetailView, CreateView, DeleteView

from .models import Act, Chapter, Article
from .forms import ChapterCreateForm, ArticleCreateForm, \
    SearchForm
from law.engine import act_search, chapter_search, article_search
# Create your views here.


class IndexView(TemplateView):
    template_name = 'index.html'


class ActsView(ListView):
    model = Act
    template_name = 'acts.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['acts'] = self.object_list
        context['search_form'] = SearchForm()
        return context


def search(request):
    search_form = SearchForm(request.POST)
    search_field = request.POST.get('search_field')

    searched_acts = act_search(search_field)
    searched_chapters = chapter_search(search_field)
    searched_articles = article_search(search_field)

    context = {'search_form': search_form,
               'searched_acts': searched_acts,
               'searched_chapters': searched_chapters,
               'searched_articles': searched_articles}

    return render(request, template_name='search_result.html', context=context)


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
    fields = ['number', 'name', 'source_url']

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        act = Act.objects.get(slug=self.kwargs['slug'])
        context['act'] = act
        context['form'] = ChapterCreateForm(initial={'act': act})
        return context

    def form_valid(self, form):
        act = Act.objects.get(slug=self.kwargs['slug'])
        form.instance.act = act
        form.save()
        return super(ChapterCreateView, self).form_valid(form)


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
        return context


class ArticleDetailView(DetailView):
    model = Act
    template_name = 'article_detail.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['act'] = self.object
        context['article'] = self.object.article_set.get(number=self.kwargs['number'])
        return context


@method_decorator(staff_member_required, name='dispatch')
class ArticleCreateView(CreateView):
    model = Article
    template_name = 'article_create.html'
    fields = ['chapter', 'priority', 'number', 'content', 'source_url']

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        act = Act.objects.get(slug=self.kwargs['slug'])
        try:
            chapter = act.chapter_set.get(number=self.kwargs['number'])
            context['form'] = ArticleCreateForm(initial={'act': act,
                                                         'chapter': chapter})
        except KeyError:
            context['form'] = ArticleCreateForm(initial={'act': act})

        context['act'] = act
        return context
    
    def form_valid(self, form):
        act = Act.objects.get(slug=self.kwargs['slug'])
        form.instance.act = act
        try:
            chapter = act.chapter_set.get(number=self.kwargs['number'])
            form.instance.chapter = chapter
        except KeyError:
            pass
        form.save()
        return super(ArticleCreateView, self).form_valid(form)

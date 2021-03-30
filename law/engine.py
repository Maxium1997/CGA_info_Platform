from django.db.models import Q
from law.models import Act, Chapter, Article


def act_search(key_word: str):
    filter_criteria = Q(name__contains=key_word)
    acts = Act.objects.filter(filter_criteria)
    return list(set(acts))


def chapter_search(key_word: str):
    filter_criteria = Q(name__contains=key_word)
    chapters = Chapter.objects.filter(filter_criteria)
    return list(set(chapters))


def article_search(key_word: str):
    filter_criteria = Q(content__contains=key_word)
    articles = Article.objects.filter(filter_criteria)
    return list(set(articles))

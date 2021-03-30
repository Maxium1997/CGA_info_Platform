from django.urls import path, include

from .views import IndexView, ActsView, ActDetailView, ActCreateView,\
    ChapterDetailView, ChapterCreateView, ChapterDeleteView,\
    ArticleDetailView, ArticleCreateView,\
    search


urlpatterns = [
    path('', IndexView.as_view(), name='index'),
    path('search', search, name='search'),

    path('acts/', include([
        path('all', ActsView.as_view(), name='acts'),
        path('create', ActCreateView.as_view(), name='act_create'),
    ])),

    path('<slug:slug>', ActDetailView.as_view(), name='act_detail'),
    path('<slug:slug>/', include([
        path('chapter/', include([
            path('create', ChapterCreateView.as_view(), name='chapter_create'),
            path('<int:number>', ChapterDetailView.as_view(), name='chapter_detail'),
            path('<int:number>/', include([
                path('delete', ChapterDeleteView.as_view(), name='chapter_delete'),
            ])),
        ])),

        path('article/', include([
            path('create', ArticleCreateView.as_view(), name='article_create'),
            path('<str:number>', ArticleDetailView.as_view(), name='article_detail'),
        ])),
    ])),
]

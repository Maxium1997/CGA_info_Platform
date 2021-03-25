from django.urls import path, include

from .views import IndexView, ActsView, ActDetailView, ActCreateView,\
    ChapterDetailView, ChapterCreateView, ChapterDeleteView,\
    ArticleDetailView


urlpatterns = [
    path('', IndexView.as_view(), name='index'),

    path('acts/', include([
        path('', ActsView.as_view(), name='acts'),
        path('create', ActCreateView.as_view(), name='act_create'),
        path('<slug>', ActDetailView.as_view(), name='act_detail'),
        path('<slug>/', include([
            path('chapter/', include([
                path('<number>', ChapterDetailView.as_view(), name='chapter_detail'),
                path('<number>/', include([
                    path('delete', ChapterDeleteView.as_view(), name='chapter_delete'),
                ])),
                path('create', ChapterCreateView.as_view(), name='chapter_create'),
            ])),
            path('<number>', ArticleDetailView.as_view(), name='article_detail')
        ])),
    ])),
]

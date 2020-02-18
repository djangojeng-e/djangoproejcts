from django.urls import path

from .apis import generic
from .views import snippet_list, snippet_detail
app_name = 'snippets'

urlpatterns = [
    # path('snippets/', snippet_list),
    # path('snippets/<int:pk>/', snippet_detail),

    # Class-based view 를 사용하는 경우, as_view()함수를 호출
    path('snippets/', generic.SnippetListCreateAPIView.as_view()),
    path('snippets/<int:pk>/', generic.SnippetRetrieveUpdateDestroyAPIView.as_view()),
]
# ButterCMS - Basic Django Module

*Simple Gneeric view helpers to get access to your butter content.*


### Usage

```settings.py
BUTTER_CMS = {
    'KEY': os.getenv('BUTTER_CMS_KEY')
}
```

### Usage


**Page Detail**

```urls.py
from butter.views import ButterPageDetailView

urlpatterns = [
    # where `brand_overview` is the page type you defined in butter-cms
    url(r'^b/(?P<slug>.*)/$', ButterPageDetailView.as_view(butter_type='brand_overview'), name='brand_overview'),
]

http://localhost:8000/b/hugo-boss/  # where hugo-boss is your slug in butter-cms
```


**Blog List**

```urls.py
from butter.views import ButterBlogListView

urlpatterns = [
    url(r'^blog/$', ButterBlogsListView.as_view(), name='blog_list'),
]

http://localhost:8000/b/hugo-boss/  # where hugo-boss is your slug in butter-cms
```


**Blog Detail**

```urls.py
from butter.views import ButterBlogDetailView

urlpatterns = [
    url(r'^blog/(?P<slug>.*)/$', ButterBlogDetailView.as_view(), name='blog_detail'),
]

http://localhost:8000/blog/hugo-boss/  # where hugo-boss is your slug in butter-cms
```

# ButterCMS - Basic Django Module

*Simple Gneeric view helpers to get access to your butter content.*


### Usage

**settings**

```settings.py
BUTTER_CMS = {
    'KEY': os.getenv('BUTTER_CMS_KEY')
}
```


**Page List**

**Template**

*butter/pages_list.html*

```urls.py
from butter.views import ButterPageDetailView

urlpatterns = [
    # where `brand_overview` is the page type you defined in butter-cms
    url(r'^b/(?P<slug>.*)/$', ButterPageDetailView.as_view(butter_type='brand_overview'), name='brand_overview'),
]

http://localhost:8000/b/hugo-boss/  # where hugo-boss is your slug in butter-cms
```


**Page Detail**

**Template**

*butter/pages_detail.html*

```urls.py
from butter.views import ButterPageDetailView

urlpatterns = [
    # where `brand_overview` is the page type you defined in butter-cms
    url(r'^b/(?P<slug>.*)/$', ButterPageDetailView.as_view(butter_type='brand_overview'), name='brand_overview'),
]

http://localhost:8000/b/hugo-boss/  # where hugo-boss is your slug in butter-cms
```


**Blog List**

**Template**

*butter/posts_list.html*

```urls.py
from butter.views import ButterBlogListView

urlpatterns = [
    url(r'^blog/$', ButterBlogsListView.as_view(), name='blog_list'),
]

http://localhost:8000/blog/
```


**Blog Detail**

**Template**

*butter/posts_detail.html*

```urls.py
from butter.views import ButterBlogDetailView

urlpatterns = [
    url(r'^blog/(?P<slug>.*)/$', ButterBlogDetailView.as_view(), name='blog_detail'),
]

http://localhost:8000/blog/what-a-wonderful-time-in-the-sun/
```


from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from django.views.generic import TemplateView
from wokerlist import views
from wokerlist.views import BirthdayView, BestWorkerView, Structure, SearchResultsView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('ckeditor/', include('ckeditor_uploader.urls')),
    path('adr/', include('wokerlist.urls'), name='wokerlist'),
    path('doc/', include('fileserv.urls'), name='fileserv'),
    path('blog/', include('blog.urls'), name='blog'),
    path('about/', include('about.urls'), name='about'),
    path('contractors/', include('contractors.urls'), name='contractors'),
    path('quiz/', include('oprosnik.urls'), name='oprosnik'),
    path('', TemplateView.as_view(template_name='index.html'), name='Index'),
    path('graphic/', Structure.as_view(), name='tmp'),
    path('birthdays/', BirthdayView.as_view(), name='birthdays'),
    path('best/', BestWorkerView.as_view(), name='best'),
    # path('search/', include('haystack.urls'),),
    # path('search/', views.SearchResultsView, name='search_results'),
    path('search/', SearchResultsView.as_view(), name='search_results'),

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

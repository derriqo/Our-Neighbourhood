from django.conf.urls import url
from . import views
from django.conf.urls.static import static
from django.conf import settings

urlpatterns=[
    url('^$',views.home,name='home'),
    url('^profile/',views.profile,name='profile'),
    # url('^edit/',views.edit_profile,name='edit_profile'),
    url('^bussiness/',views.new_bussiness,name='bussiness'),
    url('^allbiz/',views.biz_page,name='biz_page'),
]

if settings.DEBUG:
    urlpatterns+= static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)

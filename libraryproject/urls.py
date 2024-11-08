"""
URL configuration for libraryproject project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from django.contrib import admin
from django.urls import path
from apps.bookmodule import views  # استيراد الدوال من bookmodule

# قائمة الروابط
urlpatterns = [
    path('admin/', admin.site.urls),  # رابط لوحة التحكم Django admin

    # روابط الدوال الأساسية
    path('', views.index),  # الدالة index لعرض الصفحة الرئيسية
    path('index2/<int:val1>/', views.index2),  # الدالة index2 مع متغير val1
    path('<int:bookId>/', views.viewbook),  # الدالة viewbook مع متغير bookId

    # الروابط المطلوبة لكل مهمة من مختبر HTML/CSS
    path('books/html5/links', views.links_page, name='books.links'),
    path('books/html5/text/formatting', views.text_formatting_page, name='books.text_formatting'),
    path('books/html5/listing', views.listing_page, name='books.listing'),
    path('books/html5/tables', views.tables_page, name='books.tables'),
     path('admin/', admin.site.urls),
    path('books/search', views.search_page, name='books.search'),  # رابط صفحة البحث
]


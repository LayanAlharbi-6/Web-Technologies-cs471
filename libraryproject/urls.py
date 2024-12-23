from django.contrib import admin
from django.urls import path
from apps.bookmodule import views  # استيراد الدوال من bookmodule

# قائمة الروابط
urlpatterns = [
    # رابط لوحة التحكم Django admin
    path('admin/', admin.site.urls),  
    
    # الروابط الأساسية
    path('', views.index, name='index'),  # الدالة index لعرض الصفحة الرئيسية
    path('index2/<int:val1>/', views.index2, name='index2'),  # الدالة index2 مع متغير val1
    path('<int:bookId>/', views.viewbook, name='viewbook'),  # الدالة viewbook مع متغير bookId

    # الروابط المطلوبة لكل مهمة من مختبر HTML/CSS
    path('books/html5/links', views.links_page, name='books.links'),
    path('books/html5/text/formatting', views.text_formatting_page, name='books.text_formatting'),
    path('books/html5/listing', views.listing_page, name='books.listing'),
    path('books/html5/tables', views.tables_page, name='books.tables'),

    # رابط صفحة البحث
    path('books/search', views.search_page, name='books.search'),

    # الروابط الجديدة
    path('add-books/', views.add_books, name='add_books'),  # رابط لإضافة الكتب
    path('books/simple-query/', views.simple_query, name='simple_query'),  # استعلام بسيط
    path('books/complex-query/', views.complex_query, name='complex_query'),  # استعلام معقد
    path('books/lab8/task1', views.task1_view, name='task1'),

    # روابط إضافية (إذا كانت مطلوبة مستقبلاً)
    # path('books/some-other-path', views.some_other_view, name='some_other_view'),
]

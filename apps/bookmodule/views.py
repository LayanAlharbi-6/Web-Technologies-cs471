from django.http import HttpResponse
from django.shortcuts import render

def index(request):
    name = request.GET.get("name") or "world!"
    return HttpResponse("Hello, " + name)

def index2(request, val1=0):
    return HttpResponse("value1 = " + str(val1))

def viewbook(request, bookId):
    # افتراض وجود بيانات الكتب
    book1 = {'id': 123, 'title': 'Continuous Delivery', 'author': 'J. Humble and D. Farley'}
    book2 = {'id': 456, 'title': 'Secrets of Reverse Engineering', 'author': 'E. Eilam'}
    
    targetBook = None
    if book1['id'] == bookId:
        targetBook = book1
    elif book2['id'] == bookId:
        targetBook = book2
    
    context = {'book': targetBook}
    return render(request, 'bookmodule/show.html', context)

# الدوال الخاصة بمهام المختبر
def links_page(request):
    return render(request, 'bookmodule/links.html')

def text_formatting_page(request):
    return render(request, 'bookmodule/text_formatting.html')

def listing_page(request):
    return render(request, 'bookmodule/listing.html')

def tables_page(request):
    return render(request, 'bookmodule/tables.html')


# دالة لعرض صفحة البحث ومعالجة نتائج البحث
def search_page(request):
    if request.method == "POST":
        keyword = request.POST.get('keyword', '').lower()
        isTitle = request.POST.get('option1')
        isAuthor = request.POST.get('option2')

        # الحصول على قائمة الكتب
        books = __getBooksList()
        filtered_books = []

        for book in books:
            found = False
            if isTitle and keyword in book['title'].lower():
                found = True
            if not found and isAuthor and keyword in book['author'].lower():
                found = True
            if found:
                filtered_books.append(book)

        return render(request, 'bookmodule/bookList.html', {'books': filtered_books})

    return render(request, 'bookmodule/search.html')

# دالة للحصول على قائمة الكتب (مثال على قاعدة بيانات وهمية)
def __getBooksList():
    book1 = {'id': 12344321, 'title': 'Continuous Delivery', 'author': 'J.Humble and D. Farley'}
    book2 = {'id': 56788765, 'title': 'Reversing: Secrets of Reverse Engineering', 'author': 'E. Eilam'}
    book3 = {'id': 43211234, 'title': 'The Hundred-Page Machine Learning Book', 'author': 'Andriy Burkov'}
    return [book1, book2, book3]

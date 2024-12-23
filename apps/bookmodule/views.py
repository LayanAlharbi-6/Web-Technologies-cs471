from django.http import HttpResponse
from django.shortcuts import render
from django.db.models import Q
from .models import Book

# دالة الإدخال اليدوي للكتب في قاعدة البيانات
def add_books(request):
    books_data = [
        {"title": "Continuous Delivery", "author": "J. Humble and D. Farley", "price": 120.00, "edition": 3},
        {"title": "Reversing: Secrets of Reverse Engineering", "author": "E. Eilam", "price": 97.00, "edition": 2},
        {"title": "The Hundred-Page Machine Learning Book", "author": "Andriy Burkov", "price": 100.00, "edition": 4},
    ]
    for data in books_data:
        Book.objects.create(**data)
    return HttpResponse("Books added successfully!")

# استعلام بسيط للكتب
def simple_query(request):
    books = Book.objects.filter(title__icontains='and')  # استعلام للبحث عن كتب تحتوي على كلمة "and"
    response = "<h1>Simple Query Results:</h1>"
    for book in books:
        response += f"<p>ID: {book.id}, Title: {book.title}, Author: {book.author}, Price: {book.price}, Edition: {book.edition}</p>"
    return HttpResponse(response)

# استعلام معقد للكتب
def complex_query(request):
    books = Book.objects.filter(
        author__isnull=False
    ).filter(
        title__icontains='and'
    ).filter(
        edition__gte=2
    ).exclude(
        price__lte=100
    )[:10]
    if books.exists():
        response = "<h1>Complex Query Results:</h1>"
        for book in books:
            response += f"<p>ID: {book.id}, Title: {book.title}, Author: {book.author}, Price: {book.price}, Edition: {book.edition}</p>"
    else:
        response = "<h1>No books matched the query.</h1>"
    return HttpResponse(response)

# عرض الكتب بسعر أقل من أو يساوي 50 (المطلوب إضافة هذه الدالة)
def task1_view(request):
    # تصفية الكتب بسعر أقل من أو يساوي 50
    books = Book.objects.filter(Q(price__lte=50))
    # عرض النتائج في قالب HTML
    return render(request, 'bookmodule/task1.html', {'books': books})

# الدالة index لعرض الرسالة
def index(request):
    name = request.GET.get("name") or "world!"
    return HttpResponse("Hello, " + name)

# دالة index2 مع متغير val1
def index2(request, val1=0):
    return HttpResponse("value1 = " + str(val1))

# عرض بيانات الكتاب بناءً على ID
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

# صفحات HTML المطلوبة
def links_page(request):
    return render(request, 'bookmodule/links.html')

def text_formatting_page(request):
    return render(request, 'bookmodule/text_formatting.html')

def listing_page(request):
    return render(request, 'bookmodule/listing.html')

def tables_page(request):
    return render(request, 'bookmodule/tables.html')

# صفحة البحث ومعالجة النتائج
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

# قاعدة بيانات وهمية للكتب
def __getBooksList():
    book1 = {'id': 12344321, 'title': 'Continuous Delivery', 'author': 'J.Humble and D. Farley'}
    book2 = {'id': 56788765, 'title': 'Reversing: Secrets of Reverse Engineering', 'author': 'E. Eilam'}
    book3 = {'id': 43211234, 'title': 'The Hundred-Page Machine Learning Book', 'author': 'Andriy Burkov'}
    return [book1, book2, book3]



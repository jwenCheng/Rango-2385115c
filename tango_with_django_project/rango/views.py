from django.shortcuts import render
from django.http import HttpResponse
from rango.models import Category,Page

def index(request):
    #context_dict={'boldmessage':"Crunchy, creamy, cookie, candy, cupcake!"}
    category_list = Category.objects.order_by('-likes')[:5]
    page_list =Page.objects.order_by('-views')[:5]
    context_dict = {'categories': category_list, 'pages': page_list}

    return render(request,'rango/index.html',context=context_dict)

def about(request):
    context_dict = {'boldmessage': "Rango says here is the about page."}

    return render(request, 'rango/about.html', context=context_dict)


from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
def product_detail_view(request):
    obj=Product.objects.get(id=1)
    context ={
        "title":"my text",
        "description":[123,423,456]
    }
    return render(request, "detail.html",context)

def home_view(request,*args,**kwargs):
    my_context ={
        "my_text":"my text",
        "my_list":[123,423,456]
    }
    return render(request, "home.html",my_context)

def deviceAdmin_view(request,*args,**kwargs):
    return render(request, "deviceadmin.html", {})

   
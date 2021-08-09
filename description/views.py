from django.shortcuts import render

# Create your views here.

#  商城說明頁面
def description_views(request):
    return render(request, 'shop_description.html')
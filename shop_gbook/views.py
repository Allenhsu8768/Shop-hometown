from django.shortcuts import render

# Create your views here.

#  會員留言頁面
def shop_gbook_views(request):
    return render(request, 'shop_gbook.html')
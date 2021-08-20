from django.shortcuts import render
from test.models import Stock
# Create your views here.



def main_view(request) :
    # return render(request, 'test.html')
    # print(request.method)

    if request.method == "POST" :

        temp_1 = request.POST.get('test_stock_name')         # 데이터 가져오기 (name 입력)
        temp_2 = request.POST.get('test_stock_q')

        # DB 저장
        stock_name = Stock()
        stock_q = Stock()
        stock_name.text, stock_q.text= temp_1, temp_2

        stock_name.save()
        stock_q.save()

        return render(request, 'test.html', context = {'stock_name' : stock_name, 'stock_q' : stock_q})   # 데이터 반환하기

    else :
        return render(request, 'test.html', context = {'text' : 'method = get'})
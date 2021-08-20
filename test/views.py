from test.models import Stock
from django.shortcuts import render



def main_view(request) :
    # return render(request, 'test.html')
    # print(request.method)

    if request.method == "POST" :

        temp_1 = request.POST.get('test_stock_name')         # 데이터 가져오기 (name 입력)
        temp_2 = request.POST.get('test_stock_q')

        # DB 저장
        my_stock = Stock()
        my_stock.text, my_stock.volume = temp_1, temp_2

        my_stock.save()

        stock_list = Stock.objects.all()

        return render(request, 'test.html', context = {'stock_list' : stock_list} )  # 데이터 반환하기

    else :

        stock_list = Stock.objects.all()

        return render(request, 'test.html', context = {'stock_list' : stock_list} )
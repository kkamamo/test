import coffee_2
print("** 안녕하세요. GOO Coffee입니다.**")
order_list=[0,0,0]
stock = [10,10,10]
items=["아메리카노", "라떼", "핫초코"]
price = [3000,3500,4000]

select = 1
while select != 0:
    coffee_2.menu()
    select = int(input("메뉴를 선택하세요 : "))
    if select == 1:
        coffee_2.order_menu(items,price)
        coffee_2.order(items, price, order_list)
        coffee_2.result(items,order_list)
    elif select == 2:
        coffee_2.p(items,price,order_list)
    elif select == 3:
        coffee_2.m(items,price,order_list)
    else:
        print("서비스를 지원하지 않습니다.")

total_charge = 0
def menu():
    print()
    print("시스템 메뉴\n1. 주문\n2. 메뉴추가\n3. 메뉴삭제\n4. 재고 확인\n5. 재고 추가\n0. 종료")

def order_menu(items,price):
    print("주문 메뉴는 다음과 같습니다.")
    for i in range(len(items)):
        print(str(i+1)+".",items[i],price[i],"원")
    print("0. 주문 종료")
 
def order(items, price, order_list):
    global total_charge
    cof = 1
    while cof != 0:
        cof = int(input("주문하실 메뉴는? : "))
        if cof == 0:
            print("주문을 종료합니다.")
        elif cof > len(items):
            print("잘못 주문하였습니다.")
        elif cof <= len(items):
            total_charge += price[cof-1]
            order_list[cof-1] += 1

def result(items,order_list):
    global total_charge
    total_order = 0
    print("총 주문하신 커피는")
    for i in range(len(order_list)):
        if order_list[i] != 0:
            print(items[i], ":",order_list[i],"잔",end=" ")
            total_order += order_list[i]
        order_list[i] = 0
    print()
    print("총 금액은", total_charge,"원 입니다.")
    print("감사합니다.")
    total_charge = 0

def p(items,price,order_list):
    items.append(input("추가하실메뉴:"))
    price.append(int(input("가격:")))
    order_list.append(0)

def m(items,price,order_list):
    rm_data = input("삭제하실 메뉴는?")
    if rm_data not in items:
        print("메뉴가 없습니다.")
    else:
        index = items.index(rm_data)
        items.pop(index)
        price.pop(index)
        order_list.pop(index)
#def

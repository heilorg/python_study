# Write your code here :-)
price = int(input("물건 구매가를 입력해 주세요"));

discount_rate = 0;
if price >= 10000 and price < 50000 :
    discount_rate = 50
elif price >= 50000 and price < 300000 :
    discount_rate = 30
elif price >= 300000 :
    discount_rate = 10

discount_price = int(price * (discount_rate / 100));

pay = price - discount_price;

print("구매가 : " + str(price));
print("할인율 : " + str(discount_rate) + "%");
print("할인금액 : " + str(discount_price));
print("지불금액 : " + str(pay));

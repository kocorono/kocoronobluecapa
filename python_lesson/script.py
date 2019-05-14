# or -> 「条件1 or 条件2」のときはorを使う
time = 15
if time == 10 or time == 15:
    print('おやつの時間ですよ')


# not -> 「not条件式」にすると、条件式がTrueであれば「False」に、「False」であれば「True」になります。
time = 9
if not time == 18:
    print('まだ帰れねーって')

if time == 9:
    print('帰って良し')



















# inputカウントを使う
apple_price = 300
input_count = input('購入するりんごの個数を入力して:')
total_price = apple_price * int(input_count)
print('購入するりんごの個数は'+input_count+'個です')
print('支払い金額は'+str(total_price)+'円です')

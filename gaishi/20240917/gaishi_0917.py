#20240917 コーディングテストセミナー
#https://gaishishukatsu.com/archives/229972
#レストランの在庫会計の管理システム
#chatGPTに助けてもらった
          
class Restaurant:
    def __init__(self):
        self.stock = {} #在庫
        self.customers = {} #顧客
        self.orders = {} #注文
        self.sales = 0 #売上
    
    #納品リクエスト後の処理    
    def add_stock(self, menu, quantity, price):
        if menu in self.stock:
            self.stock[menu]['quantity'] += quantity
        else:
            self.stock[menu] = {'quantity': quantity, 'price': price}
    
    #来店リクエスト後の処理
    def visit(self, customer_id, people, customer_type):
        self.customers[customer_id] = {'people': people, 'type': customer_type}
        self.orders[customer_id] = []   
    
    #注文リクエスト後の処理
    def order(self, customer_id, menu, quantity):
        if menu not in self.stock: #メニューにない注文は何もしない
            return
        
        available_quantity = self.stock[menu]['quantity'] #注文可能な個数
        order_quantity = min(quantity, available_quantity) #注文個数を決定
        
        if order_quantity > 0:
            self.stock[menu]['quantity'] -= order_quantity #在庫を減らす
            self.orders[customer_id].append({'menu': menu, 'quantity': order_quantity, 'price': self.stock[menu]['price']})  

    #会計リクエスト後の処理
    def account(self, customer_id, time):
        customer = self.customers[customer_id]
        if customer['type'] == 'normal':
            total = sum(order['quantity'] * order['price'] for order in self.orders[customer_id])
        else:
            total = 5000 * customer['people'] #食べ放題
        
        #22時以降は10%増
        hour, minute, second = map(int, time.split(':'))
        if hour >= 22:
            total *= 1.10
        
        #売り上げに追加
        self.sales += total
        
    #売上
    def get_sales(self):
        return int(self.sales)
    
        
def process_requests(requests):
    restaurant = Restaurant() #インスタント化
    
    for request in requests:
        parts = request.split()
        time = parts[0]
        action = parts[1]
        
        #納品リクエスト　時刻　メニュー　個数　単価 
        if action == 'stock':
            menu = parts[2]
            quantity = int(parts[3])
            price = int(parts[4])
            restaurant.add_stock(menu, quantity, price)
        #来店リクエスト　時刻　客ID　人数　タイプ 
        elif action == 'visit':
            customer_id = int(parts[2])
            people = int(parts[3])
            customer_type = parts[4] #ノーマルか食べ放題か
            restaurant.visit(customer_id, people, customer_type)
        #注文リクエスト　時刻　客ID　メニュー　個数
        elif action == 'order':
            customer_id = int(parts[2])
            menu = parts[3]
            quantity = int(parts[4])
            restaurant.order(customer_id, menu, quantity)
        #会計リクエスト　時刻　客ID
        elif action == 'account':
            customer_id = int(parts[2])
            restaurant.account(customer_id, time)
    
    return restaurant.get_sales() #売上を返す



#標準入力　hh:mm:ss リクエスト種類
requests = []
while True:
    try:
        request = input()
        if request.strip() == "":
            break
        requests.append(request)
    except EOFError:
        break
    
#import sys #ファイル入力向け
#input = sys.stdin.read

#requests = input().strip().split('\n')

sales = process_requests(requests)
print(sales)           
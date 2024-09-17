#classの練習

#宣言
class PracticeClass: #クラス名の頭は大文字推奨
    #コンストラクタ・最初に宣言
    #def __init__(self): #変数の初期化・引数なし
    #    self.a = 0
    #    self.b = 0
        
    def __init__(self, a, b): #変数の初期化・引数あり
        #self.aとaは別物なので紐づけ
        self.a = a
        self.b = b
        
    def __del__(self): #デストラクタ・インスタンスが破棄された時の処理
        print("デストラクタされました")
    
    #メソッド    
    def multi(self):
        return self.a * self.b
    
#classの継承
class PracticeInh(PracticeClass): 
    #def __init__(self): #引数なし
    #    super().__init__() #super()で継承元のメソッドを呼び出し
    #    self.c = 2
        
    def __init__(self, a, b): #引数あり
        super().__init__(a, b)
        self.c = 2
        
    def frac(self):
        return self.a * self.b / self.c
    
#prac1 = PracticeClass() #インスタンス化・引数なし
#print(prac1.multi()) #メソッドを実行　出力は0
#prac1 = None #デストラクタが実行される

prac2 = PracticeClass(3, 4) #インスタンス化・引数あり
print(prac2.multi()) #メソッドを実行　出力は12

#prac3 = PracticeInh() #継承・引数なし
#print(prac3.frac()) #メソッドを実行　出力は0

prac4 = PracticeInh(3, 4) #継承・引数あり
print(prac4.frac()) #メソッドを実行　出力は6
print(prac4.multi()) #継承元のメソッドも実行可能　出力は12

#実行終了するとデストラクタ
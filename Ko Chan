# Ko-Chan Memory System (Logic)
class MyPrivateAI:
    def __init__(self):
        self.memory = {} # ဒါက မင်းရဲ့ မှတ်ဉာဏ်အကွက်

    def store_knowledge(self, key, value):
        # မြန်မာစာတွေကို ဒီမှာ တစ်သက်လုံး သိမ်းထားမယ်
        self.memory[key] = value
        print("မှတ်သားလိုက်ပြီ - " + key)

    def ask(self, query):
        # သိမ်းထားတဲ့ မှတ်ဉာဏ်ထဲက ပြန်ရှာပြီး ဖြေပေးမယ်
        return self.memory.get(query, "မသိသေးပါ၊ သင်ထပ်ပြောပြမှ မှတ်မိပါမယ်။")

# မင်းရဲ့ ကိုယ်ပိုင် AI ကို စသုံးခြင်း
my_ai = MyPrivateAI()
my_ai.store_knowledge("Python", "Python သည် ကုဒ်ရေးရလွယ်ကူပြီး အားကောင်းသော ဘာသာစကားဖြစ်သည်")
print(my_ai.ask("Python"))

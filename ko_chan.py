# Ko-Chan AI (Knowledge Reader)
def get_ai_response(user_query):
    try:
        # knowledge.txt ထဲက စာတွေကို ဖတ်ခြင်း
        with open("knowledge.txt", "r", encoding="utf-8") as f:
            knowledge = f.read()
        
        # မေးခွန်းကို အချက်အလက်ထဲမှာ ရှာခြင်း
        if user_query in knowledge:
            return f"ကျွန်ုပ်၏ မှတ်ဉာဏ်ထဲတွင် တွေ့ရှိသည်မှာ: {knowledge}"
        else:
            return "ကျွန်ုပ်၏ မှတ်ဉာဏ်ထဲတွင် အချက်အလက် မတွေ့ရှိပါ။ သင် ပိုမို ဖြည့်စွက်ပေးပါဦး။"
    except Exception as e:
        return "မှတ်ဉာဏ်ဖိုင် ဖတ်၍မရပါ။"

# စမ်းသပ်ခြင်း
query = "Python"
print(get_ai_response(query))

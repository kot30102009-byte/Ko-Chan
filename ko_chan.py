# Ko-Chan AI (Interactive Chat)
def get_ai_response(user_query):
    try:
        # knowledge.txt ကို utf-8 နဲ့ ဖတ်မယ်
        with open("knowledge.txt", "r", encoding="utf-8") as f:
            knowledge = f.read()
        
        if user_query in knowledge:
            return f"Ko-Chan မှတ်မိတယ်: {knowledge}"
        else:
            return "အဲ့ဒါကိုတော့ ကျွန်တော် မသိသေးပါဘူး။ knowledge.txt ထဲမှာ ထည့်ပေးပါ။"
    except Exception as e:
        return "မှတ်ဉာဏ်ဖိုင် ရှာမတွေ့ပါ သို့မဟုတ် ဖတ်၍မရပါ။"

print("Ko-Chan AI စနစ် စတင်ပြီ! (ထွက်ရန် 'bye' ဟု ရိုက်ပါ)")
while True:
    user_input = input("သင်: ")
    if user_input.lower() == 'bye':
        print("Ko-Chan: နောက်မှ ပြန်တွေ့မယ်!")
        break
    response = get_ai_response(user_input)
    print("Ko-Chan:", response)
    

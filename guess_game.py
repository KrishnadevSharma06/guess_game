import random

def guess_number():
    number = random.randint(1, 100)
    attempts = 0
    print("🤖 1 से 100 के बीच कोई संख्या सोची गई है।")
    
    while True:
        try:
            guess = int(input("अपना अनुमान लगाइए: "))
            attempts += 1
            
            if guess < number:
                print("⬆️ बहुत छोटा है! ऊपर जाइए।")
            elif guess > number:
                print("⬇️ बहुत बड़ा है! नीचे आइए।")
            else:
                print(f"🎉 सही! {attempts} प्रयासों में आपने संख्या {number} पकड़ ली।")
                break
        except ValueError:
            print("❌ कृपया एक वैध संख्या दर्ज करें।")

if __name__ == "__main__":
    guess_number()



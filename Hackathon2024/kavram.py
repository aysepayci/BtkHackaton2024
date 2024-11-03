import random

# Kazanım Kavrama Testleri Sınıfı
class TestGenerator:
    def __init__(self):
        self.questions = {
            "Python nedir?": "Python, çeşitli alanlarda kullanılan popüler bir programlama dilidir.",
            "Makine öğrenmesi ne işe yarar?": "Veri üzerinden tahmin yapmayı sağlar.",
            "Veri analitiği nedir?": "Veriden anlam çıkarmaya yarar.",
            "Yapay zeka nedir?": "Bilgisayarların insan benzeri zekayı taklit etme yeteneğidir.",
            "Veri bilimi nedir?": "Veri analizi ve modelleme süreçlerini içeren bir alandır."
        }
        self.score = 0

    def generate_test(self):
        print("\nKazanım Kavrama Testi:")
        questions_list = list(self.questions.keys())
        random.shuffle(questions_list)  # Soruları karıştır
        
        for i, question in enumerate(questions_list, 1):
            print(f"Soru {i}: {question}")
            answer = input("Cevabınızı yazın: ")
            self.check_answer(question, answer)

        print(f"\nToplam Puanınız: {self.score}/{len(questions_list)}")

    def check_answer(self, question, user_answer):
        correct_answer = self.questions[question]
        if user_answer.strip().lower() == correct_answer.lower():
            print("Doğru!")
            self.score += 1  # Doğru cevapta puan ekle
        else:
            print(f"Yanlış! Doğru cevap: {correct_answer}")

# Ana Program Akışı
def main():
    test_gen = TestGenerator()

    while True:
        print("\n1. Kazanım Kavrama Testi Yap")
        print("2. Çıkış")

        choice = input("Bir seçenek seçin: ")

        if choice == "1":
            test_gen.generate_test()
        elif choice == "2":
            print("Programdan çıkılıyor.")
            break
        else:
            print("Geçersiz seçenek. Tekrar deneyin.")

if __name__ == "__main__":
    main()

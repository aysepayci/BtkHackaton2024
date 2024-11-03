import random

# Başlangıç seviyesi
level = 1
correct_answers = 0
total_questions = 0

# Soru havuzu: Mantık, Bilim ve Teknoloji, Sanat ve Edebiyat
questions_pool = {
    "math": [
        (1, "5 + 7 nedir?", 12),
        (1, "9 - 3 nedir?", 6),
        (2, "20 * 2 nedir?", 40),
        (2, "40 / 8 nedir?", 5),
        (3, "42 + 23 nedir?", 65),
        (3, "81 - 39 nedir?", 42),
    ],
    "logic": [
        (1, "Bir elma ağacında 6 kırmızı elma ve 4 yeşil elma var. 3 kırmızı elma düşerse kaç kırmızı elma kalır?", 3),
        (2, "Bir gemide 20 koyun ve 10 inek var. Çoban kaç yaşında?", "Bilinemiyor"),
        (3, "Bir şey ne kadar çok alınırsa o kadar ağır, o kadar çok yer kaplar. Bu şey nedir?", "Su"),
    ],
    "science": [
        (1, "Güneş sisteminin merkezinde hangi gök cismi bulunur?", "Güneş"),
        (2, "Hangi gezegen halkalarıyla ünlüdür?", "Satürn"),
        (3, "İnsan vücudundaki en büyük organ hangisidir?", "Deri"),
    ],
    "art_literature": [
        (1, "Mona Lisa adlı eseri kim yaptı?", "Leonardo da Vinci"),
        (2, "Sherlock Holmes'un yaratıcısı olan yazar kimdir?", "Arthur Conan Doyle"),
        (3, "Don Kişot adlı romanın yazarı kimdir?", "Miguel de Cervantes"),
    ]
}

# Seviye ve kategoriye göre soru seçici
def select_question(level):
    available_questions = [
        q for category in questions_pool.values() for q in category if q[0] == level
    ]
    if available_questions:
        return random.choice(available_questions)
    return None

# Öğrenciye soruyu sor ve cevabı değerlendir
def ask_question(level):
    global correct_answers, total_questions
    question = select_question(level)
    
    if not question:
        print("Uygun seviye sorusu bulunamadı.")
        return False
    
    _, prompt, correct_answer = question
    
    # Soruyu sorma
    print(f"Soru {total_questions + 1}: {prompt}")
    
    user_answer = input("Cevabınız: ")
    
    # Cevapları kıyaslama (harf ve sayı formatına göre)
    try:
        if isinstance(correct_answer, int):
            user_answer = int(user_answer)
        elif isinstance(correct_answer, float):
            user_answer = float(user_answer)
    except ValueError:
        print("Geçersiz giriş.")
        return False

    # Doğru cevap kontrolü
    if user_answer == correct_answer:
        print("Doğru!")
        correct_answers += 1
        return True
    else:
        print(f"Yanlış. Doğru cevap: {correct_answer}.")
        return False

# Kişiselleştirilmiş öğrenme programı
def learning_program():
    global level, total_questions
    print("Kapsamlı Öğrenme Programına Hoş Geldiniz!")
    
    while total_questions < 10:  # Toplam 10 soru
        success = ask_question(level)
        total_questions += 1

        # Seviye ayarı
        if success:
            if correct_answers % 3 == 0 and level < 3:  # 3 doğru cevapta seviye artır
                level += 1
                print(f"Tebrikler! Seviyeniz {level} olarak yükseldi!")
        else:
            if correct_answers > 0 and level > 1:  # Yanlışta seviye düşür
                level -= 1
                print(f"Seviyeniz {level} olarak düşürüldü.")

    # Program sonucu
    print("\nProgram Sonu!")
    print(f"Toplam Doğru Cevap: {correct_answers}/{total_questions}")
    success_rate = (correct_answers / total_questions) * 100
    print(f"Başarı Oranı: %{success_rate:.2f}")

    if success_rate >= 80:
        print("Harika bir iş çıkardınız!")
    elif success_rate >= 50:
        print("İyi gidiyorsunuz, biraz daha pratik yapın!")
    else:
        print("Daha çok çalışmanız gerekiyor!")

# Programı başlat
learning_program()
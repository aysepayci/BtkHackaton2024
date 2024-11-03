import random

# Soruların havuzu
questions_pool = {
    "matematik": [
        (1, "5 + 3 kaçtır?", 8),
        (1, "12 - 4 kaçtır?", 8),
        (2, "15 x 3 kaçtır?", 45),
        (2, "100 ÷ 4 kaçtır?", 25)
    ],
    "tarih": [
        (1, "Türkiye Cumhuriyeti hangi yılda kuruldu?", 1923),
        (2, "Roma İmparatorluğu hangi yılda yıkıldı?", 476)
    ],
    "bilim": [
        (1, "Güneş sisteminin merkezindeki gök cismi nedir?", "güneş"),
        (2, "H2O nedir?", "su")
    ],
    "sanat": [
        (1, "Mona Lisa'nın ressamı kimdir?", "da vinci"),
        (2, "Sistine Şapeli'nin tavanını kim süslemiştir?", "michelangelo")
    ]
}

# Kullanıcı performansı
user_performance = {}
correct_answers = 0
total_questions = 0

def select_question(level):
    """Belirtilen seviyeye göre rastgele bir soru seçer."""
    available_questions = []
    for topic, questions in questions_pool.items():
        for question in questions:
            if question[0] == level:
                available_questions.append((topic, *question[1:]))  # topic, prompt, correct_answer
    return random.choice(available_questions) if available_questions else None

def ask_question(level):
    """Kullanıcıya soru sorar ve yanıtı kontrol eder."""
    global correct_answers, total_questions
    question = select_question(level)
    
    if not question:
        print("Uygun seviyede soru bulunamadı.")
        return False
    
    topic, prompt, correct_answer = question
    print(f"Soru {total_questions + 1} ({topic.capitalize()}): {prompt}")
    user_answer = input("Cevabınız: ").strip().lower()  # Küçük harfe dönüştür
    
    try:
        if isinstance(correct_answer, (int, float)):
            user_answer = float(user_answer)  # Matematiksel cevapsa sayıya çevir
        if user_answer == correct_answer:
            print("Doğru!")
            correct_answers += 1
            if topic not in user_performance:
                user_performance[topic] = {"correct": 0, "incorrect": 0}
            user_performance[topic]["correct"] += 1
            return True
        else:
            print(f"Yanlış. Doğru cevap: {correct_answer}.")
            if topic not in user_performance:
                user_performance[topic] = {"correct": 0, "incorrect": 0}
            user_performance[topic]["incorrect"] += 1
            return False
    except ValueError:
        print("Geçersiz giriş. Sayı girmeniz bekleniyordu.")
        if topic not in user_performance:
            user_performance[topic] = {"correct": 0, "incorrect": 0}
        user_performance[topic]["incorrect"] += 1
        return False

def learning_program():
    """Kullanıcının ilgi alanına göre öğrenme programını başlatır."""
    global correct_answers, total_questions
    print("Kişiselleştirilmiş Eğitim Programına Hoş Geldiniz!")
    
    topics_input = input("Hangi konularla ilgileniyorsunuz? Lütfen virgülle ayırarak seçin: ")
    selected_topics = [topic.strip().lower() for topic in topics_input.split(",")]
    
    # Başlangıç testiyle seviyeyi belirleme
    print("Başlangıç testiyle seviyenizi belirleyelim.")
    test_questions = [
        ("5 + 3 kaçtır?", 8),
        ("Güneş sisteminin merkezindeki gök cismi nedir?", "güneş"),
        ("Türkiye Cumhuriyeti hangi yılda kuruldu?", 1923)
    ]
    
    for prompt, correct_answer in test_questions:
        print(prompt)
        user_answer = input("Cevabınız: ").strip().lower()
        
        try:
            if isinstance(correct_answer, (int, float)):
                user_answer = float(user_answer)
            if user_answer == correct_answer:
                print("Doğru!")
                correct_answers += 1
            else:
                print(f"Yanlış. Doğru cevap: {correct_answer}.")
        except ValueError:
            print("Geçersiz giriş.")
    
    level = 1 if correct_answers < 2 else 2
    print(f"{'Orta' if level == 2 else 'Başlangıç'} seviyeden başlayacaksınız.")
    
    # Seçilen konular için soruları sorma
    total_questions = 0
    for topic in selected_topics:
        if topic in questions_pool:
            while total_questions < 5:  # Her konu için 5 soru sor
                ask_question(level)
                total_questions += 1
    
    # Performans raporu
    print("\nPerformans Raporu:")
    for topic, performance in user_performance.items():
        print(f"{topic.capitalize()}: Doğru: {performance['correct']}, Yanlış: {performance['incorrect']}")

# Programı çalıştır
if _name_ == "_main_":
    learning_program()
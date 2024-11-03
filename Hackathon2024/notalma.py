import nltk
from nltk.tokenize import sent_tokenize
from sklearn.feature_extraction.text import TfidfVectorizer
import numpy as np

# NLTK kütüphanesinin gerekli kaynaklarını indir
nltk.download('punkt', quiet=True)

# Notlar ve Özetleme
class NoteManager:
    def __init__(self):
        self.notes = []

    def take_note(self):
        note = input("Notunuzu girin: ")
        if note.strip():  # Not boş değilse
            self.notes.append(note)
            print("Not kaydedildi!")
        else:
            print("Boş not kaydedilemez.")

    def summarize_notes(self):
        if not self.notes:
            print("Özetlenecek not yok.")
            return None
        text = " ".join(self.notes)
        sentences = sent_tokenize(text)
        
        vectorizer = TfidfVectorizer()
        vectors = vectorizer.fit_transform(sentences)
        scores = vectors.toarray().sum(axis=1)
        
        # En yüksek puanlı cümleleri seçiyoruz
        summary_sentences = [sentences[i] for i in np.argsort(scores)[-3:]]
        summary = " ".join(summary_sentences)
        print("Not Özeti:\n", summary)
        return summary

# Ana Program Akışı
def main():
    note_manager = NoteManager()

    while True:
        print("\n1. Not Al")
        print("2. Notları Özetle")
        print("3. Çıkış")

        choice = input("Bir seçenek seçin: ")

        if choice == "1":
            note_manager.take_note()
        elif choice == "2":
            note_manager.summarize_notes()
        elif choice == "3":
            print("Programdan çıkılıyor.")
            break
        else:
            print("Geçersiz seçenek. Tekrar deneyin.")

if __name__ == "__main__":
    main()

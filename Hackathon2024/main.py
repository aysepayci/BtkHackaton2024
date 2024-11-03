import kavram 
import kisisellesitirlmis
import notalma
import ornek
import numpy as np
import nltk
from nltk.tokenize import sent_tokenize
from sklearn.feature_extraction.text import TfidfVectorizer
import random
def main():
    while True:
        print("\n1. Kazanım Kavrama Testi Yap")
        print("2. Not Yönetimi")
        print("3. Kişiselleştirilmiş Eğitim Programı")
        print("4. Çıkış")

        choice = input("Bir seçenek seçin: ")

        if choice == "1":
            notalma()
        elif choice == "2":
            kavram()
        elif choice == "3":
            ornek()
        elif choice == "4":
            print("Programdan çıkılıyor.")
            break
        else:
            print("Geçersiz seçenek. Tekrar deneyin.")

if __name__ == "__main__":
    main()
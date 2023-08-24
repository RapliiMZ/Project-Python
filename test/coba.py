import random

# Simpan pertanyaan dan jawaban dalam bentuk tuple (pertanyaan, jawaban)
pertanyaan_jawaban = [
    ("Apa ibu kota Indonesia?", "Jakarta"),
    ("Berapakah hasil dari 5 + 7?", "12"),
    ("Siapakah penemu gravitasi?", "Isaac Newton"),
    # Tambahkan pertanyaan dan jawaban lainnya di sini
]

while True:
    # Pilih pertanyaan secara acak
    pertanyaan, jawaban = random.choice(pertanyaan_jawaban)

    print("\nPertanyaan:")
    print(pertanyaan)
    user_jawaban = input("Jawaban: ")

    if user_jawaban.lower() == jawaban.lower():
        print("Jawaban Anda benar. Lanjut ke pertanyaan berikutnya.")
    else:
        print("Jawaban Anda salah. Silakan coba lagi.")
        continue

    lanjut = input("Lanjut ke pertanyaan berikutnya? (y/n): ")
    if lanjut.lower() != 'y':
        break

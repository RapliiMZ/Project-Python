import random

matematika = [("mtk soal 1","mtk jwbn1"),
              ("mtk soal 2","mtk jwbn2"),
              ("mtk soal 3","mtk jwbn3"),
              ("mtk soal 4","mtk jwbn4"),
              ("mtk soal 5","mtk jwbn5"),
              ]
fisika = [("fsk soal 1","fsk jwbn1"),
              ("fsk soal 2","fsk jwbn2"),
              ("fsk soal 3","fsk jwbn3"),
              ("fsk soal 4","fsk jwbn4"),
              ("fsk soal 5","fsk jwbn5"),
              ]
kimia = [("kma soal 1","kma jwbn1"),
              ("kma soal 2","kma jwbn2"),
              ("kma soal 3","kma jwbn3"),
              ("kma soal 4","kma jwbn4"),
              ("kma soal 5","kma jwbn5"),
              ]
biologi = [("blg soal 1","blg jwbn1"),
              ("blg soal 2","blg jwbn2"),
              ("blg soal 3","blg jwbn3"),
              ("blg soal 4","blg jwbn4"),
              ("blg soal 5","blg jwbn5"),
              ]


def main():
    while True :
        print("\nPilih Mapel:")
        print("1. Matematika")
        print("2. Fisika")
        print("3. Kimia")
        print("4. Biologi")
        print("5. Udahan")
        choice = input("Pilih MaPel: ")

        if choice == '1':
            soal_mtk, answer = random.choice(matematika)
            print("Jawablah soal ini: ")
            print(soal_mtk)
            answer_user = input("Jawaban: ")

            if answer_user.lower() == answer.lower():
                print("Jawaban anda benar")
            else :
                print("Jawaban anda salah")
                continue
            
            lanjut = input("CODE OTP: ")
            if lanjut.lower() == 'otp':
                break

        elif choice == '2':
            soal_fsk, answer = random.choice(fisika)
            print("Jawablah soal ini: ")
            print(soal_fsk)
            answer_user = input("Jawaban: ")
            
            if answer_user.lower() == answer.lower():
                print("Jawaban anda benar")
            else:
                print("Jawaban anda salah")
                continue

        elif choice == '3':
            soal_kma, answer = random.choice(kimia)
            print("Jawablah soal ini: ")
            print(soal_kma)
            answer_user = input("Jawaban: ")
            
            if answer_user.lower() == answer.lower():
                print("Jawaban anda benar")
            else:
                print("Jawaban anda salah")
                continue

        elif choice == '4':
            soal_blg, answer = random.choice(biologi)
            print("Jawablah soal ini: ")
            print(soal_blg)
            answer_user = input("Jawaban: ")

            if answer_user.lower() == answer.lower():
                print("Jawaban anda benar")
            else:
                print("Jawaban anda salah")
                continue

        elif choice == '5':
            print("Jangan lupa banyak berlatih ya...")
            break

        else:
            print("salah pilihan")

if "_main_":
    main()
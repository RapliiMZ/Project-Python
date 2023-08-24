import random
import string
import time

otp_length = 6
otp_data = {"otp": None, "expiry_time": None}

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

def generate_otp(length):
    char = string.digits
    otp = ''.join(random.choice(char) for _ in range(length))
    return otp

generated_otp = generate_otp(otp_length)

def generate_expiry_time():
    current_time = int(time.time())
    expiry_time = current_time + 24 * 60 * 60
    return expiry_time

def request_otp():
    otp = generate_otp(6)
    expiry_time = generate_expiry_time()
    otp_data["otp"] = otp
    otp_data["expiry_time"] = expiry_time
    return otp, expiry_time

def access_account(otp):
    if otp_data["otp"] == otp:
        if otp_data["expiry_time"] >= int(time.time()):
            return "Akses berhasil. Selamat datang!"
        else:
            return "OTP sudah kadaluarsa. Mohon minta OTP baru."
    else:
        return "Akses ditolak. Periksa kembali OTP."

def otpRun():
    while True :
        print("\nSilahkan Pilih: ")
        print("1. Nyalain PC")
        print("2. Keluar")
        choice = input("Pilih opsi: ")

        
        if choice == '1':
            otp, expiry_time = request_otp()
            print("Kode OTP anda: ", otp)
            print("berlaku sampai:", time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(expiry_time)))
            entered_otp = input("Masukan OTP: ")
            access_result = access_account(entered_otp)
            print(access_result)
            break
        elif choice == '2':
            print("Makasih bang")
            break
        else :
            print("warga mana lu!!!")

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
            
            if "__main__" :
                otpRun()
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

            if "__main__" :
                otpRun()
                break

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

            if "__main__" :
                otpRun()
                break

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

            if "__main__" :
                otpRun()
                break

        elif choice == '5':
            print("Jangan lupa banyak berlatih ya...")
            break

        else:
            print("salah pilihan")

if "_main_":
    main()
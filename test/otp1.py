import random
import string
import time

otp_length = 6
otp_data = {"otp": None, "expiry_time": None}

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

if "_main_":
    otpRun()
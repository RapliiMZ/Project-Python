import random
import string
import time
import tkinter as tk
from tkinter import messagebox

otp_length = 4
otp_data = {"otp": None, "expiry_time": None}
root = tk.Tk()

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

def generate_expiry_time():
    current_time = int(time.time())
    expiry_time = current_time + 24 * 60 * 60
    return expiry_time

def reroot_otp():
    otp = generate_otp(4)
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
    def submit_otp():
        entered_otp = otp_entry.get()
        access_result = access_account(entered_otp)
        messagebox.showinfo("Hasil Akses", access_result)


    otp, expiry_time = reroot_otp()

    messagebox.showinfo("kode otp anda:", otp)
    messagebox.showinfo("berlaku:", time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(expiry_time)))

    otp_window = tk.Toplevel()
    otp_window.title("Verifikasi OTP")
    center_window(otp_window, width=1000, height=500)

    label = tk.Label(otp_window, text="Masukkan Kode OTP Anda:")
    label.pack(pady=10)

    otp_entry = tk.Entry(otp_window)
    otp_entry.pack(pady=5)

    submit_button = tk.Button(otp_window, text="Submit", command=lambda: (submit_otp(), otp_window.destroy()))
    submit_button.pack(pady=10)



def center_window(root, width, height):
    screen_width = root.winfo_screenwidth()
    screen_height = root.winfo_screenheight()
    
    x_coordinate = (screen_width - 1000) // 2
    y_coordinate = (screen_height - 500) // 2
    
    root.geometry(f"{1000}x{500}+{x_coordinate}+{y_coordinate}")

def main():
    def start_quiz(subject):
        def check_answer():
            user_answer = answer_entry.get()
            if user_answer.lower() == answer.lower():
                messagebox.showinfo("hasil", "Jawaban anda benar")
                print(otpRun())
            else:
                messagebox.showinfo("Hasil", "Jawaban Anda salah!")

        question, answer = random.choice(subject)
        root = tk.Toplevel()
        root.title("Jawablah soal ini!")
        root.resizable(False,False)
        center_window(root, width=1000, height=500)

        question_label = tk.Label(root, text=question) 
        question_label.pack(pady=10)

        answer_label = tk.Label(root, text="Jawaban:")
        answer_label.pack()

        answer_entry = tk.Entry(root)
        answer_entry.pack(pady=5)

        submit_button = tk.Button(root, text="Submit", command=check_answer, width=20, height=2)
        submit_button.pack(pady=10)

    root.title("Ultrasonic for LIfe")
    root.resizable(False,False)
    center_window(root, width=1000, height=500)

    label = tk.Label(root, text="Pilih Mapel:")
    label.pack(pady=10, padx=10, fill="x", expand=True)

    mtk_button = tk.Button(root, text="Matematika", command=lambda: start_quiz(matematika), width=20, height=2)
    mtk_button.pack(pady=3, padx=10, expand=True)

    fsk_button = tk.Button(root, text="Fisika", command=lambda: start_quiz(fisika), width=20, height=2)
    fsk_button.pack(pady=3, padx=10, expand=True)

    kma_button = tk.Button(root, text="Kimia", command=lambda: start_quiz(kimia), width=20, height=2)
    kma_button.pack(pady=3, padx=10, expand=True)

    blg_button = tk.Button(root, text="Biologi", command=lambda: start_quiz(biologi), width=20, height=2)
    blg_button.pack(pady=3, padx=10, expand=True)

    quit_button = tk.Button(root, text="Keluar", command=root.destroy, width=20, height=2)
    quit_button.pack(pady=3, padx=10, expand=True)

    root.mainloop()

if __name__ == "__main__":
    main()

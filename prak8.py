import tkinter as tk
from tkinter import messagebox
import sqlite3

# 1. Inisialisasi Database
def create_db():
    conn = sqlite3.connect('nilai_siswa.db')
    cursor = conn.cursor()
    cursor.execute('''
                CREATE TABLE IF NOT EXISTS nilai_siswa
                (id INTEGER PRIMARY KEY AUTOINCREMENT,
                nama_siswa TEXT NOT NULL,
                biologi INTEGER NOT NULL,
                fisika INTEGER NOT NULL,
                inggris INTEGER NOT NULL,
                prediksi_fakultas TEXT NOT NULL)''')
    
    conn.commit()
    conn.close()

create_db()



# 2. Logika Prediksi
def prediksi_fakultas(biologi, fisika, inggris):
    if biologi > fisika and biologi > inggris:
        return "Kedokteran"
    elif fisika > biologi and fisika > inggris:
        return "Teknik"
    elif inggris > biologi and inggris > fisika:
        return "Bahasa"
    else:
        return "Tidak Dapat Ditentukan"


# 3. Fungsi Submit Nilai
def submit_nilai():
    nama = entry_nama.get().strip()
    try:
        bio = int(entry_bio.get())
        fis = int(entry_fis.get())
        ing = int(entry_ing.get())
    except ValueError:
        messagebox.showerror("Error", "Nilai harus berupa angka!")
        return

    if not nama:
        messagebox.showerror("Error", "Nama siswa tidak boleh kosong!")
        return

    hasil_prediksi = prediksi_fakultas(bio, fis, ing)
   # Simpan ke Database 
  conn = sqlite3.connect("nilai_siswa.db")
    cursor = conn.cursor()
    cursor.execute(
        """
        INSERT INTO nilai_siswa (nama_siswa, biologi, fisika, inggris, prediksi_fakultas)
        VALUES (?, ?, ?, ?, ?)
    """,
        (nama, bio, fis, ing, hasil_prediksi),
    )
    conn.commit()
    conn.close()


 # Tampilkan Hasil
   messagebox.showinfo("Hasil Prediksi", f"Prediksi Fakultas: {hasil_prediksi}")


 # Reset Form Input
   entry_nama.delete(0, tk.END)
    entry_bio.delete(0, tk.END)
    entry_fis.delete(0, tk.END)
    entry_ing.delete(0, tk.END)


# 4. Fungsi Hover Tombol
def on_enter(e):
    btn_submit["bg"] = "#e50fa7"
    btn_submit["fg"] = "black"

def on_leave(e):
    btn_submit["bg"] = "#644475"
    btn_submit["fg"] = "white"
    
# 5. Layout GUI Tkinter
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
root = tk.Tk()
root.title("Aplikasi Prediksi Fakultas")
root.geometry("320x240")
root.configure(padx=20, pady=20)

tk.Label(root, text="Nama Siswa:").grid(row=0, column=0, sticky="w", pady=5)
entry_nama = tk.Entry(root)
entry_nama.grid(row=0, column=1, pady=5)

tk.Label(root, text="Nilai Biologi:").grid(row=1, column=0, sticky="w", pady=5)
entry_bio = tk.Entry(root)
entry_bio.grid(row=1, column=1, pady=5)

tk.Label(root, text="Nilai Fisika:").grid(row=2, column=0, sticky="w", pady=5)
entry_fis = tk.Entry(root)
entry_fis.grid(row=2, column=1, pady=5)

tk.Label(root, text="Nilai Inggris:").grid(row=3, column=0, sticky="w", pady=5)
entry_ing = tk.Entry(root)
entry_ing.grid(row=3, column=1, pady=5)

btn_submit = tk.Button(
    root,
    text="Submit",
    command=submit_nilai,
    bg="#644475",
    fg="black",
    width=15,
)
btn_submit.grid(row=4, column=0, columnspan=2, pady=15)

btn_submit.bind("<Enter>", on_enter)
btn_submit.bind("<Leave>", on_leave)

root.mainloop()
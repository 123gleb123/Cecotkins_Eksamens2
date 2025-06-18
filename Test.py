import tkinter as tk
from tkinter import messagebox

jautajumi = [
    {
        "jautajums": "Ko dara cikls 'for' Python valodā?",
        "varianti": [
            "Izpilda kodu vienu reizi",
            "Atkārto kodu noteiktu reižu skaitu",
            "Pastāvīgi pārbauda nosacījumu",
            "Darbojas bezgalīgi"
        ],
        "atbilde": 1
    },
    {
        "jautajums": "Kurš atslēgvārds tiek izmantots, lai sāktu 'for' ciklu Python valodā?",
        "varianti": ["loop", "while", "for", "repeat"],
        "atbilde": 2
    },
    {
        "jautajums": "Kurā gadījumā 'for' cikls neko neizpildīs?",
        "varianti": [
            "for i in range(0):",
            "for i in range(1):",
            "for i in range(2):",
            "for i in range(5):"
        ],
        "atbilde": 0
    },
    {
        "jautajums": "Kas notiks, izpildot šo kodu?\n\nfor i in range(3):\n    if i == 1:\n        break\n    print(i)",
        "varianti": [
            "0 1 2",
            "1 2",
            "0",
            "0 1"
        ],
        "atbilde": 2
    },
    {
        "jautajums": "Ko izvadīs: for i in range(3): print(i)?",
        "varianti": ["0 1 2", "1 2 3", "0 1 2 3", "3 2 1"],
        "atbilde": 0
    },
    {
        "jautajums": "Cik reizes tiks izpildīts cikls?\n\nfor i in range(4):\n    print(\"Hello\")",
        "varianti": [
            "3",
            "4",
            "5",
            "0"
        ],
        "atbilde": 1
    },
    {
        "jautajums": "Kas tiks izvadīts?\n\nfor i in range(5):\n    if i % 2 == 0:\n        continue\n    print(i, end=' ')",
        "varianti": [
            "1 2 3 4",
            "0 2 4",
            "1 3",
            "0 1 2 3 4"
        ],
        "atbilde": 2
    },
    {
        "jautajums": "Kurš no šiem variantiem korekti izmanto 'for' ciklu?",
        "varianti": [
            "for i to 10:",
            "for i < 10:",
            "for i in range(10):",
            "for range i (10):"
        ],
        "atbilde": 2
    },
    {
        "jautajums": "Kas notiek, ja 'for' ciklā tiek izmantots 'break'?",
        "varianti": [
            "Turpina ciklu",
            "Iziet no cikla",
            "Izlaiž vienu iterāciju",
            "Izraisa kļūdu"
        ],
        "atbilde": 1
    },
    {
        "jautajums": "Ko dara 'continue' ciklā 'for'?",
        "varianti": [
            "Pāriet uz nākamo iterāciju",
            "Apstādina ciklu",
            "Restartē ciklu",
            "Beidz programmu"
        ],
        "atbilde": 0
    }
]


class Test:

    def __init__(self, root):
        self.root = root
        self.root.title("Python programmēšanas valodas for cikla tests")
        self.root.geometry("600x400")
        self.root.configure(bg="#2E2E2E")

        self.jaut_index = 0
        self.score = 0
        self.user_atb = []

        self.varianti_var = tk.IntVar()
        self.radio_buttons = []

        self.menu()

    def clear_window(self):
        for widget in self.root.winfo_children():
            widget.destroy()

    def menu(self):
        self.clear_window()
        tk.Label(self.root, text="Python programmēšanas valodas for cikla tests", font=("Arial", 20, "bold"),
                 fg="white", bg="#2E2E2E").pack(pady=20)

        tk.Button(self.root, text="Sākt pildit tesu", command=self.play_game, font=("Arial", 14, "bold"),
                  bg="#1F1F1F", fg="white", padx=20, pady=10).pack(pady=15)

        tk.Button(self.root, text="Par tesu", command=self.par_testu, font=("Arial", 14, "bold"),
                  bg="#5E4B8B", fg="white", padx=20, pady=10).pack(pady=15)

        tk.Button(self.root, text="Iziet", command=self.root.quit, font=("Arial", 14, "bold"),
                  bg="#D32F2F", fg="white", padx=20, pady=10).pack(pady=15)

    def par_testu(self):
        self.clear_window()
        tk.Label(self.root, text="Par testu", font=("Arial", 18, "bold"), fg="white", bg="#2E2E2E").pack(pady=20)

        test_info = (
            "Šis tests paredzēts, lai pārbaudītu zināšanas par for cikla \n"
            "darbību Python programmēšanas valodā. Jautājumi aptver\n"
            "sintakses pamatus, darbu ar range() funkciju, kā arī break un\n"
            "continue operatoru izmantošanu."
        )

        tk.Label(self.root, text=test_info, font=("Arial", 14), fg="white", bg="#2E2E2E", wraplength=500, justify="left").pack(pady=15)

        tk.Button(self.root, text="Atgriezties uz galveno izvēlni", command=self.menu,
                  font=("Arial", 14, "bold"), bg="#388E3C", fg="white", padx=20, pady=10).pack(pady=10)
        
    def play_game(self):
        self.clear_window()
        self.jaut_index = 0
        self.score = 0
        self.user_atb = []

        self.jaut_label = tk.Label(self.root, text="", font=("Arial", 14), wraplength=400, justify="left", bg="#2E2E2E", fg="white")
        self.jaut_label.pack(pady=20)

        self.options_var = tk.IntVar()
        self.radio_buttons = []
        for i in range(4):
            rb = tk.Radiobutton(self.root, text="", variable=self.options_var, value=i, font=("Arial", 12),
                                bg="#2E2E2E", fg="white", selectcolor="#444444")
            rb.pack(anchor="w", padx=20)
            self.radio_buttons.append(rb)

        self.next_button = tk.Button(self.root, text="Next", command=self.nak_jautajums,
                                     font=("Arial", 12, "bold"), bg="#4CAF50", fg="white", padx=10, pady=5)
        self.next_button.pack(pady=10)

        self.paradi_jautajumi()

    def paradi_jautajumi(self):
        q = jautajumi[self.jaut_index]
        self.jaut_label.config(text=f"Q{self.jaut_index + 1}: {q['jautajums']}")
        self.options_var.set(-1)
        for i, option in enumerate(q["varianti"]):
            self.radio_buttons[i].config(text=option)

    def nak_jautajums(self):
        izveleti = self.options_var.get()
        if izveleti == -1:
            messagebox.showwarning("Uzmanību", "Lūdzu, izvēlies atbildes variantu.")
            return

        pareizi = izveleti == jautajumi[self.jaut_index]["atbilde"]
        self.user_atb.append((izveleti, pareizi))
        if pareizi:
            self.score += 1

        self.jaut_index += 1
        if self.jaut_index < len(jautajumi):
            self.paradi_jautajumi()
        else:
            self.paradi_result()

    def paradi_result(self):
        result_text = f"Tu atbildēji pareizi uz {self.score} no {len(jautajumi)} jautājumiem!\n\n"
        for idx, (ans, correct) in enumerate(self.user_atb):
            q = jautajumi[idx]
            result_text += f"Jautajums{idx + 1}: {q['jautajums']}\n"
            result_text += f"  Tava atbilde: {q['varianti'][ans]}\n"
            if correct:
                result_text += "Pareizi!\n"
            else:
                result_text += f" Nepareizi. Pareizā atbilde: {q['varianti'][q['atbilde']]}\n"
            result_text += "\n"

        messagebox.showinfo("Tests pabeigts", result_text)
        self.root.quit()

    

root = tk.Tk()
app = Test(root)
root.mainloop()

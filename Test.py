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


root = tk.Tk()
app = Test(root)
root.mainloop()

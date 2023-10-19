import tkinter as tk

def calculate_levels():
    level = int(level_entry.get())
    bet = int(bet_entry.get())
    lev = 1

    result_label.config(text=f"Nyeremény: {bet}, nyerési esély: {100 - (100 / (level + 1))}%")

    while level > 1:
        bet = 2 * bet
        lev = lev + 1
        level -= 1

        level_info_label.config(text=f"{lev}. szint: bet:{bet}")

# Létrehozunk egy ablakot
window = tk.Tk()
window.title("Szerencsejáték Számológép")

# Szint beviteli mező
level_label = tk.Label(window, text="Add meg, hány szintes legyen:")
level_label.pack()
level_entry = tk.Entry(window)
level_entry.pack()

# Nyeremény beviteli mező
bet_label = tk.Label(window, text="Add meg a nyerni kívánt összeget:")
bet_label.pack()
bet_entry = tk.Entry(window)
bet_entry.pack()

# Számítás gomb
calculate_button = tk.Button(window, text="Számol", command=calculate_levels)
calculate_button.pack()

# Eredmény kiírás helye
result_label = tk.Label(window, text="")
result_label.pack()

# Szintek információja
level_info_label = tk.Label(window, text="")
level_info_label.pack()

# Ablak megjelenítése
window.mainloop()

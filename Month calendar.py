import tkinter as tk
import calendar

def show_calendar():
    year = int(year_var.get())
    month = months.index(month_var.get()) + 1
    cal_text = calendar.month(year, month)
    text.delete(1.0, tk.END)
    text.insert(tk.END, cal_text)


window = tk.Tk()
window.title("Month Calendar")
window.geometry("400x300")

months = list(calendar.month_name)[1:]  
years = [str(y) for y in range(2000, 2030)] 

month_var = tk.StringVar(value="August")
year_var = tk.StringVar(value="2025")

tk.Label(window, text="Select Month:").pack(pady=5)
tk.OptionMenu(window, month_var, *months).pack(pady=5)

tk.Label(window, text="Select Year:").pack(pady=5)
tk.OptionMenu(window, year_var, *years).pack(pady=5)

tk.Button(window, text="Show Calendar", command=show_calendar).pack(pady=10)

text = tk.Text(window, height=10, width=30)
text.pack()

window.mainloop()
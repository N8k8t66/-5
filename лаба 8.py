import tkinter as tk
from tkinter import messagebox, filedialog
import csv

class CarRentalApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Аренда авто")
        self.contracts = []
        
        self.create_widgets()
    
    def create_widgets(self):
        tk.Label(self.root, text="Номер договора:").pack()
        self.num_entry = tk.Entry(self.root)
        self.num_entry.pack()
        
        tk.Label(self.root, text="Клиент:").pack()
        self.client_entry = tk.Entry(self.root)
        self.client_entry.pack()
        
        tk.Label(self.root, text="Тип авто:").pack()
        self.car_entry = tk.Entry(self.root)
        self.car_entry.pack()
        
        tk.Label(self.root, text="Срок (дни):").pack()
        self.days_entry = tk.Entry(self.root)
        self.days_entry.pack()
    
        tk.Button(self.root, text="Добавить", command=self.add_contract).pack()
        tk.Button(self.root, text="Загрузить", command=self.load_file).pack()
        tk.Button(self.root, text="Сохранить", command=self.save_file).pack()
        tk.Button(self.root, text="Статистика по авто", command=self.show_car_stats).pack()
        tk.Button(self.root, text="Статистика по клиентам", command=self.show_client_stats).pack()
    
        self.listbox = tk.Listbox(self.root, width=50)
        self.listbox.pack()
    
    def add_contract(self):
        num = self.num_entry.get()
        client = self.client_entry.get()
        car = self.car_entry.get()
        days = self.days_entry.get()
        
        if not (num and client and car and days):
            messagebox.showerror("Ошибка", "Заполните все поля!")
            return
        
        if not days.isdigit():
            messagebox.showerror("Ошибка", "Срок должен быть числом!")
            return
        
        self.contracts.append((num, client, car, days))
        self.listbox.insert(tk.END, f"{num}: {client} - {car} ({days} дней)")
        
        self.num_entry.delete(0, tk.END)
        self.client_entry.delete(0, tk.END)
        self.car_entry.delete(0, tk.END)
        self.days_entry.delete(0, tk.END)
    
    def load_file(self):
        filename = filedialog.askopenfilename(filetypes=[("CSV файлы", "*.csv")])
        if not filename:
            return
        
        try:
            with open(filename, 'r') as file:
                reader = csv.reader(file)
                self.contracts = []
                self.listbox.delete(0, tk.END)
                for row in reader:
                    if len(row) == 4:
                        self.contracts.append(tuple(row))
                        self.listbox.insert(tk.END, f"{row[0]}: {row[1]} - {row[2]} ({row[3]} дней)")
            messagebox.showinfo("Успех", "Данные загружены!")
        except:
            messagebox.showerror("Ошибка", "Не удалось загрузить файл")
    
    def save_file(self):
        if not self.contracts:
            messagebox.showerror("Ошибка", "Нет данных для сохранения")
            return
        
        filename = filedialog.asksaveasfilename(defaultextension=".csv")
        if not filename:
            return
        
        try:
            with open(filename, 'w', newline='') as file:
                writer = csv.writer(file)
                for contract in self.contracts:
                    writer.writerow(contract)
            messagebox.showinfo("Успех", "Данные сохранены!")
        except:
            messagebox.showerror("Ошибка", "Не удалось сохранить файл")
    
    def show_car_stats(self):
        if not self.contracts:
            messagebox.showinfo("Инфо", "Нет данных для анализа")
            return
        
        car_stats = {}
        for contract in self.contracts:
            car_type = contract[2]
            car_stats[car_type] = car_stats.get(car_type, 0) + 1
        
        result = "Статистика по типам авто:\n"
        for car, count in car_stats.items():
            result += f"{car}: {count} договоров\n"
            messagebox.showinfo("Статистика", result)
    
    def show_client_stats(self):
        if not self.contracts:
            messagebox.showinfo("Инфо", "Нет данных для анализа")
            return
            
        client_stats = {}
        for contract in self.contracts:
            client = contract[1]
            client_stats[client] = client_stats.get(client, 0) + 1
            
        result = "Статистика по клиентам:\n"
        for client, count in client_stats.items():
            result += f"{client}: {count} договоров\n"
            
            messagebox.showinfo("Статистика", result)

root = tk.Tk()
app = CarRentalApp(root)
root.mainloop()
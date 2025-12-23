import tkinter as tk
from tkinter import ttk, messagebox, scrolledtext
import os

# File paths
EMPLOYEES_FILE = "employees.txt"
PAYROLL_FILE = "payroll.txt"

# HRA percentage (20% of basic salary)
HRA_PERCENTAGE = 0.20

# FILE OPERATIONS 

def load_employees():
    """Load employees from file"""
    employees = []
    if os.path.exists(EMPLOYEES_FILE):
        with open(EMPLOYEES_FILE, 'r') as f:
            for line in f:
                line = line.strip()
                if line:
                    parts = line.split(',')
                    if len(parts) == 3:
                        employees.append({
                            'id': parts[0],
                            'name': parts[1],
                            'basic_salary': float(parts[2])
                        })
    return employees

def save_employees(employees):
    """Save employees to file"""
    with open(EMPLOYEES_FILE, 'w') as f:
        for emp in employees:
            f.write(f"{emp['id']},{emp['name']},{emp['basic_salary']}\n")

def save_payroll_record(emp_id, name, month, year, basic, hra, gross):
    """Append payroll record to file"""
    with open(PAYROLL_FILE, 'a') as f:
        f.write(f"{emp_id},{name},{month},{year},{basic},{hra},{gross}\n")

def load_payroll_records():
    """Load all payroll records"""
    records = []
    if os.path.exists(PAYROLL_FILE):
        with open(PAYROLL_FILE, 'r') as f:
            for line in f:
                line = line.strip()
                if line:
                    parts = line.split(',')
                    if len(parts) == 7:
                        records.append({
                            'emp_id': parts[0],
                            'name': parts[1],
                            'month': parts[2],
                            'year': parts[3],
                            'basic': float(parts[4]),
                            'hra': float(parts[5]),
                            'gross': float(parts[6])
                        })
    return records

def calculate_salary(basic_salary):
    """Calculate HRA and Gross Salary"""
    hra = basic_salary * HRA_PERCENTAGE
    gross = basic_salary + hra
    return hra, gross

#GUI APPLICATION 

def create_main_window():
    """Create the main application window"""
    root = tk.Tk()
    root.title("Payroll Management System")
    root.geometry("900x600")
    root.configure(bg='#f0f0f0')
    
    # Title
    title_label = tk.Label(root, text="PAYROLL MANAGEMENT SYSTEM", 
                          font=("Arial", 20, "bold"), bg='#2c3e50', fg='white', pady=15)
    title_label.pack(fill=tk.X)
    
    # Button Frame
    button_frame = tk.Frame(root, bg='#f0f0f0', pady=20)
    button_frame.pack()
    
    # Buttons
    btn_style = {'font': ('Arial', 11), 'width': 25, 'height': 2, 'bg': '#3498db', 'fg': 'white', 'relief': 'raised'}
    
    tk.Button(button_frame, text="Add Employee", command=lambda: add_employee_window(root), **btn_style).grid(row=0, column=0, padx=10, pady=5)
    tk.Button(button_frame, text="View All Employees", command=lambda: view_all_employees_window(root), **btn_style).grid(row=0, column=1, padx=10, pady=5)
    tk.Button(button_frame, text="Search Employee", command=lambda: search_employee_window(root), **btn_style).grid(row=1, column=0, padx=10, pady=5)
    tk.Button(button_frame, text="Process Payroll", command=lambda: process_payroll_window(root), **btn_style).grid(row=1, column=1, padx=10, pady=5)
    tk.Button(button_frame, text="Employee Payroll History", command=lambda: employee_history_window(root), **btn_style).grid(row=2, column=0, padx=10, pady=5)
    tk.Button(button_frame, text="Monthly Payroll Report", command=lambda: monthly_report_window(root), **btn_style).grid(row=2, column=1, padx=10, pady=5)
    
    exit_btn_style = btn_style.copy()
    exit_btn_style['bg'] = '#e74c3c'
    tk.Button(button_frame, text="Exit", command=root.quit, **exit_btn_style).grid(row=3, column=0, columnspan=2, pady=20)
    
    # Footer
    footer_label = tk.Label(root, text="Simple Payroll Management System | HRA: 20% of Basic Salary", 
                           font=("Arial", 9), bg='#34495e', fg='white', pady=10)
    footer_label.pack(side=tk.BOTTOM, fill=tk.X)
    
    return root

# ADD EMPLOYEE WINDOW 

def add_employee_window(parent):
    """Window to add new employee"""
    window = tk.Toplevel(parent)
    window.title("Add Employee")
    window.geometry("400x300")
    window.configure(bg='#ecf0f1')
    
    tk.Label(window, text="Add New Employee", font=("Arial", 16, "bold"), bg='#ecf0f1').pack(pady=20)
    
    # Form Frame
    form_frame = tk.Frame(window, bg='#ecf0f1')
    form_frame.pack(pady=10)
    
    tk.Label(form_frame, text="Employee ID:", font=("Arial", 11), bg='#ecf0f1').grid(row=0, column=0, sticky='w', pady=10, padx=10)
    emp_id_entry = tk.Entry(form_frame, font=("Arial", 11), width=25)
    emp_id_entry.grid(row=0, column=1, pady=10)
    
    tk.Label(form_frame, text="Name:", font=("Arial", 11), bg='#ecf0f1').grid(row=1, column=0, sticky='w', pady=10, padx=10)
    name_entry = tk.Entry(form_frame, font=("Arial", 11), width=25)
    name_entry.grid(row=1, column=1, pady=10)
    
    tk.Label(form_frame, text="Basic Salary:", font=("Arial", 11), bg='#ecf0f1').grid(row=2, column=0, sticky='w', pady=10, padx=10)
    salary_entry = tk.Entry(form_frame, font=("Arial", 11), width=25)
    salary_entry.grid(row=2, column=1, pady=10)
    
    def save_employee():
        emp_id = emp_id_entry.get().strip()
        name = name_entry.get().strip()
        salary_str = salary_entry.get().strip()
        
        if not emp_id or not name or not salary_str:
            messagebox.showerror("Error", "All fields are required!")
            return
        
        try:
            salary = float(salary_str)
            if salary <= 0:
                messagebox.showerror("Error", "Salary must be positive!")
                return
        except ValueError:
            messagebox.showerror("Error", "Invalid salary amount!")
            return
        
        employees = load_employees()
        
        # Check duplicate ID
        for emp in employees:
            if emp['id'] == emp_id:
                messagebox.showerror("Error", "Employee ID already exists!")
                return
        
        employees.append({'id': emp_id, 'name': name, 'basic_salary': salary})
        save_employees(employees)
        
        messagebox.showinfo("Success", f"Employee '{name}' added successfully!")
        window.destroy()
    
    tk.Button(window, text="Save Employee", command=save_employee, 
             font=("Arial", 12), bg='#27ae60', fg='white', width=20, height=2).pack(pady=20)

#  VIEW ALL EMPLOYEES WINDOW 

def view_all_employees_window(parent):
    """Window to view all employees"""
    window = tk.Toplevel(parent)
    window.title("All Employees")
    window.geometry("700x500")
    window.configure(bg='#ecf0f1')
    
    tk.Label(window, text="All Employees", font=("Arial", 16, "bold"), bg='#ecf0f1').pack(pady=20)
    
    employees = load_employees()
    
    if not employees:
        tk.Label(window, text="No employees found!", font=("Arial", 12), bg='#ecf0f1').pack(pady=20)
        return
    
    # Create Treeview
    frame = tk.Frame(window)
    frame.pack(pady=10, padx=20, fill=tk.BOTH, expand=True)
    
    tree = ttk.Treeview(frame, columns=("ID", "Name", "Basic Salary"), show='headings', height=15)
    tree.heading("ID", text="Employee ID")
    tree.heading("Name", text="Name")
    tree.heading("Basic Salary", text="Basic Salary")
    
    tree.column("ID", width=150, anchor='center')
    tree.column("Name", width=300, anchor='w')
    tree.column("Basic Salary", width=150, anchor='center')
    
    for emp in employees:
        tree.insert("", tk.END, values=(emp['id'], emp['name'], f"₹{emp['basic_salary']:.2f}"))
    
    scrollbar = ttk.Scrollbar(frame, orient=tk.VERTICAL, command=tree.yview)
    tree.configure(yscroll=scrollbar.set)
    scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
    tree.pack(fill=tk.BOTH, expand=True)

# SEARCH EMPLOYEE WINDOW 

def search_employee_window(parent):
    """Window to search employee"""
    window = tk.Toplevel(parent)
    window.title("Search Employee")
    window.geometry("500x400")
    window.configure(bg='#ecf0f1')
    
    tk.Label(window, text="Search Employee", font=("Arial", 16, "bold"), bg='#ecf0f1').pack(pady=20)
    
    search_frame = tk.Frame(window, bg='#ecf0f1')
    search_frame.pack(pady=10)
    
    tk.Label(search_frame, text="Employee ID:", font=("Arial", 11), bg='#ecf0f1').pack(side=tk.LEFT, padx=5)
    search_entry = tk.Entry(search_frame, font=("Arial", 11), width=20)
    search_entry.pack(side=tk.LEFT, padx=5)
    
    result_frame = tk.Frame(window, bg='white', relief=tk.RIDGE, bd=2)
    result_frame.pack(pady=20, padx=40, fill=tk.BOTH, expand=True)
    
    result_label = tk.Label(result_frame, text="", font=("Arial", 11), bg='white', justify=tk.LEFT)
    result_label.pack(pady=20, padx=20)
    
    def search():
        emp_id = search_entry.get().strip()
        if not emp_id:
            messagebox.showerror("Error", "Please enter Employee ID!")
            return
        
        employees = load_employees()
        found = None
        for emp in employees:
            if emp['id'] == emp_id:
                found = emp
                break
        
        if found:
            result_text = f"Employee Found!\n\n"
            result_text += f"ID: {found['id']}\n"
            result_text += f"Name: {found['name']}\n"
            result_text += f"Basic Salary: ₹{found['basic_salary']:.2f}"
            result_label.config(text=result_text, fg='green')
        else:
            result_label.config(text="Employee not found!", fg='red')
    
    tk.Button(search_frame, text="Search", command=search, 
             font=("Arial", 10), bg='#3498db', fg='white', width=10).pack(side=tk.LEFT, padx=5)

#PROCESS PAYROLL WINDOW 

def process_payroll_window(parent):
    """Window to process payroll"""
    window = tk.Toplevel(parent)
    window.title("Process Payroll")
    window.geometry("600x500")
    window.configure(bg='#ecf0f1')
    
    tk.Label(window, text="Process Payroll", font=("Arial", 16, "bold"), bg='#ecf0f1').pack(pady=20)
    
    # Input Frame
    input_frame = tk.Frame(window, bg='#ecf0f1')
    input_frame.pack(pady=10)
    
    tk.Label(input_frame, text="Employee ID:", font=("Arial", 11), bg='#ecf0f1').grid(row=0, column=0, sticky='w', pady=10, padx=10)
    emp_id_entry = tk.Entry(input_frame, font=("Arial", 11), width=20)
    emp_id_entry.grid(row=0, column=1, pady=10)
    
    tk.Label(input_frame, text="Month (1-12):", font=("Arial", 11), bg='#ecf0f1').grid(row=1, column=0, sticky='w', pady=10, padx=10)
    month_entry = tk.Entry(input_frame, font=("Arial", 11), width=20)
    month_entry.grid(row=1, column=1, pady=10)
    
    tk.Label(input_frame, text="Year:", font=("Arial", 11), bg='#ecf0f1').grid(row=2, column=0, sticky='w', pady=10, padx=10)
    year_entry = tk.Entry(input_frame, font=("Arial", 11), width=20)
    year_entry.grid(row=2, column=1, pady=10)
    
    # Result Frame
    result_frame = tk.Frame(window, bg='white', relief=tk.RIDGE, bd=2)
    result_frame.pack(pady=20, padx=40, fill=tk.BOTH, expand=True)
    
    result_text = scrolledtext.ScrolledText(result_frame, font=("Courier", 10), height=10, width=60)
    result_text.pack(pady=10, padx=10)
    
    def process():
        emp_id = emp_id_entry.get().strip()
        month = month_entry.get().strip()
        year = year_entry.get().strip()
        
        if not emp_id or not month or not year:
            messagebox.showerror("Error", "All fields are required!")
            return
        
        try:
            month_num = int(month)
            if month_num < 1 or month_num > 12:
                messagebox.showerror("Error", "Month must be between 1-12!")
                return
        except ValueError:
            messagebox.showerror("Error", "Invalid month!")
            return
        
        employees = load_employees()
        employee = None
        for emp in employees:
            if emp['id'] == emp_id:
                employee = emp
                break
        
        if not employee:
            messagebox.showerror("Error", "Employee not found!")
            return
        
        basic = employee['basic_salary']
        hra, gross = calculate_salary(basic)
        
        # Display result
        result = "="*50 + "\n"
        result += "SALARY BREAKDOWN\n"
        result += "="*50 + "\n"
        result += f"Employee ID: {employee['id']}\n"
        result += f"Name: {employee['name']}\n"
        result += f"Month/Year: {month}/{year}\n"
        result += "-"*50 + "\n"
        result += f"Basic Salary: ₹{basic:.2f}\n"
        result += f"HRA (20%): ₹{hra:.2f}\n"
        result += "-"*50 + "\n"
        result += f"Gross Salary: ₹{gross:.2f}\n"
        result += "="*50 + "\n"
        
        result_text.delete(1.0, tk.END)
        result_text.insert(1.0, result)
        
        # Save to file
        save_payroll_record(emp_id, employee['name'], month, year, basic, hra, gross)
        messagebox.showinfo("Success", "Payroll processed successfully!")
    
    tk.Button(window, text="Process Payroll", command=process, 
             font=("Arial", 12), bg='#27ae60', fg='white', width=20, height=2).pack(pady=10)

#EMPLOYEE PAYROLL HISTORY WINDOW 

def employee_history_window(parent):
    """Window to view employee payroll history"""
    window = tk.Toplevel(parent)
    window.title("Employee Payroll History")
    window.geometry("800x500")
    window.configure(bg='#ecf0f1')
    
    tk.Label(window, text="Employee Payroll History", font=("Arial", 16, "bold"), bg='#ecf0f1').pack(pady=20)
    
    search_frame = tk.Frame(window, bg='#ecf0f1')
    search_frame.pack(pady=10)
    
    tk.Label(search_frame, text="Employee ID:", font=("Arial", 11), bg='#ecf0f1').pack(side=tk.LEFT, padx=5)
    emp_id_entry = tk.Entry(search_frame, font=("Arial", 11), width=20)
    emp_id_entry.pack(side=tk.LEFT, padx=5)
    
    # Treeview Frame
    tree_frame = tk.Frame(window)
    tree_frame.pack(pady=10, padx=20, fill=tk.BOTH, expand=True)
    
    tree = ttk.Treeview(tree_frame, columns=("Month", "Year", "Basic", "HRA", "Gross"), show='headings', height=12)
    tree.heading("Month", text="Month")
    tree.heading("Year", text="Year")
    tree.heading("Basic", text="Basic Salary")
    tree.heading("HRA", text="HRA")
    tree.heading("Gross", text="Gross Salary")
    
    tree.column("Month", width=100, anchor='center')
    tree.column("Year", width=100, anchor='center')
    tree.column("Basic", width=150, anchor='center')
    tree.column("HRA", width=150, anchor='center')
    tree.column("Gross", width=150, anchor='center')
    
    scrollbar = ttk.Scrollbar(tree_frame, orient=tk.VERTICAL, command=tree.yview)
    tree.configure(yscroll=scrollbar.set)
    scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
    tree.pack(fill=tk.BOTH, expand=True)
    
    def view_history():
        emp_id = emp_id_entry.get().strip()
        if not emp_id:
            messagebox.showerror("Error", "Please enter Employee ID!")
            return
        
        # Clear existing data
        for item in tree.get_children():
            tree.delete(item)
        
        records = load_payroll_records()
        emp_records = [r for r in records if r['emp_id'] == emp_id]
        
        if not emp_records:
            messagebox.showinfo("Info", "No payroll records found for this employee!")
            return
        
        for record in emp_records:
            tree.insert("", tk.END, values=(
                record['month'], 
                record['year'], 
                f"₹{record['basic']:.2f}",
                f"₹{record['hra']:.2f}",
                f"₹{record['gross']:.2f}"
            ))
    
    tk.Button(search_frame, text="View History", command=view_history, 
             font=("Arial", 10), bg='#3498db', fg='white', width=12).pack(side=tk.LEFT, padx=5)

#MONTHLY PAYROLL REPORT WINDOW

def monthly_report_window(parent):
    """Window to view monthly payroll report"""
    window = tk.Toplevel(parent)
    window.title("Monthly Payroll Report")
    window.geometry("900x600")
    window.configure(bg='#ecf0f1')
    
    tk.Label(window, text="Monthly Payroll Report", font=("Arial", 16, "bold"), bg='#ecf0f1').pack(pady=20)
    
    search_frame = tk.Frame(window, bg='#ecf0f1')
    search_frame.pack(pady=10)
    
    tk.Label(search_frame, text="Month (1-12):", font=("Arial", 11), bg='#ecf0f1').pack(side=tk.LEFT, padx=5)
    month_entry = tk.Entry(search_frame, font=("Arial", 11), width=10)
    month_entry.pack(side=tk.LEFT, padx=5)
    
    tk.Label(search_frame, text="Year:", font=("Arial", 11), bg='#ecf0f1').pack(side=tk.LEFT, padx=5)
    year_entry = tk.Entry(search_frame, font=("Arial", 11), width=10)
    year_entry.pack(side=tk.LEFT, padx=5)
    
    # Treeview Frame
    tree_frame = tk.Frame(window)
    tree_frame.pack(pady=10, padx=20, fill=tk.BOTH, expand=True)
    
    tree = ttk.Treeview(tree_frame, columns=("Emp ID", "Name", "Basic", "HRA", "Gross"), show='headings', height=15)
    tree.heading("Emp ID", text="Emp ID")
    tree.heading("Name", text="Name")
    tree.heading("Basic", text="Basic Salary")
    tree.heading("HRA", text="HRA")
    tree.heading("Gross", text="Gross Salary")
    
    tree.column("Emp ID", width=100, anchor='center')
    tree.column("Name", width=250, anchor='w')
    tree.column("Basic", width=150, anchor='center')
    tree.column("HRA", width=150, anchor='center')
    tree.column("Gross", width=150, anchor='center')
    
    scrollbar = ttk.Scrollbar(tree_frame, orient=tk.VERTICAL, command=tree.yview)
    tree.configure(yscroll=scrollbar.set)
    scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
    tree.pack(fill=tk.BOTH, expand=True)
    
    total_label = tk.Label(window, text="", font=("Arial", 12, "bold"), bg='#ecf0f1')
    total_label.pack(pady=10)
    
    def view_report():
        month = month_entry.get().strip()
        year = year_entry.get().strip()
        
        if not month or not year:
            messagebox.showerror("Error", "Please enter both month and year!")
            return
        
        # Clear existing data
        for item in tree.get_children():
            tree.delete(item)
        
        records = load_payroll_records()
        monthly_records = [r for r in records if r['month'] == month and r['year'] == year]
        
        if not monthly_records:
            messagebox.showinfo("Info", f"No payroll records found for {month}/{year}!")
            total_label.config(text="")
            return
        
        total_gross = 0
        for record in monthly_records:
            tree.insert("", tk.END, values=(
                record['emp_id'], 
                record['name'], 
                f"₹{record['basic']:.2f}",
                f"₹{record['hra']:.2f}",
                f"₹{record['gross']:.2f}"
            ))
            total_gross += record['gross']
        
        total_label.config(text=f"Total Gross Salary: ₹{total_gross:.2f}")
    
    tk.Button(search_frame, text="View Report", command=view_report, 
             font=("Arial", 10), bg='#3498db', fg='white', width=12).pack(side=tk.LEFT, padx=5)

#MAIN

def main():
    """Main application"""
    root = create_main_window()
    root.mainloop()

if __name__ == "__main__":
    main()
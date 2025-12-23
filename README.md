# Employee Payroll System

A simple Python-based payroll system application with console and GUI interfaces.

## 📋 Overview

This system helps manage employee payroll by calculating salaries, maintaining records, and generating reports. Built with Python and Tkinter.

## ✨ Features

- **Add Employees** - Store employee ID, name, and basic salary
- **View Employees** - Display all employees in a table
- **Search** - Find employees by ID
- **Process Payroll** - Calculate monthly salaries (Basic + HRA)
- **View History** - Check payroll history for any employee
- **Monthly Reports** - Generate reports for specific months

### Salary Calculation
```
HRA = 20% of Basic Salary
Gross Salary = Basic Salary + HRA
```

## 🚀 Quick Start

### Requirements
- Python 3.6+
- tkinter (usually comes with Python)

### Run the Application

**GUI Version:**
```bash
python payroll.py
```

**Console Version:**
```bash
python payroll_system.py
```

**OOP Console Version:**
```bash
python payroll_system_oop.py
```

## 📁 Project Structure

```
├── payroll.py                 # GUI version (main)
├── payroll_system.py          # Console version (procedural)
├── payroll_system_oop.py      # Console version (OOP)
├── employees.txt              # Employee data storage
├── payroll.txt                # Payroll records
└── README.md
```

## 💾 Data Storage

**employees.txt** - CSV format:
```
emp_id,name,basic_salary
E001,John Doe,50000.0
```

**payroll.txt** - CSV format:
```
emp_id,name,month,year,basic,hra,gross
E001,John Doe,12,2024,50000.0,10000.0,60000.0
```

## 🎯 How It Works

1. **Add Employee** → Enter details → Saved to `employees.txt`
2. **Process Payroll** → Select employee + month/year → Calculate salary → Save to `payroll.txt`
3. **View Reports** → Query by employee or month → Display results

## 🖼️ Screenshots

### Main Menu
- 6 functional buttons for different operations
- Clean, professional interface

### Features
- Add/view/search employees
- Process monthly payroll
- View detailed salary breakdowns
- Generate reports with totals

## 🛠️ Technical Details

### Technologies Used
- **Python 3** - Core programming language
- **Tkinter** - GUI framework
- **CSV Files** - Data persistence

### Code Versions
1. **Procedural** (`payroll_system.py`) - Functions-based approach
2. **OOP** (`payroll_system_oop.py`) - Class-based design with:
   - Employee class
   - PayrollRecord class
   - FileManager class
   - EmployeeManager class
   - PayrollManager class
3. **GUI** (`payroll.py`) - Tkinter interface

## 📚 What I Learned

- File I/O operations in Python
- Building GUI applications with Tkinter
- Data validation and error handling
- Converting procedural code to OOP
- Working with CSV file formats
- Creating user-friendly interfaces

## 🔄 Development Process

1. ✅ Planned features and requirements
2. ✅ Built console version with functions
3. ✅ Refactored to OOP design
4. ✅ Created GUI with Tkinter
5. ✅ Added validation and error handling
6. ✅ Tested all features

## 🎓 Key Concepts Applied

- Functions and modular code
- Object-oriented programming
- File handling
- GUI development
- Input validation
- Data structures (lists, dictionaries)

## 🚧 Future Improvements

- Database integration (SQLite)
- Employee update/delete functionality
- Tax calculations
- PDF salary slip generation
- Export to Excel
- User authentication


## 👤 Author

Created as a learning project to practice Python programming and GUI development.

---

**Made with Python 🐍 and Tkinter**

# 🤙Contact

Feel free to connect with me on [LinkedIn](https://www.linkedin.com/in/amit-kumar-maurya-b23281253) or reach out if you have questions or feedback!
Test update from responsiveness branch

# Basic File Handling Application 📄

A Python CLI application for reading, modifying, and creating text files with robust error handling.
Built as **Task 3** for **Saiket Systems Python Development Internship**.

---

## 📸 Project Preview

### Main Menu
![Main Menu](screenshots/1_main_menu.png)

### Read File Operation
![Read File](screenshots/2_read_file.png)

### Create Sample File
![Create Sample File](screenshots/3_sample_file_created.png)

### Find & Replace Operation
![Find & Replace](screenshots/4_find_and_replace.png)

### File Information
![File Info](screenshots/5_file_info.png)

### Create Custom File
![Create Custom File](screenshots/6_custom_file.png)

---

## ✨ Features

✅ **Read Files** - Display file content with error handling
✅ **Find & Replace** - Search and replace words in files
✅ **File Information** - View file size and properties
✅ **Create Sample Files** - Demo file with pre-written content
✅ **Create Custom Files** - Create files with your own content
✅ **Robust Error Handling** - Handles FileNotFoundError, PermissionError, IOError
✅ **User-Friendly Menu** - Interactive CLI interface

---

## 💻 Technical Stack

- **Language:** Python 3.x
- **Concepts:**
  - File I/O operations
  - Exception handling (try-except)
  - String manipulation
  - Object-Oriented Programming (Classes)
  - User input validation

---

## 🚀 How to Run

```bash
# Clone the repository
git clone https://github.com/khushirai2216-boop/Basic-File-Handling.git
cd Basic-File-Handling

# Run the application
python basic_file_handling.py
```

---

## 📖 How to Use

### **Option 1: Read File**
- View the complete content of any file
- Handles missing files gracefully

**Screenshot:** See "Read File Operation" above

### **Option 2: Find & Replace**
- Find specific words in a file
- Replace with new words
- Save changes or discard

**Screenshot:** See "Find & Replace Operation" above

### **Option 3: File Information**
- View filename
- Check file size in bytes and KB
- Verify if file exists

**Screenshot:** See "File Information" above

### **Option 4: Create Sample File**
- Creates a demo file with Python-related content
- Useful for testing features

**Screenshot:** See "Create Sample File" above

### **Option 5: Create Custom File**
- Create your own file with custom content
- Line-by-line input
- Type 'END' to finish

**Screenshot:** See "Create Custom File" above

### **Option 6: Exit**
- Gracefully close the application

---

## 🎯 Example Workflow
FILE HANDLING APPLICATION

Saiket Systems - Python Development Internship
Enter filename: myfile.txt
MENU OPTIONS

Read file
Find and replace word
Display file information
Create sample file (for testing)
Create custom file
Exit

Choice: 5

Enter file name: myfile.txt
Enter file content:

Line 1: Hello World

Line 2: This is my file

Line 3: END
✓ File 'myfile.txt' created successfully!
Choice: 2

Find: Hello

Replace with: Hi

Save changes? (y/n): y

✓ File updated successfully!

---

## 🔑 Key Concepts Implemented

| Concept | Implementation |
|---------|-----------------|
| **File I/O** | `open()`, `read()`, `write()` with context managers |
| **Exception Handling** | FileNotFoundError, PermissionError, IOError, Exception |
| **String Methods** | `count()`, `replace()`, `strip()`, `upper()` |
| **OOP** | FileHandler class with methods |
| **Data Validation** | Input checks for empty content, missing words |
| **User Interaction** | Menu-driven interface with error messages |

---

## 📊 Code Structure
basic_file_handling.py

├── FileHandler (class)

│   ├── init(filename)

│   ├── read_file()

│   ├── find_and_replace(content, find_word, replaced_word)

│   ├── write_file(content)

│   └── display_file_info()

│

├── create_sample_file(filename)

├── create_custom_file(filename)

└── main()

---

## 🎓 Learning Outcomes

✅ File handling with Python (reading, writing, creating)
✅ Exception handling for different error scenarios
✅ String manipulation and text processing
✅ Object-Oriented Programming (classes and methods)
✅ Menu-driven application design
✅ Input validation and error management
✅ User experience design (CLI)

---

## 💡 Future Enhancements

- [ ] Add file backup functionality
- [ ] Implement undo/redo operations
- [ ] Add search with case sensitivity options
- [ ] Support for multiple file formats (CSV, JSON, etc.)
- [ ] File encryption/decryption
- [ ] GUI version using tkinter
- [ ] Batch file operations
- [ ] File comparison tool

---

## 📄 License

This project is licensed under the MIT License - see the LICENSE file for details.

---

## 👨‍💼 About

Built as **Task 3** of **Saiket Systems Python Development Internship**

**Skills Demonstrated:**
- Python Programming
- File I/O Operations
- Error Handling & Debugging
- OOP Principles
- Problem Solving
- Code Documentation

---

## 🔗 Related Projects

- [Task 1: To-Do List Application](https://github.com/khushirai2216-boop/To-Do_List_app)
- [Task 2: Number Guessing Game](https://github.com/khushirai2216-boop/Number-Guessing-Game)

---
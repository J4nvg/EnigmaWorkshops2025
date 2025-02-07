# Workshop 1
# **What is an IDE?**

An **IDE (Integrated Development Environment)** consists of three key parts:

🔹 **I - Integrated**: Combines multiple tools into a single interface.

🔹 **D - Development**: Supports coding, testing, and debugging.

🔹 **E - Environment**: Provides a structured workspace with everything needed to build software.

So, an **IDE is an environment where a developer can create, manage, and debug code efficiently, with all necessary tools in one place.** 🚀

🔹 Popular IDEs:

- **PyCharm** (Great for Python projects, debugging, and project structuring)
- **VSCode** (Lightweight, flexible, great extensions)

---

## **Why Use an IDE Instead of a Simple Text Editor?**

Text editors like Notepad or Vim let you write code, but **IDEs provide much more**:

| Feature | Text Editor | IDE |
| --- | --- | --- |
| Code Highlighting | ✅ | ✅ |
| Auto-Completion | ❌ | ✅ |
| Debugging Tools | ❌ | ✅ |
| Virtual Environments | ❌ | ✅ |
| Version Control Integration | ❌ | ✅ |

---

# **Getting Started: Setting Up Your Project**

### **Step 1: Create a New Project in PyCharm**

1️⃣ Open **PyCharm** → Click **New Project**

2️⃣ Select a folder for your project

3️⃣ Choose a **Python Interpreter** (venv, Conda, or system Python)

4️⃣ Click **Create** 🎉

---

# **Using Virtual Environments (venv)**

👨‍💻 A **virtual environment** keeps your dependencies separate from the system Python, avoiding conflicts between projects.

### **How to Set Up a venv in PyCharm**

1. When creating a project, select **"New Virtual Environment"**
2. Choose **venv** and set the location (default is fine)
3. Click **Create** – PyCharm will set up everything for you!

To manually create one:

```bash
python -m venv venv
source venv/bin/activate  # Mac/Linux
venv\\Scripts\\activate  # Windows
```

🔹 Use **venv** to keep each project isolated!

---

# **File System: Good Practices for Project Organization**

**Why does structure matter?**

✅ Makes code easier to navigate

✅ Prevents duplicate or messy files

✅ Helps debugging and collaboration

### **Example Folder Structure for a Python Project**

```
my_project/
│── data/               # Store datasets
│── src/                # Main source code
│   ├── __init__.py     # Marks it as a Python package
│   ├── utils.py        # Helper functions
│── main.py             # Main script (outside of the source code!)
│── tests/              # Unit tests
│── venv/               # Virtual environment
│── requirements.txt    # Dependencies
│── README.md           # Project description

```

🔹 **Tip:** Keep your files **modular** (one purpose per file).

---

# **Debugging: Finding & Fixing Bugs Efficiently**

Debugging in an IDE like PyCharm makes it **faster and easier** than just using `print()` statements.

### **Example: Debugging a Simple Python Script**

We started with this code:

```python
from random import randint

def GenerateRandomNumber(upper):
    return randint(1, upper)

def main():
    num1 = GenerateRandomNumber(10)
    num2 = GenerateRandomNumber(10)
    result = num1 + num2
    ans = input(f"What is {num1} + {num2}? ")

    if ans == result:  # 🚨 Bug here! `ans` is a string
        print("Correct!")
    else:
        print("Try again!")

main()

```

### **What Went Wrong?**

🤔 **Bug:** `ans` is a **string**, but `result` is an **integer**, so the comparison `ans == result` **always fails**.

### **Fix:** Convert `ans` to an integer

```python
if int(ans) == result:
```

---

# **Using the Debugger in PyCharm**

✅ Set **breakpoints** to pause execution at key points.

✅ Use **Step Over** and **Step Into** to control execution.

✅ Check **variable values** in real-time.

### **How to Debug in PyCharm**

1️⃣ **Set a Breakpoint**: Click in the **gutter (left margin)** of the editor.

2️⃣ **Run in Debug Mode**: Click the **🐞 Debug button** instead of Run.

3️⃣ **Step Through the Code**:

- 🏃 **Step Over (F8)**: Run one line at a time.
- 🔍 **Step Into (F7)**: Go inside a function call.
- ↩️ **Step Out (Shift+F8)**: Exit the function.
4️⃣ **Inspect Variables**: See real-time values in the Debugger pane.

🔹 **Using PyCharm’s Debugger = Faster bug fixes** 🚀

---

# **Final Tips & Next Steps**

✅ Use an **IDE** to improve efficiency and code structure.

✅ Set up a **virtual environment** to avoid dependency issues.

✅ Follow **good project organization** for maintainability.

✅ **Use PyCharm’s Debugger** to find and fix bugs efficiently.

### **Where to Go Next?**

📖 **Learn More:**

- [PyCharm Documentation](https://www.jetbrains.com/help/pycharm/)
- [Follow all the Enigma workshops](https://github.com/J4nvg/EnigmaWorkshops2025)

🎯 **Next Steps**:

- Try **debugging your own script** in PyCharm!
- Explore **GitHub** for version control.
- Learn **Docker** to make your projects portable.

🚀 Happy Coding!
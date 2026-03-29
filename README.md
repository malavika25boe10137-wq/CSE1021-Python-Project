# CSE1021-Python-Project
# Community Shop Inventory & Alert System

### 1. Project Overview & Significance
The **Community Shop Inventory & Alert System** is a purposeful Python application designed to solve a common problem faced by small-scale grocery vendors. In many communities, shopkeepers rely on manual, paper-based tracking, which frequently leads to "stock-outs" of essential daily goods like milk or bread. 

This project provides a digital solution that allows shopkeepers to track daily sales interactively and automatically generates a "Restock Report" whenever an item's quantity falls below a critical threshold. By digitizing this process, the system helps prevent revenue loss and ensures the community has consistent access to necessary supplies.

### 2. Scope of the Project
Understanding the scope ensures the system is used effectively within its designed parameters:

* **In-Scope (Current Functionalities):**
    * **Real-time Tracking:** Tracking daily sales of core household essentials.
    * **Automated Alerting:** Identifying items that fall below a minimum safety stock (5 units).
    * **Data Validation:** Handling user input errors (non-numeric data) to prevent system crashes.
    * **Reporting:** Generating a concise restock list and a full inventory status summary.
* **Out-of-Scope (Future Enhancements):**
    * **Persistent Storage:** This version uses RAM-based storage; data resets when the program closes. Integration with `.txt` or `.csv` files is a planned future update.
    * **Payment Integration:** The system tracks stock quantity only and does not process financial transactions or taxes.
    * **Multi-user Support:** Designed for a single terminal/shopkeeper use case.

### 3. Academic Context (CSE1021)
This project serves as a comprehensive application of the **CSE1021: Introduction to Problem Solving and Programming** syllabus. 
* **Control Flow:** Implements `while` loops and conditional branching (`if-elif-else`) for dynamic user interaction.
* **Data Structures:** Uses **Python Dictionaries** for efficient inventory lookups and **Sets** for mandatory duplicate removal.
* **Error Handling:** Employs `try-except` blocks to manage non-numeric inputs, ensuring program robustness.
* **Logic:** Follows a **Top-Down Design** methodology, breaking the problem into Input, Processing, and Output modules.

### 4. Technical Setup & Installation
To run this project, you must have **Python 3.x** installed. The system relies entirely on standard Python modules.

1.  **Download:** Save `inventory_system.py` to your local machine.
2.  **Navigate:** Open your terminal/command prompt and navigate to the file's folder.
3.  **Execute:** Run the program by typing:
    ```bash
    python inventory_system.py
    ```

### 5. How to Use the System
1.  **Enter Item:** Type the name of the item sold (e.g., `Milk`). The system is case-insensitive.
2.  **Enter Quantity:** Input the number of units sold. If you enter an invalid character, the error handling logic will prompt a retry.
3.  **Finalize:** Once the shift is over, type **`done`** to trigger the final analysis.
4.  **Review:** Review the **Restock Report** and full inventory update.

### 6. Key Features
* **Case Standardization:** Automatically handles inputs like "milk" or "mILK" using `.capitalize()`.
* **Input Validation:** Prevents crashes from non-numeric data using `try-except` blocks.
* **Real-time Logic:** Subtracts sales and flags "LOW" status immediately.
* **Duplicate Removal:** Uses set operations to ensure the Restock Report is unique and actionable.

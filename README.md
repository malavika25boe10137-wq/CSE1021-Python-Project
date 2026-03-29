# CSE1021-Python-Project

# Community Shop Inventory & Alert System

### Project Overview
The **Community Shop Inventory & Alert System** is a purposeful Python application designed to solve a common problem faced by small-scale  grocery vendors in local neighborhoods. In many communities, shopkeepers rely on manual, paper-based tracking, which frequently leads to "stock-outs" of essential daily goods like milk or bread. This project provides a digital solution that allows shopkeepers to track daily sales interactively and automatically generates a "Restock Report" whenever an item's quantity falls below a critical threshold. By abstracting the programming tasks involved in inventory management , this system helps prevent revenue loss and ensures the community has consistent access to necessary supplies

### Academic Context
This project serves as a comprehensive application of the **CSE1021: Introduction to Problem Solving and Programming** utilizes fundamental algorithm design techniques to analyze and solve a real-world computing problem. The implementation demonstrates proficiency in representing compound data using Python lists and dictionaries, implementing control flow through iteration and conditional statements , and applying array techniques for data integrity—such as the removal of duplicate entries. It follows the "Top-Down Design" methodology for algorithm implementation as taught in the course's core modules.

### Key Features and Functionalities
* **Interactive Sales Logging:** A dynamic `while` loop allows users to enter multiple sales entries in one session.
* **Robust Data Validation:** The system uses `try-except` blocks to handle non-numeric inputs, ensuring the program does not crash during a busy shift.
* **Case-Insensitive Input:** The program automatically standardizes item names (e.g., converting "milk" or "mILK" to "Milk"), preventing duplicate entries in the inventory dictionary.
* **Automated Alert Logic:** Uses conditional branching (`if-elif-else`) to immediately flag items that fall below the minimum stock threshold.
* **Comprehensive Reporting:** Generates a dual report—a specific "Restock List" for urgent orders and a "Full Inventory Status" for general oversight.

### Technical Setup and Installation
To run this project, you must have **Python 3.x** installed on your computer. No external libraries or third-party tools are required, as the system relies entirely on standard Python modules and built-in data structures. 

1.  **Download the Code:** Download the `inventory_system.py` file from this repository and place it in a dedicated folder.
2.  **Open Terminal:** Navigate to the folder containing the file using your command prompt or terminal.
3.  **Execute the Program:** Type `python inventory_system.py` and press Enter. 
4.  **Interactive Mode:** The program will start in interactive mode, providing immediate feedback for every command entered.

### How to Use the System
Upon starting the program, you will interact with a pre-defined list of common household items such as Milk, Bread, and Rice. The system will prompt you to enter the name of an item sold; if the item is not in the system, it will alert you to try again. After entering a valid item, you will be asked for the quantity sold. You can continue logging items until the shift is over, at which point typing **"done"** will trigger the final analysis. The program then iterates through the entire inventory, identifies items that have fallen below the **Minimum Threshold of 5 units**, and displays a clear "Restock Report" alongside a full status update of all current stock levels.

### Logic and Troubleshooting
The system is built on a "Top-Down" architectural model. If you encounter an error where an item is not being recognized, ensure that the item exists in the initial `inventory` dictionary at the top of the script. The system includes a "Removal of Duplicates" algorithm to ensure that the final restock report is concise and accurate, even if multiple sales for the same item were recorded throughout the day.

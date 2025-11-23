# Expense-Tracker
The Personal Finance &amp; Expense Tracker is a simple offline Python GUI application that helps users record daily expenses, view summaries, track category-wise spending, and export data. It provides an easy, clean, and user-friendly way to manage personal finances.

# Personal Finance & Expense Tracker (Offline)

## Overview
A single-file Python desktop app to track Income and Expenses. Uses Tkinter for GUI, SQLite for local storage, and matplotlib for charts. Runs offline — perfect for Visual Studio Code.

## Features
- Add Income/Expense transactions with date, category and description.
- Persistent local storage using SQLite (finance.db).
- Transactions table with sorting, filtering, and delete.
- Monthly summary and embedded Income vs Expense chart.
- Export to Excel (optional, requires pandas & openpyxl).
- Backup local database.

## Requirements
- Python 3.8+
- Recommended packages:
  - pandas (optional, for export): `pip install pandas`
  - matplotlib (for charts): `pip install matplotlib`
  - openpyxl (if exporting Excel with pandas): `pip install openpyxl`

## Run
1. Save the script as `expense_tracker.py`.
2. Open terminal in folder and run:
3. Use the GUI: add transactions, filter, view summary, export.

## Files
- `expense_tracker.py` — main program (single file).
- `finance.db` — created automatically on first run (SQLite DB).

## Notes
- Works fully offline.
- To uninstall, delete `expense_tracker.py` and `finance.db`.

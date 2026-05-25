# Secure Desktop Voting & Live Analytics System

A professional, multi-window electronic voting and data ledger application built using Python, Tkinter, and an integrated SQLite3 relational database. Engineered with robust front-end validation layers, defensive database logic, and a dynamic mathematical analytics engine.

## 🚀 Key Engineering Solutions Implemented

* **Object-Oriented Design (OOP):** Re-architected from flat procedural scripts into robust Python classes inheriting from `tk.Frame`. This isolates memory leaks and ensures continuous, crash-free performance.
* **Defensive Input Validation:** Built pre-commit validation pipelines that screen string inputs, data types, and numeric ranges *before* initiating SQL operations. Underage voters or unqualified candidates are blocked instantly at the UI level to protect database integrity.
* **Mac AppKit Crash Mitigation:** Discovered and patched a native macOS Monterey Tkinter bug (`NSMenuWindowManager` segmentation faults) by completely removing unsafe wildcard imports (`from tkinter import *`) and migrating to an explicit, grid-weighted button control array.
* **Relational Database Ledger:** Implemented real-time atomic data storage via `sqlite3`. The application uses self-healing schema checks (`CREATE TABLE IF NOT EXISTS`) to deploy and construct its own environment smoothly on any machine.
* **Live Aggregate Math Engine:** Built an audit screen that queries raw ballots using SQLite aggregation (`COUNT`, `GROUP BY`, `ORDER BY DESC`), computes live voter distribution percentages, and renders election results dynamically.

---

## 🛠️ App Architecture & Module Blueprint

The project consists of 7 modular, decoupled Python scripts communicating seamlessly via an underlying local database layer:

1. **`frmLogin.py`** – The secure entry gate. Features administrative credential masking, screen centering logic, and explicit hand-offs to the dashboard layout.
2. **`frmMenu.py`** – The operational brain of the application. Houses an explicit, crash-proof grid button grid canvas that handles macro frame-swapping routines.
3. **`VoterDetails.py`** – Student voter demographic registration engine with integrated age constraint screening ($\ge 18$).
4. **`CandidateDetails.py`** – Complex screening form checking multi-variable criteria (Age $\ge 18$, Academic CGPA $\ge 3.0$, and Student Level $\ge 300$) before granting ballot access.
5. **`castVote.py`** – Secure electronic ballot slip page. Feeds voter selections into an immutable transactional ledger (`VotesTally`) with automatic timestamps.
6. **`ViewVoterDetails.py`** – High-density administrative view utilizing a spreadsheet-style `ttk.Treeview` canvas with alternating row striping and dynamic column resizing.
7. **`frmResults.py`** – Live metrics dashboard. Automatically tallies the database rows, processes candidate percentages, and explicitly renders the winner elect.

---

## 💻 Tech Stack & Environment

* **Language:** Python 3.10+
* **Database Engine:** SQLite3 (Embedded Relational Database)
* **Graphical User Interface:** Tkinter Architecture / TTK Styling Canvas
* **Development Environment:** JetBrains PyCharm

---

## 📥 How to Run and Test Locally

1. Make sure you have Python 3 installed on your machine.
2. Clone this repository or download the source files into a single directory.
3. Open your terminal/command prompt inside that folder and run the initialization script:
   ```bash
   python frmLogin.py
   ```
4. **Admin Credentials:** 
   * **Username:** `Admin`
   * **Password:** `12345`

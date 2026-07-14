# 🤖 AI Text-to-SQL Generator

Convert natural language into executable SQL queries using **Google Gemini AI** and **SQLite**.

This application allows users to ask questions in plain English, automatically generates SQL queries using Generative AI, executes them on a SQLite database, explains the generated SQL, and displays the results in an interactive table.

---

## 🚀 Features

- 🤖 Natural Language → SQL using Gemini AI
- 📝 AI-generated SQL explanations
- 🗄 SQLite database integration
- 📊 Interactive query results
- 📥 Download results as CSV
- 📚 Database schema viewer
- 🎨 Modern Streamlit interface

---

## 🛠 Tech Stack

- Python
- Streamlit
- Google Gemini API
- SQLite
- Pandas
- python-dotenv

---

## 📂 Project Structure

```
AI-Text-to-SQL-Generator/
│
├── app.py
├── ai.py
├── database.py
├── requirements.txt
├── .gitignore
└── README.md
```

---

## ⚙ Installation

Clone the repository

```bash
git clone https://github.com/shrutisingh07/AI-Text-to-SQL-Generator.git
```

Move into the project

```bash
cd AI-Text-to-SQL-Generator
```

Install dependencies

```bash
pip install -r requirements.txt
```

Create a `.env` file

```
GEMINI_API_KEY=YOUR_API_KEY
```

Run the application

```bash
streamlit run app.py
```

---

## 💻 Example Queries

- Show all employees
- Show employees earning more than 50000
- Show IT employees
- Show average salary
- Count total employees

---

## 📸 Screenshots

Add screenshots here after deployment.

Example:

- Home Page
- SQL Generation
- Query Results

---

## 🔮 Future Improvements

- Multiple database support
- PostgreSQL & MySQL integration
- Query history
- Database upload
- AI-powered query optimization
- Charts & visualizations

---

## 👩‍💻 Developer

**Shruti Singh**

GitHub:
https://github.com/shrutisingh07

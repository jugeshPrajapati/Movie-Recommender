
# 🎬 Movie Recommendation System with Chatbot (PyQt5 GUI)

A smart movie recommender desktop application that suggests similar movies based on your input, filters, and a built-in conversational chatbot. Built using **Python**, **PyQt5**, **pandas**, and **scikit-learn**.

---

## 🚀 Features

- 🎯 **Content-Based Movie Recommendation**  
  Suggests top 10 similar movies based on the one you enter.

- 🧠 **Chatbot Assistant**  
  Built-in conversational assistant using NLTK. Ask questions like:
  - "How to use it?"
  - "Which movie is best?"
  - "What is soup?"

- 🔎 **Smart Filters**  
  Filter recommendations by:
  - **Genre** (action, romance, comedy, etc.)
  - **Rating** (High to Low or Low to High)
  - **Year** (Old to New or New to Old)
  - **Soup**: A smart feature that matches based on actor, director, producer, genre, and title.

- 📋 **Interactive Table View**  
  All recommendations are displayed in a scrollable table for quick browsing.

- 🖥️ **Standalone GUI App**  
  No need to use command line — fully interactive PyQt5 desktop interface.

---


## 👨‍💻 Author

**Jugesh**  
Made with ❤️ and Python

---
pyinstaller --onefile --windowed --clean --noconfirm --icon=movie.ico  --add-data "Bestdataset.csv;." app.py

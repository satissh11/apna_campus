# 🏫 Apna Campus

**Apna Campus** is a Flask-based web application that helps students, faculty, and visitors quickly search and explore campus locations. The application uses an SQLite database to provide detailed information about blocks, floors, rooms, roles, categories, and navigation details.

🌐 **Live Demo:** https://apna-campus-34by.vercel.app/

---

## 📖 Overview

Finding a specific room, office, lab, or department on a large campus can be challenging. **Apna Campus** simplifies this process through an intelligent search system and an organized location directory.

---

## ✨ Features

### 🔍 Smart Search
Search locations using:
- Name
- Type
- Block
- Floor
- Room Number
- Role
- Category
- Description

### 🗂️ Category-wise Location Directory
- Browse all campus locations in a structured format.
- Easy navigation through categorized listings.

### 📍 Location & Navigation Support
- Latitude and Longitude coordinates.
- Map labels for better navigation.

### 🖼️ Static Asset Management
- Campus logo support.
- Icons and static resources integration.

---

## 🛠️ Tech Stack

| Component | Technology |
|-----------|------------|
| Backend | Flask (Python) |
| Database | SQLite |
| Frontend | HTML, CSS, Jinja2 Templates |
| Deployment | Vercel |

---

## 📂 Project Structure

apna_campus/
│
├── aap.py                # Main Flask application
├── requirements.txt      # Python dependencies
├── vercel.json           # Vercel deployment configuration
├── campus.db             # SQLite database
│
├── templates/            # HTML templates
│   ├── landing.html
│   ├── index.html
│   └── result.html
│
└── static/               # Static assets
    ├── logo/
    ├── css/
    ├── js/
    └── icons/

---

## ⚙️ Installation & Local Setup

### 1. Clone the Repository

git clone https://github.com/satissh11/apna_campus.git

cd apna_campus

### 2. Create a Virtual Environment (Recommended)

python -m venv venv

Activate the environment:

**Windows**

venv\Scripts\activate

**Linux / macOS**

source venv/bin/activate

### 3. Install Dependencies

pip install -r requirements.txt

### 4. Run the Application

python aap.py

### 5. Open in Browser

http://127.0.0.1:5000

---

## 🌐 Deployment on Vercel

### Step 1
Push the project to GitHub.

### Step 2
Connect the repository to Vercel.

### Step 3
Ensure the following files are present in the root directory:

- requirements.txt
- vercel.json

### Step 4
Deploy the project.

Vercel automatically detects the Flask configuration and deploys the application.

🔗 Live URL:
https://apna-campus-34by.vercel.app/

---

## 📸 Screenshots

### 🏠 Homepage
landing.html

### 🔎 Search Page
index.html

### 📄 Result Page
result.html

Add screenshots inside a `screenshots/` folder and use:

![Homepage](screenshots/homepage.png)

![Search Page](screenshots/search.png)

![Result Page](screenshots/result.png)

---

## 👨‍💻 Author

**Satish Kumar**

📍 Ranchi, Jharkhand, India

### Interests
- IoT Development
- Web Development
- Drone Design
- Embedded Systems

### GitHub
https://github.com/satissh11

---

## 🤝 Contributing

Contributions are welcome!

1. Fork the repository
2. Create a feature branch
3. Commit your changes
4. Push to your branch
5. Open a Pull Request

---

## 📜 License

This project is licensed under the **MIT License**.

Feel free to use, modify, and distribute this project in accordance with the license terms.

---

⭐ If you found this project useful, consider giving it a star on GitHub!

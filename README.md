
````markdown
# 📁 Task Management System

A **simple, lightweight task management application** designed for **college minor project submission**, but **production-ready with Docker, Gunicorn, and Nginx configuration**.

This application lets you:
- Signup and login with email and password
- View **your own tasks**
- **Add**, **edit**, **delete**, **mark done**, and **undo** tasks
- See **created** and **completed** datetime
- Styled with **Bootstrap 5**

---

## 🚀 Features

✅ User Authentication (Signup, Signup, Sessions)  
✅ Personalized Dashboard (each user sees their own tasks)  
✅ CRUD Operations (Create, Update, Delete, Complete, Undo)  
✅ Timestamps for Creation and Completion  
✅ Responsive UI with Bootstrap  
✅ Dockerized for Deployment  
✅ Nginx + Gunicorn Support (Production)  

---

## 🟣 Tech Stack

- **Flask** (Python Web Framework)  
- **Jinja2** Templating  
- **PyMongo** for Database  
- **Bcrypt** for Password Hashing  
- **Docker, Gunicorn, Nginx** for Deployment  
- **Bootstrap 5** for UI Styling  

---

## ⚙ Installation (Development)

1️⃣ **Clone the repository:**

```bash
git clone https://github.com/yourUsername/taskmanagement.git
cd taskmanagement
````

2️⃣ **Create a virtual environment and activate it:**

```bash
python3 -m venv venv
source venv/Scripts/activate  # On Windows
source venv/bin/activate      # On Linux/Mac
```

3️⃣ **Install requirements:**

```bash
pip install -r requirements.txt
```

4️⃣ **Set up environment variables:**

Create a `.env` file in the root directory:

```bash
SECRET_KEY='your_secret_key'
MONGODB_URI='your_mongodb_connection_url'
```

---

## ⚙ Run (Development)

```bash
export FLASK_ENV=development
flask run
```

Open [http://127.0.0.1:5000](http://127.0.0.1:5000) in your browser.

---

## 🐳 Docker (Production)

1️⃣ Build the Docker image:

```bash
docker build -t taskmanagement .
```

2️⃣ Run a container:

```bash
docker run -p 8000:8000 -e SECRET_KEY='your_key' -e MONGODB_URI='your_url' taskmanagement
```

---

## 🌍 Deployment Notes

✅ **Docker Compose:**
See `docker-compose.yaml` for multi-service configuration.

✅ **Nginx:**
For production, put Nginx in **reverse proxy** in front of Gunicorn.

✅ **SSL:**
For HTTPS, use certbot with Nginx.

---

## 📁 Project Structure (Final)

```
.
├── app/
│ ├─ __init__.py
│ ├─ routes/
│ ├─ models/
│ ├─ templates/
│ ├─ static/
├── .venv/
├── .gitignore
├── requirements.txt
├── Dockerfile
├── nginx.conf
├── run.py
├── .env.example
├── README.md
```

---


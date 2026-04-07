# Flask_Form_Handling_POST_Method

# Flask Login System (POST Method)

## 📌 Project Overview

This project demonstrates how to build a simple **login system using Flask** and handle user input securely using the **POST method**.

It is part of my backend development learning journey.

---

## 🚀 Features

* Login form with username and password
* Data sent securely using POST method
* Backend validation of credentials
* Displays success or error message

---

## 🛠️ Technologies Used

* Python
* Flask
* HTML

---

## 📂 Project Structure

```
flask-login-post-method/
│
├── app.py
└── templates/
    └── post.html
```

---

## ⚙️ How It Works

1. User opens the login page.
2. Enters username and password.
3. Form sends data using POST method.
4. Flask receives data using:

   ```
   request.form.get()
   ```
5. Backend checks credentials:

   * If correct → Login Successful
   * If incorrect → Error message displayed

---

## ▶️ How to Run the Project

1. Install Flask:

   ```
   pip install flask
   ```

2. Run the application:

   ```
   python app.py
   ```

3. Open browser and go to:

   ```
   http://127.0.0.1:5000/
   ```

---

## 🧠 Concepts Learned

* Flask routing
* HTML forms
* POST method
* request.form in Flask
* Basic authentication logic

---

## 🔒 Why POST Method?

* Data is not visible in URL
* More secure than GET
* Used in real-world login systems

---

## 🎯 Future Improvements

* Add database (SQLite)
* Password hashing for security
* User registration system
* Better UI with CSS

---

## 👨‍💻 Author

Amrutha D N

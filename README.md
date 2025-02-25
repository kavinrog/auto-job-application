# 💼 Auto Job Application Form Filler  

This project automates job application submissions using **Selenium**. The script reads user details from a JSON file, navigates to a sample job application page, and fills in the required fields automatically.  

## 📌 Features  
✅ Reads user details from `user_data.json`  
✅ Auto-fills form fields (text inputs, radio buttons, dropdowns)  
✅ Detects CAPTCHA and pauses for manual resolution  
✅ Simple setup and easy to customize  

---  

## 🔧 Installation  

1. **Clone the repository**  
   ```bash  
   git clone https://github.com/kavinrog/auto-job-application.git  
   cd auto-job-application  
   ```  

2. **Create and activate a virtual environment**  
   ```bash  
   python -m venv venv  
   source venv/bin/activate  # Windows: venv\Scripts\activate  
   ```  

3. **Install dependencies**  
   ```bash  
   pip install -r requirements.txt  
   ```  

4. **Download & set up ChromeDriver**  
   - [Download ChromeDriver](https://chromedriver.chromium.org/downloads)  
   - Ensure it's added to your system PATH or placed in the project directory  

---  

## 🚀 Usage  

### **Run Two Separate Scripts**
You need **two terminal windows** (or tabs) for running the project properly:

1. **Start the local server (Run this in Terminal 1)**  
   ```bash  
   python -m http.server 8000  
   ```  
   - Ensure `application.html` is in the same directory.  
   - Open `http://localhost:8000/application.html` in your browser to verify.  

2. **Run the automation script (Run this in Terminal 2)**  
   ```bash  
   python main.py  
   ```  
   - The script will launch a browser and fill the form automatically.  

---  

## 🎥 Demo Video  

Watch the demo: [Demo Video on YouTube](https://youtu.be/YourDemoVideoLink)  

---  

## 📁 Project Structure  

```
auto-job-application/
│
├── application.html        # Sample job application form (if used locally)
├── main.py                 # Selenium automation script
├── user_data.json          # Sample user data for form filling
├── requirements.txt        # List of dependencies
└── README.md               # Project documentation
```

---  

## 🛠 Troubleshooting  

- **Connection refused?** Make sure the local server is running.  
- **Form not loading?** Check the URL in `main.py`.  
- **ChromeDriver issues?** Ensure it's installed and matches your Chrome version.  

---


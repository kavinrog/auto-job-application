# 💼 Auto Job Application Form Filler 

Tired of filling out the same job application forms over and over? This script takes care of the busy work for you! Just enter your details once, sit back, and let it do the work.  

With this automation, applying to jobs is faster, easier, and way less annoying. No more typing your name 100 times a day!  

## ✨ What This Script Does
✅ Fills out job applications **automatically**  
✅ Handles different input types (text fields, radio buttons, dropdowns)  
✅ Detects CAPTCHA (because, you know, robots) and waits for you  
✅ Works in **Chrome & Firefox** (or runs invisibly in the background!)  
✅ Keeps logs so you know what’s happening  

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
   - For **Firefox users**, install [geckodriver](https://github.com/mozilla/geckodriver)  

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

## 📁 Example `user_data.json`
To customize the application details, edit `user_data.json`:
```json
{
  "name": "John Doe",
  "email": "john.doe@example.com",
  "experience": "3",
  "position": "Software Engineer",
  "gender": "male",
  "resume_path": "/path/to/resume.pdf"
}
```
- `name` → Your full name  
- `email` → Your email address  
- `experience` → Years of experience (integer)  
- `position` → Must match an option in the dropdown  
- `gender` → Can be `"male"` or `"female"`  

---  

## 🖥 Browser Support  
Currently, the script runs on **Google Chrome** using `ChromeDriver`.  
To use **Firefox**, modify `main.py`:

```python
from selenium.webdriver.firefox.options import Options as FirefoxOptions

options = FirefoxOptions()
driver = webdriver.Firefox(options=options)  # Switch from Chrome to Firefox
```

---  

## 📎 Resume Upload Support (Optional)
To enable resume uploads, modify `main.py`:
```python
driver.find_element(By.ID, "resume").send_keys("/path/to/resume.pdf")
```
Ensure your `application.html` includes a file input:
```html
<input type="file" id="resume" name="resume">
```

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

### ❌ Oh no! ChromeDriver isn’t playing nice?
- If you see **ChromeDriver version error**, update ChromeDriver:
  ```bash
  brew install chromedriver  # macOS
  sudo apt install chromium-chromedriver  # Ubuntu
  ```

### ❌ Form Not Loading?  
- Make sure `application.html` is in the **same directory** as `main.py`.  
- Open `http://localhost:8000/application.html` in your browser manually.  

### ❌ Chrome Not Opening?  
- If it's running **headless**, edit `main.py` and **remove**:
  ```python
  options.add_argument("--headless")
  ```
- Run `python main.py` again.  

### ❌ CAPTCHA Issues?  
- The script **pauses** when it detects CAPTCHA.  
- If you want **automatic CAPTCHA solving**, consider:  
  - **2Captcha API** → `https://2captcha.com/`  
  - **OCR-Based Solutions** → Using `pytesseract`  

---  

## 🔮 Future Enhancements (Optional)  
💡 **Auto-Apply to Multiple Jobs** – Extract job links and apply automatically.  
💡 **AI-Powered Resume Matching** – Analyze job descriptions and adjust applications.  
💡 **Auto-Solve CAPTCHAs** – Use external CAPTCHA solving APIs.  

---  

## 👨‍💻 Author  
🛠 **Kavinder Roghit Kanthen**  

---  

### 📢 **Found an Issue?**  
Feel free to **open an issue** or **contribute** to the project! 

---  

## 🤖 AI Assistance  
This README and code structure were formatted and improved using **GPT/AI tools** to enhance clarity and efficiency. 


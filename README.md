# 🛡️ Security Header Scanner

This is a lightweight Python tool for scanning websites to detect missing or misconfigured HTTP security headers. It provides a quick baseline assessment of web application hardening.

---

## 🔍 What It Does

- Sends an HTTP request to each target URL
- Checks for the presence of key security headers:
  - `Content-Security-Policy`
  - `Strict-Transport-Security`
  - `X-Frame-Options`
  - `X-XSS-Protection`
  - `X-Content-Type-Options`
  - `Referrer-Policy`
  - `Permissions-Policy`
- Outputs results to the terminal and saves them to `report.md`

---

## 📁 File Structure

```
webscanner/
├── scanner.py          # Main script
├── urls.txt            # Input list of URLs
├── report.md           # Markdown report output
├── requirements.txt    # Python dependencies
└── README.md           # This file
```

---

## ⚙️ How to Use

1. Create and activate a virtual environment (optional but recommended):

   ```bash
   python -m venv venv
   source venv/bin/activate   # On Windows: venv\Scripts\activate
   ```

2. Install dependencies:

   ```bash
   pip install -r requirements.txt
   ```

3. Add target URLs to `urls.txt` (one per line), for example:

   ```
   https://example.com
   https://github.com
   ```

4. Run the scanner:

   ```bash
   python scanner.py
   ```

5. View the results in `report.md` or directly in the terminal output.

---

## 📄 Example Output

```text
=== Scanning: https://github.com ===
[✔] Content-Security-Policy
[✔] Strict-Transport-Security
[✘] Permissions-Policy is missing
[=] Total score: 6/7
```

---

## 🧠 Why Use This Tool?

- Perform quick audits of public-facing web applications
- Deliver structured reports to freelance clients
- Expand into full recon or penetration testing pipelines

---

## 📦 Dependencies

- Python 3.7+
- `requests` library

Install with:

```bash
pip install -r requirements.txt
```

---

## 📌 Notes

- This tool performs **passive analysis only** (no active fuzzing or exploitation).
- You can extend it with:
  - HTML vulnerability checks
  - Cookie flag analysis
  - Domain enumeration
  - Export to PDF or HTML

---

Feel free to modify or contribute!

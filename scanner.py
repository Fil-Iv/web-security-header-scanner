import requests

security_headers = [
    "Content-Security-Policy",
    "Strict-Transport-Security",
    "X-Frame-Options",
    "X-XSS-Protection",
    "X-Content-Type-Options",
    "Referrer-Policy",
    "Permissions-Policy"
]


def scan_headers(url, output_lines):
    print(f"\n=== Проверка на: {url} ===")
    output_lines.append(f"## Проверка на: {url}")
    try:
        response = requests.get(url, timeout=10)
        found = 0
        for header in security_headers:
            if header in response.headers:
                print(f"[✔] {header}")
                output_lines.append(f"- ✅ **{header}**")
                found += 1
            else:
                print(f"[✘] {header} липсва")
                output_lines.append(f"- ❌ {header} липсва")
        print(f"[=] Общ резултат: {found}/{len(security_headers)}\n")
        output_lines.append(f"**Общ резултат: {found}/{len(security_headers)}**\n")
    except Exception as e:
        error_msg = f"[!] Грешка при достъп до {url}: {e}"
        print(error_msg)
        output_lines.append(f"- ⚠️ {error_msg}")


if __name__ == "__main__":
    try:
        with open("urls.txt", "r") as f:
            urls = [line.strip() for line in f if line.strip()]

        markdown_output = ["# Web Security Header Report\n"]

        for url in urls:
            if not url.startswith("http"):
                url = "https://" + url
            scan_headers(url, markdown_output)

        with open("report.md", "w", encoding="utf-8") as report_file:
            report_file.write("\n".join(markdown_output))

        print("\n📄 Докладът е записан в: report.md")

    except FileNotFoundError:
        print("❌ Файлът urls.txt не е намерен.")

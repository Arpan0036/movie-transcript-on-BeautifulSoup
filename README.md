# Movie Transcript Scraper (Python)

A simple and efficient Python-based web scraper that automatically extracts movie transcripts from **Subslikescript.com** and saves them as `.txt` files.  
Built using `requests` and `BeautifulSoup`, this tool demonstrates clean web-scraping logic, HTML parsing, and automated file generation.

---

## 🚀 Features
- Scrapes movie titles and transcript links from the homepage  
- Automatically visits each movie page  
- Extracts the full transcript using HTML parsing  
- Saves each transcript as a UTF-8 `.txt` file  
- Uses lightweight libraries (`requests`, `bs4`)  

---

## 🧠 How It Works
1. Fetches the homepage of Subslikescript  
2. Collects all movie URLs from the script list  
3. Visits each movie page one-by-one  
4. Extracts the title and transcript  
5. Creates a text file for each transcript  

---

## 📦 Requirements
Install dependencies before running:

```bash
pip install requests beautifulsoup4 lxml

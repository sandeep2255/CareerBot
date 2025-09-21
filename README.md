# CareerBot

**CareerBot** is an AI-powered job application assistant that automatically scrapes job listings from websites and generates professional email content for applications. Built with Python, Selenium, and LangChain with Ollama, CareerBot streamlines your job search process and helps you apply efficiently.  

---

## Features

- **Job Scraping:** Automatically search and collect job listings based on your query.  
- **Email Generation:** Generate professional, polite, and customized email content for each job.  
- **Agent-based Workflow:** Uses LangChain agents and tools to coordinate scraping and email generation.  
- **AI-powered:** Leverages Ollama models to generate human-like, professional emails.  
- **Configurable:** Limit the number of jobs, set search queries, and choose AI models.  

---

## Tech Stack

- **Python 3.10+**  
- **Selenium** – For automated web scraping.  
- **BeautifulSoup** – Optional, for advanced HTML parsing.  
- **LangChain** – For agent orchestration.  
- **Ollama** – Local AI models to generate email content.  
- **Webdriver Manager** – Simplified ChromeDriver management.  

## Installation

1. Clone the repository:

```bash
git clone https://github.com/yourusername/CareerBot.git
cd CareerBot
````

2. Create a virtual environment:

```bash
python -m venv job_venv
job_venv\Scripts\activate  # Windows
source job_venv/bin/activate  # macOS/Linux
```

3. Install dependencies:

```bash
pip install -r requirements.txt
pip install langchain-ollama
pip install selenium webdriver-manager
```

4. Ensure Ollama is installed and a model is available:

```bash
ollama pull gemma3:1b  # or your preferred model
ollama start           # start the local Ollama server
```

---

## Usage

```python
from job_agent import JobAgent

# Initialize the agent
agent = JobAgent(headless=True, model="gemma3:1b")

# Fetch top 5 Software Developer jobs and generate email content
job_emails = agent.fetch_and_prepare_emails(query="Software Developer", limit=5)

for idx, item in enumerate(job_emails, 1):
    print(f"--- Job {idx} ---")
    print("Job Title:", item['job_data']['title'])
    print("Company:", item['job_data']['company'])
    print("Email Content:\n", item['email_content'])
    print("\n----------------\n")

# Close the agent
agent.close()
```

---

## Folder Structure

```
CareerBot/
│
├─ Scrapping_tool/
│   └─ job_scraper.py       # Selenium scraping logic
│
├─ Job_tools.py             # LangChain tools for scraping and email generation
├─ job_agent.py             # Agent orchestration using LangChain + Ollama
├─ requirements.txt
└─ README.md
```

---

## License

This project is licensed under the **MIT License**. See the `LICENSE` file for details.

```
MIT License

Copyright (c) 2025 Sandeep Pradeep

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES, OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
```

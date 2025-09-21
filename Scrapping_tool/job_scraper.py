from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
import time
import re


class JobScraper:
    def __init__(self, headless=True):
        """
        Initialize the Selenium driver with options.
        """
        options = Options()
        if headless:
            options.add_argument("--headless=new")
        options.add_argument("--disable-gpu")
        options.add_argument("--window-size=1920,1080")
        self.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)

    def search_jobs(self, query="Software Developer", site="https://technopark.in/job-search"):
        """
        Search jobs on the site and return links to job postings.
        """
        self.driver.get(site)
        time.sleep(2)

        search_box = self.driver.find_element(By.CSS_SELECTOR, "input[placeholder='Search By Job Description / Company Name']")
        search_box.send_keys(query)
        search_box.submit()
        time.sleep(5)

        job_divs = self.driver.find_elements(By.CSS_SELECTOR, "div.flex.w-full.flex-col")
        job_links = []

        for div in job_divs:
            a_tags = div.find_elements(By.TAG_NAME, "a")
            if a_tags:
                href = a_tags[0].get_attribute("href")
                job_links.append(href)

        return job_links

    def scrape_job_details(self, link):
        """
        Scrape details of a single job posting.
        """
        self.driver.get(link)
        time.sleep(1)

        job_data = {}

        try:
            title_elem = self.driver.find_element(By.TAG_NAME, "h1")
            job_data['title'] = title_elem.text.strip()
        except:
            job_data['title'] = None

        try:
            div_elem = self.driver.find_element(By.CSS_SELECTOR, "div.flex.items-center.justify-between.pt-2")
            company_elem = div_elem.find_element(By.TAG_NAME, "a")
            job_data['company'] = company_elem.text.strip()
        except:
            job_data['company'] = None

        try:
            brief_div = self.driver.find_element(By.XPATH, "//h3[text()='Brief Description']/following-sibling::div")
            job_data['description'] = brief_div.get_attribute("innerHTML")
        except:
            p_tags = self.driver.find_elements(By.TAG_NAME, "p")
            job_data['description'] = "\n".join([p.text for p in p_tags])

        emails = re.findall(r"[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}", self.driver.page_source)
        job_data['email'] = emails[0] if emails else None

        return job_data

    def scrape_all_jobs(self, query="Software Developer", site="https://technopark.in/job-search", limit=None):
        """
        Search jobs and scrape details of all jobs or a limited number.
        """
        job_links = self.search_jobs(query, site)
        if limit:
            job_links = job_links[:limit]

        all_jobs = []
        for link in job_links:
            job_data = self.scrape_job_details(link)
            all_jobs.append(job_data)

        return all_jobs

    def close(self):
        self.driver.quit()

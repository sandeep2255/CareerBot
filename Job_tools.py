from Scrapping_tool.job_scraper import JobScraper
from langchain_community.chat_models import ChatOllama
from langchain.prompts import ChatPromptTemplate, HumanMessagePromptTemplate
from langchain.tools import Tool

scraper= JobScraper(headless=True)
model = ChatOllama(model="gemma3:1b") 

def scrape_job_tool(query, limit=1):
    jobs = scraper.scrape_all_jobs(query=query, limit=limit)
    return jobs

def generate_email_tool(job_data):
    template = """You are a professional job seeker assistant. 
    Write a polite, concise, and professional email to apply for this job.

    Job Title: {title}
    Company: {company}
    Job Description: {description}
    Contact Email: {email if email else 'Not provided'}

    Write the email content only, do not add extra explanations.
    """

    humanMessage = HumanMessagePromptTemplate.from_template(template)
    chatPrompt = ChatPromptTemplate.from_messages([humanMessage])
    prompt = chatPrompt.format_prompt(
        title=job_data.get('title', 'N/A'),
        company=job_data.get('company', 'N/A'),
        description=job_data.get('description', 'N/A'),
        email=job_data.get('email', None)
    ).to_messages()


job_scrapper_tool = Tool(
    name="Job Scraper",
    func=scrape_job_tool,
    description="Use this tool to scrape job postings based on a query. Input should be a job title or keywords, and an optional limit for number of jobs to return.",
)

emeail_generator_tool = Tool(
    name="Email Generator",
    func=generate_email_tool,
    description="Use this tool to generate a professional job application email based on the provided job details. Input should be a job data dictionary.",
)
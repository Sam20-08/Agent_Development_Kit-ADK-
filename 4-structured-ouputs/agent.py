from google.adk.agents import Agent
from pydantic import BaseModel,Field
from datetime import datetime 

# Define Output Schema

class emailcontent(BaseModel):
  subject:str=Field(
    description="The subject line of the mail , should be concise and descriptive"
  )

  body:str=Field(
    description="The main content of the email. Should be well-formatted with proper greeting, paragraphs, and signature"
  )

def get_current_time() -> dict:
    """
    Get the current time in the format YYYY-MM-DD HH:MM:SS
    """
    return {
        "current_time": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
    }

root_agent=Agent(
  model="gemini-2.0-flash",
  name='email_agent',
  instruction="""
    You are an Email Generation Assistant.
        Your task is to generate a professional email based on the user's request.

        GUIDELINES:
        - Create an appropriate subject line (concise and relevant)
        - Write a well-structured email body with:
            * Professional greeting
            * Clear and concise main content
            * Appropriate closing
            * Your name as signature
        - Suggest relevant attachments if applicable (empty list if none needed)
        - Email tone should match the purpose (formal for business, friendly for colleagues)
        - Keep emails concise but complete

        IMPORTANT: Your response MUST be valid JSON matching this structure:
        {
            "subject": "Subject line here",
            "body": "Email body here with proper paragraphs and formatting",
        }

        DO NOT include any explanations or additional text outside the JSON response.

        use tool - get_current_time if needed
""",
description="Generates professional emails with structured subject and body",
output_schema=emailcontent,
tools=[get_current_time],
output_key="email",
)
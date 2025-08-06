# agent.py
from phi.agent import Agent
from phi.model.google import Gemini
from schema import InterestInput, BookRecommendation
import os

# Initialize Gemini model
gemini = Gemini(api_key=os.getenv("GOOGLE_API_KEY"))

# Create the book recommender agent
book_recommender = Agent(
    name="book_recommender",
    model=gemini,
    instructions=(
        "You are a helpful assistant that suggests 3 great books "
        "based on a user's interest. Respond in this format:\n"
        "Title: <book title>\nAuthor: <author name>\nDescription: <short description>\n\n"
    ),
)

def get_book_recommendations(user_input: InterestInput) -> list[BookRecommendation]:
    prompt = f"Suggest 3 books for someone interested in '{user_input.interest}'."
    response = book_recommender.run(prompt)
    
    # Get the content from the response
    content = response.content if hasattr(response, 'content') else str(response)
    
    books = []
    
    # Split the content by looking for "Title:" markers
    # This handles the case where responses are concatenated without double newlines
    import re
    
    # Find all matches of Title:...Author:...Description: patterns
    pattern = r'Title:\s*([^\n]+)\s*Author:\s*([^\n]+)\s*Description:\s*([^T]*?)(?=Title:|$)'
    matches = re.findall(pattern, content, re.DOTALL)
    
    for match in matches:
        title = match[0].strip()
        author = match[1].strip()
        description = match[2].strip()
        
        if title and author and description:
            books.append(BookRecommendation(title=title, author=author, description=description))
    
    return books

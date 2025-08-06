from phi.agent import Agent
from phi.model.google import Gemini
from schema import UseCaseInput, LLMRecommendation
import os

# Gemini LLM agent setup
llm_agent = Agent(
    name="llm-recommender-agent",
    model=Gemini(id="gemini-1.5-flash", api_key=os.getenv("GOOGLE_API_KEY"))
)

def get_llm_recommendation(use_case: str) -> list[LLMRecommendation]:
    prompt = f"""
    Based on the use case: "{use_case}", suggest the top 3 most suitable LLM models.
    For each model, provide EXACTLY in this format:
    
    Model: [Model Name]
    Provider: [Provider Name]
    Description: [Brief description of why it's suitable]
    
    Please keep each response concise and well-structured.
    """
    
    response = llm_agent.run(message=prompt)
    response_text = response.get_content_as_string()

    # Parse the response to extract model recommendations
    models = []
    lines = response_text.split('\n')
    current_model = {}
    
    for line in lines:
        line = line.strip()
        if line.startswith('Model:'):
            if current_model:  # Save previous model if exists
                if all(key in current_model for key in ['model_name', 'provider', 'description']):
                    models.append(LLMRecommendation(**current_model))
            current_model = {'model_name': line.replace('Model:', '').strip()}
        elif line.startswith('Provider:'):
            current_model['provider'] = line.replace('Provider:', '').strip()
        elif line.startswith('Description:'):
            current_model['description'] = line.replace('Description:', '').strip()
    
    # Don't forget the last model
    if current_model and all(key in current_model for key in ['model_name', 'provider', 'description']):
        models.append(LLMRecommendation(**current_model))
    
    # If parsing failed, provide fallback recommendations
    if not models:
        models = [
            LLMRecommendation(
                model_name="GPT-4",
                provider="OpenAI", 
                description=f"Excellent for {use_case} with strong reasoning and language capabilities"
            ),
            LLMRecommendation(
                model_name="Claude 3",
                provider="Anthropic",
                description=f"Great for {use_case} with focus on helpful, harmless, and honest responses"
            ),
            LLMRecommendation(
                model_name="Gemini 1.5",
                provider="Google",
                description=f"Good for {use_case} with multimodal capabilities and fast response times"
            )
        ]
    
    return models[:3]  # Return top 3

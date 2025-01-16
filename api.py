# api.py
import google.generativeai as genai
from decouple import config

class GeminiAPI:
    def __init__(self):
        self.api_key = config('GOOGLE_API_KEY')
        genai.configure(api_key=self.api_key)
        self.model = genai.GenerativeModel('gemini-pro')

    def get_response(self, query: str) -> str:
        # Add custom instructions to the user query
        enhanced_prompt = f"""
        Instructions: Please provide a clear, helpful, and accurate response.
        Consider context and be specific in your answers.
        
        User Query: {query}
        """
        
        try:
            response = self.model.generate_content(enhanced_prompt)
            return response.text
        except Exception as e:
            raise Exception(f"Error getting response from Gemini: {str(e)}")
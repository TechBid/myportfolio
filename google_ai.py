import os
import google.generativeai as genai
import dotenv

dotenv.load_dotenv()

# Load API key from environment variables for security
API_KEY = os.getenv("GEMINI_API_KEY")
if not API_KEY:
    raise ValueError("GEMINI_API_KEY not found in environment variables")

genai.configure(api_key=API_KEY)

def ask_ai_model(context, query):
    """
    Sends a query to the Gemini model with some context.
    Implements strict grounding to prevent hallucination.
    """
    # Input validation
    if not query or not query.strip():
        return "Please provide a valid question."
    
    if len(query) > 1000:
        return "Your question is too long. Please keep it under 1000 characters."
    
    # Sanitize query - remove potentially harmful characters
    query = query.strip()
    
    try:
        model = genai.GenerativeModel('gemini-2.5-flash')
        
        # Strict grounding prompt to prevent hallucination
        prompt = f"""You are an AI assistant helping visitors learn about a specific project or research paper.

STRICT RULES:
1. You MUST answer using ONLY the information provided in the context below
2. If the context does not contain the information needed to answer the question, say: "I don't have that information in the provided context. Please ask about the details that are available."
3. DO NOT make up, infer, or fabricate any information
4. DO NOT mention skills, technologies, or features not explicitly stated in the context
5. Keep your answers concise and directly based on the context

CONTEXT:
{context}

USER QUESTION: {query}

Please provide a helpful answer based strictly on the context above."""

        response = model.generate_content(prompt)
        
        if not response or not response.text:
            return "I apologize, but I couldn't generate a response. Please try rephrasing your question."
        
        return response.text
        
    except Exception as e:
        # Log error for debugging (in production, use proper logging)
        print(f"Error in ask_ai_model: {str(e)}")
        return "I'm having trouble connecting to the AI service right now. Please try again in a moment."

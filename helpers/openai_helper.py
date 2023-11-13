import openai

class OpenAIHelper:
    def __init__(self, api_key):
        openai.api_key = api_key

    def generate_response(self, ingredients, method, diet):
        # Form a structured prompt
        query = f"""
        Create a recipe using the following ingredients: {ingredients} 
        The method of cooking should be: {method} 
        The dietary requirement is: {diet}

        The recipe should be structured in the following format:

        INGREDIENT - UNIT - QTY - COST - TOTAL COST
        PREP TIME
        COOK TIME
        TOTAL TIME REQUIRED
        METHOD
        """

        # Query the OpenAI API
        response = openai.Completion.create(engine="text-davinci-003", prompt=query, max_tokens=400)

        # Extract the 'choices' list from the response
        choices = response['choices']

        # If the 'choices' list is not empty, return the 'text' field of the first choice
        if choices:
            text = choices[0]['text']
            try:
                html_table = self.text_to_html_table(text)  # Convert text to HTML table
                return html_table
            except Exception as e:
                return f"An error occurred while generating the recipe: {str(e)}"

        return 'Sorry, I was not able to generate a recipe based on your inputs.'

    def text_to_html_table(self, text):
        rows = text.split('\n')
        html_rows = ["<tr><td>" + "</td><td>".join(row.split('-')) + "</td></tr>" for row in rows]
        return "<table>" + "\n".join(html_rows) + "</table>"

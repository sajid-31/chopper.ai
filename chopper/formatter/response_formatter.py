class ResponseFormatter:
    def format(self, llm_response):
        # Simple formatting, can be enhanced
        return llm_response['choices'][0]['message']['content'].strip()

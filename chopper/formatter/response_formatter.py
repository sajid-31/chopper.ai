import json

class ResponseFormatter:
    def format(self, llm_response):
        # Simple formatting, can be enhanced
        response = llm_response['choices'][0]['message']['content'].strip()
        # print(response)
        response = json.loads(response)
        if response['TYPE']=='AMBIGUOUS':
            return 'Your question does not align with my area of expertise'
        elif response['TYPE']=='CODE':
            result = ""
            for command_dict in response['CODE']:
                for desc,command in command_dict.items():
                    result = result +'➡️  ' + desc + '\n' + '\033[92m'+command + '\033[0m' + '\n'
            return result
        
        elif response['TYPE']=='CONCEPT':
            return response['INFO']
           
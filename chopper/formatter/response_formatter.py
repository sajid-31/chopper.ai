import json

class ResponseFormatter:
    def __init__(self):
        self.command_list = []

    def format(self, llm_response):
        self.command_list = []
        response = llm_response['choices'][0]['message']['content'].strip()
        # print(response)
        response = json.loads(response)
        if response['TYPE']=='AMBIGUOUS':
            return 'Your question does not align with my area of expertise'
        elif response['TYPE']=='CODE':
            result = ""
            iteration=1
            for command_dict in response['CODE']:
                for desc,command in command_dict.items():
                    result = result+ str(iteration) +' ➡️  ' + desc + '\n' + '\033[92m'+command + '\033[0m' + '\n'
                    iteration+=1
                    self.command_list.append(command)
            return result
        
        elif response['TYPE']=='CONCEPT':
            return response['INFO']
    
    # used in main.py to get all the commands in a list
    def get_commands(self):
        return self.command_list
           
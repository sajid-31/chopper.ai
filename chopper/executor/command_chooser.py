class CommandChooser:
    @staticmethod
    def choose_command(commands):
        no_of_commands = len(commands)
        command_number_input = input(f"\n🤔✨ \033[96m Which command do you want me to execute? \nEnter 'all' to execute all commands \ntype command number to execute a specific command \npress enter to skip \033[0m \n")
        if command_number_input=="all"or command_number_input=="ALL":
            return no_of_commands+1
        if command_number_input.isdigit()==False:
            return -1
        if int(command_number_input) <= 0 or int(command_number_input) > no_of_commands + 1:
            return -1
        else:
            return int(command_number_input)

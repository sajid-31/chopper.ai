class CommandChooser:
    @staticmethod
    def choose_command(formatted_response):
        print("\n⚙️  Possible Commands Detected:")
        # Dummy commands for now
        commands = ["ls", "pwd", "date"]
        for idx, cmd in enumerate(commands):
            print(f"{idx + 1}. {cmd}")
        choice = input("Choose command number to execute (or press Enter to skip): ")
        return commands[int(choice) - 1] if choice.isdigit() else None

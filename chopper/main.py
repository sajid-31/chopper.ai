from .ui.terminal_ui import TerminalUI
from .llm_connector.llm_client import LLMClient
from .formatter.response_formatter import ResponseFormatter
from .executor.command_chooser import CommandChooser
from .executor.command_executor import CommandExecutor
from .system_info.system_info_fetcher import fetch_system_info
from pathlib import Path
from importlib.resources import files
from .animations.spinner import Spinner
import sys

def main():
    print("🔧 CHOPPER.AI Terminal Started!")

    ui = TerminalUI()
    llm = LLMClient()
    formatter = ResponseFormatter()
    command = CommandChooser()
    executor = CommandExecutor()

    try:
        while True:
            user_input = ui.get_user_input()

            if user_input.strip().lower() in ['exit','quit']:
                print("👋 Exiting Chopper AI. Goodbye!")
                sys.exit(0)

            file_path = files('chopper.prompts').joinpath('chopper_help.txt')
            with file_path.open('r') as file:
                prompt = file.read()
            user_input = prompt + user_input

            spinner = Spinner("💡 Thinking...")
            spinner.start()

            llm_response = llm.query(user_input)

            spinner.stop()

            formatted_response = formatter.format(llm_response)
            commands_to_execute = formatter.get_commands()
            ui.display_output(formatted_response)
            if len(commands_to_execute)==0:
                continue
            while True:
                choice = command.choose_command(commands_to_execute)
                if choice == -1:
                    break
                else:
                    executor.execute(choice,commands_to_execute)
    except KeyboardInterrupt:
        print("\n🛑 Interrupted. Exiting Chopper AI. Goodbye!")
        sys.exit(0)



if __name__ == "__main__":
    main()


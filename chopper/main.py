from ui.terminal_ui import TerminalUI
from llm_connector.llm_client import LLMClient
from formatter.response_formatter import ResponseFormatter
from executor.command_chooser import CommandChooser
from executor.command_executor import CommandExecutor
from system_info.system_info_fetcher import fetch_system_info
def main():
    print("🔧 CHOPPER.AI Terminal Started!")

    ui = TerminalUI()
    llm = LLMClient()
    formatter = ResponseFormatter()

    while True:
        user_input = ui.get_user_input()
        llm_response = llm.query(user_input)
        formatted_response = formatter.format(llm_response)
        ui.display_output(formatted_response)

        command = CommandChooser.choose_command(formatted_response)
        if command:
            CommandExecutor.execute(command)


if __name__ == "__main__":
    main()


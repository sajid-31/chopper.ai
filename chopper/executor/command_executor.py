import subprocess
import shlex

class CommandExecutor:
    @staticmethod
    def execute(choice, commands):
        def run_command(command):
            print(f"🚀 Executing command: \033[96m{command}\033[0m")
            cmd = shlex.split(command)
            try:
                result = subprocess.run(
                    cmd,
                    capture_output=True,
                    text=True,
                    check=True
                )
                print("\033[92m✅ OUTPUT:\n" + result.stdout + "\033[0m") 
            except subprocess.CalledProcessError as e:
                print("\033[91m❌ Command failed with return code:", e.returncode)
                print("🔻 ERROR OUTPUT:\n" + e.stderr + "\033[0m")
            except FileNotFoundError:
                print("\033[91m❗ Command not found! Check if it's installed.\033[0m")
            except Exception as e:
                print(f"\033[91m⚠️ Unexpected error: {str(e)}\033[0m")


        if choice == len(commands) + 1:
            for command in commands:
                run_command(command)
        else:
            command = commands[choice - 1]
            run_command(command)

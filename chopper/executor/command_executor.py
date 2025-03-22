import os

class CommandExecutor:
    @staticmethod
    def execute(command):
        print(f"\n🚀 Executing: {command}\n")
        os.system(command)

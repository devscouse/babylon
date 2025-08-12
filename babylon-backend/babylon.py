
from src.agent import BabylonAgent
from colorama import Fore, just_fix_windows_console

just_fix_windows_console()


def main():
    agent = BabylonAgent()
    response = agent.chat("I would like to begin my session") 
    print(Fore.GREEN + response.content.__str__() + Fore.RESET)
     
    while user_msg := input("Enter your response: "):
        response = agent.chat(user_msg) 
        print(Fore.GREEN + response.content.__str__() + Fore.RESET)




if __name__ == "__main__":
    main()

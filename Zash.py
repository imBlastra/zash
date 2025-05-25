import os

print("Ros: Onyx")
def mode(cmd: str):
    if cmd == "onyx":
        print("you are using onyx ros")
    elif cmd == "help":
        print("help: show this help")
        print("onyx: show the current mode")
        print("exit: exit the cli")
        print("entr: newline")
        print("env: show the current environment")
        print("user: show the current user")
        print("home: show the current home")
        print("path: show the current path")
        print("mkdir: create a new directory")
        print("ls: list the files in the current directory")
        print("echo: print a string")
        print("mem: show the memory usage")

    elif cmd == "":
        #newline
        pass
    elif cmd == "env":
        print("PATH: " + os.environ["PATH"])
        print("HOME: " + os.environ["HOME"])
        print("USER: " + os.environ["USER"])
    elif cmd == "user":
        print("user: " + os.environ["USER"])
    elif cmd == "home":
        print("home: " + os.environ["HOME"])
    elif cmd == "path":
        print("path: " + os.environ["PATH"])
    elif cmd == "mkdir":
        print("mkdir: create a new directory")
        dir_name = input("Enter the name of the directory: ")
        os.makedirs(dir_name, exist_ok=True)
        print(f"Directory '{dir_name}' created.")
    elif cmd == "ls":
       files = os.listdir(".")
       print(files)
    elif cmd == "echo":
        string = input("echo: ")
        print(string)
    elif cmd == "mem":
        mem = psutil.virtual_memory()
        print(f"Total: {mem.total / (1024 ** 3):.2f} GB")
        print(f"Available: {mem.available / (1024 ** 3):.2f} GB")
        print(f"Used: {mem.used / (1024 ** 3):.2f} GB")
    else:
        print("invalid cmd(use help to see the list of commands)")

while True:
    user_input = input("onyx@ros:~$  ")
    if user_input.lower() == "exit":
        print("Exiting ROS CLI.")
        break
    mode(user_input)

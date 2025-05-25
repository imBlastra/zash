import os
import sys
import subprocess

user = input("Username:")

def main():
 while True:
  try:
     #prompt
     inp = input(f'{user}@zash$')
     if inp.strip() == 'exit':
      break
     #parse
     args = inp.split()
     if not args:
         continue
     #built-in: cd
     if args[0] == 'cd':
         if len(args) > 1:
          os.chdir(args[1])
         else:
          os.chdir(os.path.expanduser('~'))
         try:
            os.chdir(dest)
         except Exception as e:
             print(f"cd: {e}")   
         continue
        #Built-in: echo
     if args[0] == 'echo':
       print(' '. join(args[1:]))
       continue

if __name__ == "__main__":
   main() 

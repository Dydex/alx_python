import sys

def main():
    argv = sys.argv[1:]  # Exclude the script name itself from the arguments
    num_args = len(argv)
    
    if num_args == 0:
        print("0 arguments.")
    elif num_args == 1:
        print("1 argument:")
        
        for i, arg in enumerate(argv, start=1):
                print(f"{i}: {arg}")
                
    else:
        print(f"{num_args} arguments:")

        for i, arg in enumerate(argv, start=1):
                print(f"{i}: {arg}")

if __name__ == "__main__":
    main()

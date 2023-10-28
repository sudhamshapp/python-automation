import os
def main():
    req_path = input("enter the path to naviagte: ")
    print(os.getcwd())
    try:
        os.chdir(req_path)
        print(os.getcwd())
    except FileNotFoundError:
        print("file not found")
    except PermissionError:
        print("permission denied")
    except NotADirectoryError:
        print("not a directory")    
    except Exception as e:
        print(e)
    return None    
if __name__ == "__main__":
    main()                    
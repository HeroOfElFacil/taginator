import os

text=[]

def import_txt():
    print("Importing files...")
    filelist = os.listdir(os.getcwd())
    for file in filelist:
        if file.endswith(".txt"):
            print(file) #filename
            try:
                with open(file, 'r', encoding = "utf-8") as f:
                    contents = f.read()
                    text.append(contents)
            except:
                pass
    print("Done!")

def main():
    print("Hello")
    import_txt()

if __name__ == '__main__':
    main()

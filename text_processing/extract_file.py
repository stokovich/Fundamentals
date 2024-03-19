def extract_file():
    path = input()

    index = path.rfind("\\")
    substring = path[index + 1:]
    substring_list = substring.split('.')

    print(f'File name: {substring_list[0]}')
    print(f'File extension: {substring_list[1]}')


extract_file()

def extract_file_info(file_path):
    file_name_with_extension = file_path.split("\\")[-1]
    file_name, file_extension = file_name_with_extension.rsplit('.', 1)

    print(f"File name: {file_name}")
    print(f"File extension: {file_extension}")

file_path = input()
extract_file_info(file_path)

# import re
#
# pattern = r'\\([A-Za-z\-]+)\.([a-z]+)'  # we have two groups inside our regex -> 1st with the file name, 2nd with its ext
# text = input()
# # this match will give us a list with a nested tuple inside it, so we have to unpack it
# match = re.findall(pattern, text)  # match [0][0] --> file name, match [0][1] --> file ext
# print(f'File name: {match[0][0]}\n'
#       f'File extension: {match[0][1]}')

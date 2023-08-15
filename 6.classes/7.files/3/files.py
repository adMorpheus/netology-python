FILES_PATHS = ['files/1.txt','files/2.txt','files/3.txt']


def sort_files():
    result = []
    for src_file in FILES_PATHS:
        with open(src_file, 'rt', encoding='utf8') as file:
            content = file.read()
            file.seek(0)
            result.append({'name': src_file.split("/")[1], 'count_lines': len(file.readlines()), 'text': content})

    sorted_files = sorted(result, key=lambda f: f['count_lines'])
    with open('result.txt', 'w', encoding='utf8') as file:
        for src_file in sorted_files:
            file.write(src_file['name'] + '\n')
            file.write(str(src_file['count_lines']) + '\n')
            file.write(src_file['text'] + '\n')


sort_files()

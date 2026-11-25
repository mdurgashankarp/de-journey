
file_name = input("File Name: ").strip().lower()

if '.' in file_name:
    extension = file_name.rsplit('.', 1)[1]

    match extension:
        case 'jpg' | 'jpeg':
            print('image/jpeg')
        case 'png':
            print('image/png')
        case 'gif':
            print('image/gif')
        case 'pdf':
            print('application/pdf')
        case 'zip':
            print('application/zip')
        case 'txt':
            print('text/plain')
        case _:
            print('application/octet-stream')
else:
    print('application/octet-stream')

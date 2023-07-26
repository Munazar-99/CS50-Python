file_name = input('Name of the File: ').split('.')

match file_name[len(file_name)-1]:
    case 'jpeg' | 'jpg' | 'gif' | 'png':
        print('image file')
    case 'pdf':
        print('application/pdf')
    case 'txt':
        print('application/txt')
    case  'zip':
        print('application/zip')
    case _:
        print('application/octet-stream')
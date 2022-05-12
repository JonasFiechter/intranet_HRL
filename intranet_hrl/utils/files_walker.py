import os

def files_walker(root_dir, last_dir, next_dir, dirs=[], files=[], history=''):
    print(f'\ntop of function - {root_dir} {last_dir} {next_dir}\n')
    on_root = False
    path = root_dir

    if next_dir != 'root':
        path = last_dir.replace(':', '/') + '/' + next_dir
    else:
        last_dir = path.replace('./', '')

    if last_dir != 'blank' and next_dir != 'root':
        last_dir += ':' + next_dir
    
    dirs = [d for d in last_dir.split(':')]
    history = dirs.pop()
    print(f'history {history} | dirs {dirs}')
    
    print(f'path before walk - {path}\n')
    for root, _dirs, files in os.walk(path):
        dirs = [d for d in _dirs]
        files = [{'path': str(root[1:] + '/' + f), 'file': f} for f in files]
        # print(f'files > {files} dirs > {dirs} root > {root}')
        break

    print(f'end of function - {root_dir}, {last_dir}, {next_dir}\n')
    return  dirs, files, last_dir, history
import os


def files_walker(root_dir, last_dir, next_dir, dirs=[], files=[], history={}):
    on_root = False
    path = root_dir

    if ':' not in last_dir:
        history = {'last_dir': 'blank', 'next_dir': 'root'}
    else:
        dirs = [d for d in last_dir.split(':')]
        next_dir_for_history = dirs.pop()
        last_dir_for_history = ':'.join(dirs)
        history = {'last_dir': last_dir_for_history, 'next_dir': next_dir_for_history}

    if next_dir != 'root':
        path = last_dir.replace(':', '/') + '/' + next_dir
    else:
        last_dir = path.replace('./', '')

    if last_dir != 'blank' and next_dir != 'root':
        last_dir += ':' + next_dir

    dirs = [d for d in last_dir.split(':')]
    
    for root, _dirs, files in os.walk(path):
        dirs = [d for d in _dirs]
        files = [{'path': str(root + '/' + f), 'file': f} for f in files]
        # print(f'files > {files} dirs > {dirs} root > {root}')
        break

    # print(f'end of function - {root_dir}, {last_dir}, {next_dir}\n')
    return  dirs, files, last_dir, history


def files_walker_2(root_dir, path, last_dir):

    dirs = []
    files = []
    if path:
        last_dir = path.split(':')[0]
        path = path.split(':')[1]
    print(f'last_dir: {last_dir} | path: {path}')

    print(f'path before walk > {root_dir} + {path}')

    try:
        for root, dirs, files in os.walk(root_dir + '/' + path):
            dirs = [d for d in dirs]
            files = [{'path': str(root + '/' + f), 'file': f} for f in files]
            break
    except:
        print('error ocurred!')

    print(f'files: {files} | dirs: {dirs}')

    last_dir = path
    history = ''
    return dirs, files, last_dir, history
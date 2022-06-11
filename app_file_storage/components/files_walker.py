import os


def files_walker(root_dir, path, dirs=[], files=[]):

    # The way that this method works can be a little tricky but is much smaller than the older one
    # The first check is determine if the history string will be populated based on the position of
    # the path, because if path is one of the child of the root folder it will return to the root
    # folder, and if it is empty (because is the root folder itself) it just goes empty

    history = '/'.join(path.split('/')[:-1])
    
    # path_list = path.split('/')
    # The content of the path splited items can be usefull to solve the problem with the children 
    # of the root folder that was only True when inside the second level below the root, so this 
    # 'if' can solve this little issue  
    try:
        if not path.split('/')[0] and path.split('/')[1]:
            history = '/'
    except:
        pass

    # print(f'history => {history} path_list => {path_list}')

    # This loop breaks on the first walk inside the path given. And returns to lists with dicts
    # one for every directory and other for each file inside the path.

    for root, dirs, files in os.walk(root_dir + '/' + path):
        dirs = [{'name': d, 'path': path + '/' + d} for d in dirs]
        files = [{ 'file': f, 'path': str(root + '/' + f)} for f in files]
        break

    return dirs, files, history


def files_walker_old(root_dir, last_dir, next_dir, dirs=[], files=[], history={}):
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



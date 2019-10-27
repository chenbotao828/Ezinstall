from dulwich import porcelain
import sys
import os
import shutil

"""
ez.exe
    install <author>/<repo>
    uninstall <package>
"""

def main(args):
    args = args[1:]
    head = args[0]

    if head == "install":
        repo = args[1]
        url = "https://github.com/" + repo + ".git"
        module = repo.split('/')[1]
        path = os.path.abspath('./packages/' + module)
        os.makedirs(path)
        try:
            porcelain.clone(url,path)
        except:
            shutil.rmtree(path)
    elif head == "uninstall":
        module = args[1]
        path = os.path.abspath('./packages/' + module)
        shutil.rmtree(path)

if __name__ == '__main__':
    main(sys.argv)

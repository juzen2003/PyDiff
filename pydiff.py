import sys
import filecmp
import os.path

def py_diff(dir_cmp, title=True, sub_title=True):
    if(title):
        print "============================="
        print "Check main directory"
        print "============================="
        title = False

    # checking different file/dir names
    for name in dir_cmp.right_only:
        print "File/dir ONLY found in %s: %s" % (dir_cmp.right,name)
    for name in dir_cmp.left_only:
        print "File/dir ONLY found in %s: %s" % (dir_cmp.left,name)

    # checking files content if names are the same in both dirs
    for name in dir_cmp.diff_files:
        print "Same file name with DIFFERENT contents found in both directories:"
        print "%s" % (dir_cmp.right)
        print "%s" % (dir_cmp.left)
        print "File: %s" % (name)

    if(sub_title):
        print "============================="
        print "Check same sub directory"
        print "============================="
        sub_title = False

    # recursively check the same sub dirs if existed
    for sub in dir_cmp.subdirs.values():
        py_diff(sub, False, False)

# main function
if __name__ == '__main__':
    if(len(sys.argv) != 3):
        print "Please input only 2 path of directories like: python py_diff.py dir1 dir2"
        exit()

    dir1 = sys.argv[1]
    dir2 = sys.argv[2]
    dir_cmp = filecmp.dircmp(dir1, dir2)
    py_diff(dir_cmp)

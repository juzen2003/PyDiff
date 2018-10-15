import sys
import filecmp
import os.path

# # print(sys.argv)
# # print(os.path.dirname("/Users/yjchang/Desktop/App Academy/project/pythonDiff/dir2"))
# dir1 = "/Users/yjchang/Desktop/App Academy/project/pythonDiff/dir1"
# dir2 = "/Users/yjchang/Desktop/App Academy/project/pythonDiff/dir2"
# dir3 = "/Users/yjchang/Desktop/App Academy/project/pythonDiff/dir3"
#
# # print filecmp.dircmp(dir1, dir2).report()
# dir_cmp = filecmp.dircmp(dir1, dir3)
# # checking different file/dir names
# for name in dir_cmp.right_only:
#     print "File/dir only found in %s: %s" % (dir_cmp.right,name)
# for name in dir_cmp.left_only:
#     print "File/dir only found in %s: %s" % (dir_cmp.left,name)
#
# # checking files content if names are the same in both dirs
# for name in dir_cmp.diff_files:
#     print "diff file %s found in %s" % (name, dir_cmp.right)
#     print "diff file %s found in %s" % (name, dir_cmp.left)
#
# for sub in dir_cmp.subdirs.values():
#     print sub


def py_diff(dir_cmp):
    # checking different file/dir names
    for name in dir_cmp.right_only:
        print "File/dir ONLY found in %s: %s" % (dir_cmp.right,name)
    for name in dir_cmp.left_only:
        print "File/dir ONLY found in %s: %s" % (dir_cmp.left,name)

    # checking files content if names are the same in both dirs
    for name in dir_cmp.diff_files:
        print "File found in both dir but has different contents: %s" % (name)

    # recursive searching all sub
    for sub in dir_cmp.subdirs.values():
        py_diff(sub)

# main function
if __name__ == '__main__':
    dir1 = "/Users/yjchang/Desktop/App Academy/project/pythonDiff/dir1"
    dir2 = "/Users/yjchang/Desktop/App Academy/project/pythonDiff/dir2"
    dir3 = "/Users/yjchang/Desktop/App Academy/project/pythonDiff/dir3"

    dir_cmp = filecmp.dircmp(dir1, dir3)
    py_diff(dir_cmp)

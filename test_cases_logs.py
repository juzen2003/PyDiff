# Here are test cases and logs for pydiff.py
"""
testing hierarchy:

pythonDiff/
    - pydiff.py
    - dir1/
        - test_dir.py
        - sub1/
            - test_sub1.py
    - dir1_dup/ (this one has the same file hierarchy as dir1)
    - dir1_var1/
        - test_dir.py
        - sub1/
            - test_sub1.py
    - dir1_var2/
        - test_dir.py
        - sub1/
            - test_sub1.py
    - dir2/
        - test_dir.py
        - test_dir_1.py
    - dir3/
        - test_dir.py
        - test_dir_1.py
        - sub1/
            - test_sub1.py
        - sub3/
            - test_sub3.py
    - dir3_var1/
        - test_dir.py
        - test_dir_1.py
        - sub1/
            - test_sub1.py
        - sub3/
            - test_sub3.py
            - sub4/
                - test_sub4.py
"""

"""
Test cases:
1. when more than 2 paths or less than 2 paths of directories are inputed, print out instruction messages
logs:
$ python pydiff.py dir2/ dir1/ dir3/
Please input only 2 path of directories like: python py_diff.py dir1 dir2
$ python pydiff.py dir2/
Please input only 2 path of directories like: python py_diff.py dir1 dir2
$ python pydiff.py
Please input only 2 path of directories like: python py_diff.py dir1 dir2

2. test out two directories with same files (same contents) and sub directories (same file content in sub directories)
logs:
$ python pydiff.py dir1/ dir1_dup/
=============================
Check main directory
=============================
=============================
Check same sub directory
=============================

3. test out two directories with different file names in main and different sub directories
logs:
$ python pydiff.py dir1/ dir2/
=============================
Check main directory
=============================
File/dir ONLY found in dir2/: test_dir_1.py
File/dir ONLY found in dir1/: sub1
=============================
Check same sub directory
=============================

4. test out two directories with same file name with different contents in main, and same file names with same contents in sub
logs:
$ python pydiff.py dir1/ dir1_var1/
=============================
Check main directory
=============================
Same file name with DIFFERENT contents found in both directories:
dir1_var1/
dir1/
File: test_dir.py
=============================
Check same sub directory
=============================

5. test out two directories with same file name with same contents in main, and same file names with different contents in sub
logs:
$ python pydiff.py dir1/ dir1_var2/
=============================
Check main directory
=============================
=============================
Check same sub directory
=============================
Same file name with DIFFERENT contents found in both directories:
dir1_var2/sub1
dir1/sub1
File: test_sub1.py

6. test out two directories with different file names in main and sub, and different numbers of sub directories
logs:
$ python pydiff.py dir1/ dir3/
=============================
Check main directory
=============================
File/dir ONLY found in dir3/: sub3
File/dir ONLY found in dir3/: test_dir_1.py
=============================
Check same sub directory
=============================
Same file name with DIFFERENT contents found in both directories:
dir3/sub1
dir1/sub1
File: test_sub1.py

7. est out two directories with same files in main and sub, and different hierarchy of sub directories
logs:
python pydiff.py dir3_var1/ dir3/
=============================
Check main directory
=============================
=============================
Check same sub directory
=============================
File/dir ONLY found in dir3_var1/sub3: sub4
"""

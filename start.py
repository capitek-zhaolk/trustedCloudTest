# coding: utf-8

import os


def main():
    dirname = os.path.join(os.path.abspath(os.curdir), "testcase")
    print dirname, "..................."
    filenames = os.listdir(dirname)
    filenames.sort(key=lambda x: x[4:-3])

    for filename in filenames:
        file_path = os.path.join(dirname, filename)
        if os.path.isfile(file_path):
            print "begin to run '%s'" % file_path
            result = os.system("python %s" % file_path)
            print "%s output %s" % (filename, result)

if __name__ == '__main__':
    main()

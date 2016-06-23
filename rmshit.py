import os
import sys
import shutil


shittyfiles = [
	'~/_viminfo',
	'~/.bash_history',
	'~/AppData/Local/Temp',
	'~/Downloads',
	'/temp/*'
]


def yesno(question, default="n"):
    """ Asks the user for YES or NO, always case insensitive.
        Returns True for YES and False for NO.
    """
    prompt = "%s (y/[n]) " % question

    ans = raw_input(prompt).strip().lower()

    if not ans:
        ans = default

    if ans == "y":
        return True
    return False

def errHandler(f, path, e):
	print e
	print "{0}: {1}".format(path, e[1].strerror)

def rmshit():
    print("Found shittyfiles:")
    found = []
    for f in shittyfiles:
        absf = os.path.expanduser(f)
        if os.path.exists(absf):
            found.append(absf)
            print("    %s" % f)

    if len(found) == 0:
        print("No shitty files found :)")
        return

    if yesno("Remove all?", default="n"):
        for f in found:
            if os.path.isfile(f):
				try:
					os.remove(f)
				except OSError as e:
					errHandler(e)
            else:
                shutil.rmtree(f, False, errHandler)
        print("All cleaned")
    else:
        print("No file removed")


if __name__ == '__main__':
    rmshit()

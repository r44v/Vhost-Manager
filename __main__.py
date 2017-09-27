import ctypes, sys
from vhost import program


def is_admin():
    try:
        return ctypes.windll.shell32.IsUserAnAdmin()
    except:
        return False

if is_admin():
    program()
    print("Added data to specified vhost and hosts files\n\nDo not forget to restart your web server\n\n")
    input("Press enter to exit")

else:
    # Re-run the program with admin rights
    args = " ".join(sys.argv)
    ctypes.windll.shell32.ShellExecuteW(None, "runas", sys.executable, args, None, 1)
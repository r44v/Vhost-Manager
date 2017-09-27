
#  Specify vhost info, each dict in list is an new vhost
data = [
    {
        "url": "localhost",
        "path": "C:/xampp/htdocs/"
    },
    {
        "url": "simplesidebar.local.dev",
        "path": "C:/xampp/htdocs/startpages/simple_sidebar/public"
    },
        ]

# Specify the needed files, current data are the defaults in windows with xampp
vhost_file = r"C:\xampp\apache\conf\extra\httpd-vhosts.conf"
hosts_file = r"C:\Windows\System32\drivers\etc\hosts"


def get_vhost(path, url):
    """
    Creates apache vhost config text

    :param path:
    :param url:
    :return:
    """

    info = """
<VirtualHost *:80>
    DocumentRoot "%%path%%"
    ServerName "%%url%%"
    ServerAlias "%%url%%"
    <Directory "%%path%%">
        AllowOverride All
        Require all Granted
    </Directory>
</VirtualHost>
""".replace("%%url%%", url).replace("%%path%%", path)
    return info


def get_hosts(path, url):
    """
    Creates windows host file config data

    :param path:
    :param url:
    :return: string
    """

    info = """
# host for %%path%%
127.0.0.1\t%%url%%
""".replace("%%url%%", url).replace("%%path%%", path)
    return info


def write_to_vhost_manager_area(target_file, text_data):
    """
    Writes <text_data> to <target_file>

    :param target_file:
    :param text_data:
    :return:
    """

    open_tag = "##>{{VHOST_MANAGER}}"
    close_tag = "##<{{VHOST_MANAGER}}"

    file_lines = tuple(open(target_file, 'r'))
    file_handle = open(target_file, 'w')

    opened = False
    for line in file_lines:
        line = line.replace("\n", "")
        if line == open_tag:
            opened = True
            file_handle.write(line)
            file_handle.write("\n")
            file_handle.write(text_data)
            file_handle.write("\n")
        elif line == close_tag:
            opened = False
            file_handle.write(line)
            file_handle.write("\n")
        elif opened:
            continue
        else:
            file_handle.write(line)
            file_handle.write("\n")


def program():
    """
    Executes main program

    :return:
    """

    vhost = ""
    for info in data:
        path = info["path"]
        url = info["url"]
        vhost += get_vhost(path, url)

    hosts = ""
    for info in data:
        path = info["path"]
        url = info["url"]
        hosts += get_hosts(path, url)

    write_to_vhost_manager_area(vhost_file, vhost)
    write_to_vhost_manager_area(hosts_file, hosts)

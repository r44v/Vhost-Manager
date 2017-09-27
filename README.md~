# Vhost manager
For windows with xampp

## Script info
Written for Python 3.6 with no extra libraries

Tested with [2017-07-11] XAMPP for Windows 7.1.7-0

This script requests admin rights because it rewrites your hosts file

## Why?

Intially I used a simular script writting in php and I combined it with python to actually write the changes. I deciced the configuration whas to much of a hassle so I rewrote it in python. It works great for laravel projects because each new project needs its own vhost.

## Initial configuration

Put the following in both your vhost config file and your windows hosts file

```
##>{{VHOST_MANAGER}}

##<{{VHOST_MANAGER}}
```

the files should be at the following locations

```
C:\xampp\apache\conf\extra\httpd-vhosts.conf
C:\Windows\System32\drivers\etc\hosts
```

if the locations are different please change the 'vhost_file' and 'hosts_file' variables in vhost.py

## Adding vhosts

Edit the following lines in the vhost.py file to add an new vhost location and a local url.

```python
data = [
    {
        "url": "localhost",
        "path": "C:/xampp/htdocs/"
    },
    {
        "url": "newproject.local.dev",
        "path": "C:/xampp/htdocs/newproject/public"
    },
        ]
```

side note: *this script does not create the specified path it only points to the location*

## Licence
The Unlicense

Totally free to use
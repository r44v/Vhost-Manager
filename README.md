# Vhost manager
For windows with xampp

## Script info
Written for Python 3.6 with no extra libraries
Tested with [2017-07-11] XAMPP for Windows 7.1.7-0
This script requests admin rights because it rewrites your hosts file

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

Edit the following lines in the vhost.py file

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

## Licence
The Unlicense

Totally free to use
import os


Params = {
    "server": "192.168.1.5",
    "port": 8000,
    "url": "/assets/report/",
    "request_timeout": 30,
}

PATH = os.path.join(os.path.dirname(os.getcwd()), 'log', 'cmdb.log')

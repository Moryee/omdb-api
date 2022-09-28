# gunicorn.conf.py

accesslog = "/home/app/web/log/gunicorn.access.log"
errorlog = "/home/app/web/log/gunicorn.error.log"
capture_output = True

loglevel = "info"

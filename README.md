This base python template works has arguments and logging automatically setup for you.
Logging is configured by logging.yaml file

Arguments are configured in the getArgs function under TEMPLATE FUNCTIONS section.

LOGGING USE AS FOLLOWS
INFORMATIONAL MESSAGES
Confirmation that things are working as expected.
    info("This is an example informational message")
    
DEBUG MESSAGES
Detailed information, typically of interest only when diagnosing problems.
    *debug("You should know about %s" % (somevariable))
    
WARNING MESSAGES
An indication that something unexpected happened, or indicative of some problem in the 
near future (e.g. ‘disk space low’). The software is still working as expected.
    if <<something isn't quite right>>:
        warning("Something isn't quite right")

ERROR MESSAGES
Due to a more serious problem, the software has not been able to perform some function.
    try:
        something
    except as e:
        error(e)
```
# PythonTemplate
usage: base.py [-h] [-l LOGFILE] [-c LOGCONFIG] [-d] [-v]

optional arguments:
  -h, --help            show this help message and exit
  -l LOGFILE, --logfile LOGFILE
                        Logging Filename (default is script_name.log)
  -c LOGCONFIG, --logconfig LOGCONFIG
                        Logging Configuration File (default is logging.yaml)
  -d, --debug           Set Debug
  -v, --verbose         Set Logging to Verbose
  ```

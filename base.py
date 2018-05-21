# -*- coding: utf-8 -*-

__author__ = 'Jason Smith'
__credits__ = []
__email__ = "jasons2@cisco.com"

"""
Template for Python Scripts.
"""

### BASE IMPORTS
import logging
import logging.config
import yaml
import argparse

### IMPORTS


## BASE FUNCTIONS
def setupLogging(logconfig, logfile, verbose, debug):
    """
    Setup logging configuration
    """
    global config

    with open(logconfig, 'rt') as f:
        config = yaml.safe_load(f.read())
 
    if logfile:
        configureLogging(handler='file_handler', filename=logfile)

    if verbose:
        configureLogging(handler='file_handler', formatter='verbose')
        configureLogging(handler='console', formatter='verbose')
    
    if debug:
        configureLogging(handler='file_handler', level='DEBUG')
        configureLogging(handler='console', level='DEBUG')
    
    logging.config.dictConfig(config)

def configureLogging(handler='', formatter='', level='', filename=''):
    """
    """
    global config, logger
    if formatter:
        config['handlers'][handler]['formatter'] = formatter
    if level:
        config['handlers'][handler]['level'] = level
    if filename and handler =='file_handler':
        config['handlers'][handler]['filename'] = filename

    logging.config.dictConfig(config)

def getArgs():
    """
    Get Arguments from Command Line.  Set defaults for logfile, logconfig, debug and verbose.
    """
    parser = argparse.ArgumentParser()
    parser.set_defaults(logfile='',
                        logconfig = 'logging.yaml',
                        debug=False,
                        verbose=False)

    parser.add_argument('-l', '--logfile', help='Logging Filename (default is script_name.log)')
    parser.add_argument('-c', '--logconfig', help='Logging Configuration File (default is logging.yaml)')
    parser.add_argument('-d', '--debug', help='Set Debug', dest='debug', action='store_true')
    parser.add_argument('-v', '--verbose', help='Set Logging to Verbose', dest='verbose', action='store_true')

    output = parser.parse_args()  # assign contents of parser to output.

    if not output.logfile:  # Check to see if there is a logfile in command line.
        # Assign logfile to name of script plus .log
        output.logfile = __file__.split(".")[0] + ".log"

    return output

def info(msg):
    logger.info(msg)

def error(msg):
    logger.error(msg)

def warning(msg):
    logger.warning(msg)

def debug(msg):
    logger.debug(msg)

### HELPER FUNCTIONS


### MAIN FUNCTION
def main():
    """
    Main Function
    """
    info("Starting Program %s" % (__file__))
    
### MAIN PROGRAM
if __name__ == "__main__":
    # Create an initial logger. It will only log to console and it will disabled
    # when we read the logging configuration from the config file.
    logging.basicConfig(level="INFO",
                        format='%(asctime)s [%(levelname)s] : %(name)s : %(message)s',
                        datefmt='%D %I:%H:%M')
    logger = logging.getLogger()
    # Example of Configuring Logging Levels for External Modules
    #mlogger = logging.getLogger('mimir')
    #mlogger.setLevel(logging.INFO)

    args = getArgs()  # Get arguments from command line.
    # Setup default logging based on default config file.  Previous config is overwritten
    setupLogging(logconfig=args.logconfig, logfile=args.logfile, verbose=args.verbose, debug=args.debug)

    main()

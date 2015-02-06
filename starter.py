from logging.handlers import HTTPHandler
import sys
import logging
import time

#simulates client initiates command to machine
if (sys.argv[1] == "get"):
	logger = logging.getLogger('starter')
	logger.setLevel(logging.DEBUG)
	logger.addHandler(HTTPHandler("localhost:8888", "/"))
	logger.warning('testing GET')

#simulates machine initiates a POST to client
if (sys.argv[1] == "post"):
	logger = logging.getLogger('mylogger')
	logger.setLevel(logging.WARNING)
	logger.addHandler(HTTPHandler("localhost:8888", "/", method='POST'))
	logger.warning('testing POST')





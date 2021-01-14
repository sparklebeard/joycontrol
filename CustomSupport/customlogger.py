import sys

class Logger:
	# def __init__(self):

	def info(self, message):
		print(f'Info log: {message}', flush=True)

	def warning(self, message: str):
		print(f'Warning log: {message}', flush=True)

	def debug(self, message: str):
		print(f'Debug log: {message}')

	def error(self, message):
		print(f'Error log: {message}', file=sys.stderr, flush=True)

	def critical(self, message):
		print(f'Critical log: {message}', file=sys.stderr, flush=True)

def getLogger(arg):
	return Logger()
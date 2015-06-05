import argparse

parser = argparse.ArgumentParser(description='Set logging level')
parser.add_argument('--log_level', nargs=1, default='DEBUG', #dest='loggingLevel',
		     help="Set the Logging level for the script")
#parser.add_argument('--foo' )

args = parser.parse_args()

if args.log_level:
   print "log level"
try: 
   args.foo
   print "foo"
except: 
   pass

import argparse

# python logging_argparse.py --log_level=ERROR
# python logging_argparse.py --log_level ERROR

parser = argparse.ArgumentParser(description='Set logging level')
parser.add_argument('--log_level', nargs=1, default=["DEBUG"], #dest='loggingLevel',
		     help="Set the Logging level for the script")
parser.add_argument('--foo' )
parser.add_argument('--bar', default='baz')

args = parser.parse_args()

if hasattr(args, 'log_level') and args.log_level:
   print "log level " + str(args.log_level) #", ".join(args.log_level)
if hasattr(args, 'foo') and args.foo:
	print "foo is " 
if hasattr(args, 'bar') and args.bar:
	print "bar is " + args.bar

# A few gotcha's:
# setting nargs=N causes parser.parse_args to automatically generates a list even nargs=1
#  --log_level=ERROR returns args.loglevel=['ERROR']; so make default= a list also
# parser.add_argument(... default=None) so check if the argument is defined if args.bar: ...
# to check an argument had been defined by add_arguemnt hasattr(args, 'arg_name')
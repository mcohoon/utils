import logging
import sys

#
# Setup logging
#

# create module_logger using getLogger() 
module_logger = logging.getLogger('logging_basics_script_logger')
# set the logging level
module_logger.setLevel('DEBUG')

module_logger.addHandler(logging.StreamHandler(sys.stdout))
if module_logger.getEffectiveLevel() == logging.DEBUG:
   module_logger.debug("Loging level debug")

for handler in module_logger.handlers:
    module_logger.info(handler)


class Cat:
   def meow(self):
      """ cat onomatopoeia """
      module_logger.info("Call to meow method")

module_logger.error("foo")
module_logger.setLevel(logging.DEBUG)
module_logger.info("info")

if __name__ == "__main__":
    cat = Cat()
    cat.meow()

# # logging formatted with ASCII date time
# logger = logging.getLogger('script_logger')
# formatter = logging.Formatter("%(asctime)s %(levelname)s: %(message)s", "%Y-%m-%d %H:%M:%S")
# ch = logging.StreamHandler()
# ch.setFormatter(formatter)
# logger.addHandler(ch)
# logger.setLevel(logging.INFO)

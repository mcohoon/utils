import logging
import sys
# create logger
module_logger = logging.getLogger('spam_application.auxiliary')

module_logger.addHandler(logging.StreamHandler(sys.stdout))
if module_logger.getEffectiveLevel() == logging.DEBUG:
   print "Loging level debug"

for handler in module_logger.handlers:
    print handler


class Cat:
   def meow(self):
      """The sound a cat makes"""
      print "Meow!"
      module_logger.info("Someone Called Meow")

module_logger.error("foo")
module_logger.setLevel(logging.DEBUG)
module_logger.info("info")

if __name__ == "__main__":
    cat = Cat()
    cat.meow()

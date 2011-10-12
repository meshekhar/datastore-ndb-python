"""Alternate way of running the unittests, for Python 2.5 or Windows."""

__author__ = 'Beech Horn'

import sys
import unittest


def suite():
  mods = ['context', 'eventloop', 'key', 'model', 'query', 'tasklets', 'thread']
  test_mods = ['%s_test' % name for name in mods]
  ndb = __import__('ndb', fromlist=test_mods, level=1)

  loader = unittest.TestLoader()
  suite = unittest.TestSuite()

  for mod in [getattr(ndb, name) for name in test_mods]:
    for name in set(dir(mod)):
      if name.endswith('Tests'):
        test_module = getattr(mod, name)
        tests = loader.loadTestsFromTestCase(test_module)
        suite.addTests(tests)

  return suite


def main():
  v = 0
  q = 0
  for arg in sys.argv[1:]:
    if arg.startswith('-v'):
      v += arg.count('v')
    elif arg == '-q':
      q += 1
  if q:
    v = 0
  else:
    v = max(v, 1)
  unittest.TextTestRunner(verbosity=v).run(suite())


if __name__ == '__main__':
  main()

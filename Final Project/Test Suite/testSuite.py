import unittest
from ..Admin.adminTest import TestAdmin
from .login import TestLogin

login = unittest.TestLoader().loadTestsFromTestCase(TestLogin)
admin = unittest.TestLoader().loadTestsFromTestCase(TestAdmin)

test_suite = unittest.TestSuite([login, admin])

# run the suite
unittest.TextTestRunner(verbosity=2).run(test_suite)
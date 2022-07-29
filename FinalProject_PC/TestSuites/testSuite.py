import unittest

from Admin.adminTest import TestAdmin
from Login.login import TestLogin


login = unittest.TestLoader().loadTestsFromTestCase(TestLogin)
admin = unittest.TestLoader().loadTestsFromTestCase(TestAdmin)

test_suite = unittest.TestSuite([login, admin])

# run the suite
unittest.TextTestRunner().run(test_suite)
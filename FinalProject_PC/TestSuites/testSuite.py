import unittest

from Admin.adminTest import TestAdmin
from Login.login import TestLogin
from Buzz.buzzTest import TestBuzz
from Directory.directoryTest import TestDirectory
from Leave.leaveTest import TestLeave
from Performance.performanceTest import TestPerformance
from PIM.pimTest import TestEmployeeList
from Recruitment.recruitmentTest import TestRecruitment
from Time.timeTest import TestTime


login = unittest.TestLoader().loadTestsFromTestCase(TestLogin)
admin = unittest.TestLoader().loadTestsFromTestCase(TestAdmin)
buzz = unittest.TestLoader().loadTestsFromTestCase(TestBuzz)
directory = unittest.TestLoader().loadTestsFromTestCase(TestDirectory)
leave = unittest.TestLoader().loadTestsFromTestCase(TestLeave)
performance = unittest.TestLoader().loadTestsFromTestCase(TestPerformance)
pim = unittest.TestLoader().loadTestsFromTestCase(TestEmployeeList)
recruitment = unittest.TestLoader().loadTestsFromTestCase(TestRecruitment)
time = unittest.TestLoader().loadTestsFromTestCase(TestTime)

test_suite = unittest.TestSuite([login, admin, buzz, directory, leave, performance, pim, recruitment, time])

# run the suite
unittest.TextTestRunner().run(test_suite)
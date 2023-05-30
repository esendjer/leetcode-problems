# from typing import NoneType
import unittest
import logging


import my_hash_set

CALLS = (
    ["MyHashSet","add","add","contains","contains","add","contains","remove","contains"],
    ["MyHashSet","add","add","contains","contains","add","contains","remove","contains","add","contains"],
)
CASES = (
     [[],[1],[2],[1],[3],[2],[2],[2],[2]],
     [[],[1],[2],[1],[3],[2],[2],[2],[2],[1000000],[1000000]],
)
RESULTS = (
    [None,None,None,True,False,None,True,None,False],
    [None,None,None,True,False,None,True,None,False,None,True],
)

class TestSolution(unittest.TestCase):
    logger = logging.getLogger(__name__)

    def runTest(self):
        for i, calls in enumerate(CALLS):
            to_test = my_hash_set
            class_to_test = getattr(to_test, calls[0], "blah-blah")
            self.logger.warning("=> %s, %s", str(calls[0]), str(i))
            self.assertNotEqual(isinstance(class_to_test, str), True)
            to_test = class_to_test()
            for case_i in range(1, len(calls)):
                test_call = getattr(to_test, calls[case_i], False)
                test_res = test_call(*CASES[i][case_i])
                wanted_res = RESULTS[i][case_i]
                self.assertEqual(test_res, wanted_res)



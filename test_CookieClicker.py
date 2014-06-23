import unittest
import random
from CookieClicker import ClickerState


class ClickerStateInitializeTests(unittest.TestCase):
    """
    This class is a unit tester of the "Clicker State" class for the Cookie Clicker assignement
    """
    
    def setUp(self):
        self.test_object = ClickerState()
    
    def test_ClickerState_InitializeTotalCookies_CheckZeroTotalCookies(self):
        expected = 0.0
        
        test_object = ClickerState()
        actual = test_object._total_cookies
        
        self.assertEqual(expected, actual)
        
    def test_ClickerState_InitializeCurrentCookies_VerifyZeroCurrentCookies(self):
        expected = 0.0
        
        test_object = ClickerState()
        actual = test_object._current_cookies
        
        self.assertEqual(expected, actual)
        
    def test_ClickerState_InitializeCurrentTime_VerifyZeroCurrentTime(self):
        expected = 0.0
        
        actual = self.test_object._current_time
        
        self.assertEqual(expected, actual)
        
    def test_ClickerState_InitializeCookiePerSecond_VerifyOnePerSecondCookieRate(self):
        expected = 1.0
        
        actual = self.test_object._cookies_per_second
        
        self.assertEqual(expected, actual)
        
    def test_ClickerState_InitializeHistoryList_VerifyFourItemListOfThreeZeroesAndOneNone(self):
        expected = [0.0, None, 0.0, 0.0]
        
        actual = self.test_object._history_list
        
        self.assertEqual(expected, actual)
        
        
        
        
        
    
    
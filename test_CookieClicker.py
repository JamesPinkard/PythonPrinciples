import unittest
import random
from CookieClicker import *


class ClickerStateInitializeTests(unittest.TestCase):
    """
    This class is a unit tester of the initializer for the "Clicker State" class for the Cookie Clicker assignement
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
        expected = [(0.0, None, 0.0, 0.0)]
        
        actual = self.test_object._history_list
        
        self.assertEqual(expected, actual)
        
class ClickerStateStrTests(unittest.TestCase):
    """
    This class is a unit tester of the str method for the "Clicker State" class for the Cookie Clicker assignement
    """
    def setUp(self):
        self.tester_object = ClickerState()
    
    
    def test_StrMethod_CallStringOnInitializedClickerState_ReturnStringOfCookieAndTimeStatus(self):
        expected = 'Total Cookies: 0.0\n' \
        'Current Cookies: 0.0\n' + \
        'Current Time: 0.0\n' + \
        'Cookies Per Second: 1.0'
        test_ClickerStateObject = ClickerState()
        
        actual = str(test_ClickerStateObject)
        
        self.assertEqual(expected,  actual)
        
    def test_StrMethod_CallStringOnAllTwoStatus_ReturnStringOfAllTwo(self):
        expected = 'Total Cookies: 2.0\n' \
        'Current Cookies: 2.0\n' + \
        'Current Time: 2.0\n' + \
        'Cookies Per Second: 2.0'         
        self.tester_object._total_cookies = 2.0
        self.tester_object._current_cookies = 2.0
        self.tester_object._current_time = 2.0
        self.tester_object._cookies_per_second = 2.0
        
        actual = str(self.tester_object)
        
        self.assertEqual(expected, actual)
        
class ClickerStateGetMethodsTests(unittest.TestCase):
    """
    This class is a unit tester of the get methods for the "Clicker State" class for the Cookie Clicker assignement
    """
    def setUp(self):
        self.tester_object = ClickerState()
        self.expected = 0.0
        self.actual = 1.0
        
    
    def verify_expected_equals_actual(self):
        """
        Tests whether the expected value is equal to the actual value
        """
        self.assertEqual(self.expected, self.actual)
        
        
        
    def test_GetCookies_InitialState_ReturnZeroCookies(self):
        expected = 0.0
        
        actual = self.tester_object.get_cookies()
        
        self.assertEqual(expected, actual)
        
    def test_GetCookies_TwoCookies_ReturnTwoCookies(self):
        expected = 2.0
        self.tester_object._current_cookies = 2.0
        
        actual = self.tester_object.get_cookies()
        
        self.assertEqual(expected, actual)
        
    def test_GetRate_Initial_ReturnOne(self):
        
        self.expected = 1.0
        
        self.actual = self.tester_object.get_cps()
        
        self.verify_expected_equals_actual()
        
    def test_GetRate_RateOfTwo_ReturnTwo(self):
        
        self.expected = 2.0
        self.tester_object._cookies_per_second = 2.0
        
        self.actual = self.tester_object.get_cps()
        
        self.verify_expected_equals_actual
        
    def test_GetTime_Initial_ReturnZero(self):
        
        self.expected = 0.0
        
        self.actual = self.tester_object.get_time()
        
        self.verify_expected_equals_actual()
        
    def test_GetTime_TwoSeconds_ReturnTwo(self):
        
        self.expected = 2.0
        self.tester_object._current_time = 2.0
        
        self.actual = self.tester_object.get_time()
        
        self.verify_expected_equals_actual()
        
    def test_GetHistory_Initial_ReturnListOfThreeZeroesAndOneNone(self):
        
        self.expected = [(0.0, None, 0.0, 0.0)]
        
        self.actual = self.tester_object.get_history()
        
        self.verify_expected_equals_actual()    
        
    def test_GetHistory_ClickerBought_ReturnListOfTwoTuples(self):
        #Arrange
        self.expected = [(0.0, None, 0.0, 0.0), (5.0, "Clicker", 5.0, 5.0)]
        self.tester_object._current_time = 5.0
        self.tester_object._total_cookies = 5.0
        
        current_time = self.tester_object.get_time()
        total_cookies = self.tester_object._total_cookies
        item = "Clicker"
        cost_of_item = 5.0
        tuple_to_append = (current_time, item, cost_of_item, total_cookies)
        
        self.tester_object._history_list.append(tuple_to_append)
        
        #Act
        self.actual = self.tester_object.get_history()
        
        #Assert
        self.verify_expected_equals_actual()
        
class ClickerStateTimeUntilTests(unittest.TestCase):
    """
    This class is a unit tester of the get methods for the "Clicker State" class for the Cookie Clicker assignement
    """
    def setUp(self):
        self.tester_object = ClickerState()
        self.expected = 0.0
        self.actual = 1.0
        
    
    def verify_expected_equals_actual(self):
        """
        Tests whether the expected value is equal to the actual value
        """
        self.assertEqual(self.expected, self.actual)
        
    def test_TimeUntil_InitialSettingsTenCookieInquiery_ReturnTen(self):
        
        self.expected =  10.0
        number_of_cookies = 10.0
        
        self.actual = self.tester_object.time_until(number_of_cookies)
        
        self.verify_expected_equals_actual()
        
    def test_TimeUntil_InitialSettingsTwentyCookieInquiery_ReturnTwenty(self):
        
        self.expected = 20.0
        number_of_cookies = 20.0
        
        self.actual = self.tester_object.time_until(number_of_cookies)
        
        self.verify_expected_equals_actual()
        
    def test_TimeUntil_TwoCookiesPerSecondsSevenCookieInquiery_ReturnTwenty(self):
        
        self.expected = 4.0
        number_of_cookies = 7.0
        self.tester_object._cookies_per_second = 2
        
        self.actual = self.tester_object.time_until(number_of_cookies)
        
        self.verify_expected_equals_actual()
        
    def test_TimeUntil_TwoCookiesPerSecondsCurrentlyWithTwoCookiesSevenCookieInquiery_ReturnTwenty(self):
        
        self.expected = 3.0
        number_of_cookies = 7.0
        self.tester_object._cookies_per_second = 2
        self.tester_object._current_cookies = 2
        
        self.actual = self.tester_object.time_until(number_of_cookies)
        
        self.verify_expected_equals_actual()
        
class ClickerStateWaitTests(unittest.TestCase):
    """
    This class is a unit tester of the get methods for the "Clicker State" class for the Cookie Clicker assignement
    """
    def setUp(self):
        self.tester_object = ClickerState()
        self.expected = 0.0
        self.actual = 1.0
        
    
    def verify_expected_equals_actual(self):
        """
        Tests whether the expected value is equal to the actual value
        """
        self.assertEqual(self.expected, self.actual)
        
    def test_Wait_InitialToTenSeconds_CheckStatusForTen(self):
        self.expected = [10.0,10.0,10.0]
        
        self.tester_object.wait(10.0)
        actual_total_cookies= self.tester_object._total_cookies
        actual_current_cookies= self.tester_object._current_cookies
        actual_current_time= self.tester_object._current_time
        self.actual=[actual_current_cookies,actual_current_time,actual_total_cookies]
        
        self.verify_expected_equals_actual()
        
    def test_Wait_ThreeCPSWaitForTenSeconds_StateOfThirtyCookiesInTenSeconds(self):
        self.set_expected_end_status(30.0,10.0,30.0)
        self.set_cps(3.0)
        
        self.object_wait(10.0)
        
        self.verify_expected_equals_actual()
        
    def test_Wait_ThreeCPSTenTotalCookiesFiveCurrentCookiesWaitForTwentySeconds_StateOfSeventyTotalInTwentySeconds(self):
        self.set_expected_end_status(65.0,20.0,70.0)
        self.tester_object._current_cookies= 5.0
        self.tester_object._total_cookies = 10.0
        self.set_cps(3.0)
        
        self.object_wait(20.0)
        
        self.verify_expected_equals_actual()
        
    def set_expected_end_status(self,current_cookies,current_time,total_cookies):
        self.expected = [current_cookies,current_time,total_cookies]    

    def set_cps(self,rate):
        self.tester_object._cookies_per_second = rate
        

        

    def object_wait(self, time):
        self.tester_object.wait(time)
        actual_total_cookies= self.tester_object._total_cookies
        actual_current_cookies= self.tester_object._current_cookies
        actual_current_time= self.tester_object._current_time
        self.actual=[actual_current_cookies,actual_current_time,actual_total_cookies]
    
        
        
class ClickerStateBuyTests(unittest.TestCase):
    """
    This class is a unit tester of the get methods for the "Clicker State" class for the Cookie Clicker assignement
    """
    def setUp(self):
        self.tester_object = ClickerState()
        self.expected_cps = 0.0
        self.expected_history = [(None,None,None,None)]
        self.expected_current_cookies = 0.0
               
        
    
    def verify_history_time_and_cookies(self):
        """
        Tests whether the expected value is equal to the actual value
        """
        self.assertEqual(self.expected_cps, self.tester_object._cookies_per_second)
        self.assertEqual(self.expected_history, self.tester_object._history_list)
        self.assertEqual(self.expected_current_cookies, self.tester_object._current_cookies)
        
    def test_BuyItem_InitialBuyClickerCantAfford_UnalteredState(self):
        self.expected_cps = 1.0
        self.expected_history = [(0.0, None, 0.0, 0.0)]
        self.expected_current_cookies = 0.0
        
        self.tester_object.buy_item("Clicker", 5.0, 1.0)
        
        self.verify_history_time_and_cookies()
        
    def test_BuyItem_FiveCookiesBuyClicker_StateOfZeroCookiesAndTwoCPS(self):
        self.expected_cps = 2.0
        self.expected_history = [(0.0, None, 0.0, 0.0), (5.0, "Clicker", 5.0, 5.0)]
        self.expected_current_cookies = 0.0
        self.tester_object._current_cookies = 5.0
        self.tester_object._total_cookies = 5.0
        self.tester_object._current_time = 5.0
        
        self.tester_object.buy_item("Clicker", 5.0, 1.0)
        
        self.verify_history_time_and_cookies()
        
    def test_BuyItem_ThirteenCookiesBuyTwoClickers_StateOfThreeCookiesAndThreeCPS(self):
        self.expected_cps = 3.0
        self.expected_current_cookies = 3.0
        self.expected_history = [(0.0, None, 0.0, 0.0), (13.0, "Clicker", 5.0, 13.0),(13.0, "Clicker", 5.0, 13.0)]
        self.tester_object._current_cookies = 13.0
        self.tester_object._total_cookies = 13.0
        self.tester_object._current_time = 13.0
        
        self.tester_object.buy_item("Clicker", 5.0, 1.0)
        self.tester_object.buy_item("Clicker", 5.0, 1.0)
        
        self.verify_history_time_and_cookies()
        
    
        
    
    

    
    
        
        
        
        
        
    
    
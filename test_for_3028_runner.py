import time,unittest
from HTMLTestRunner1 import HTMLTestRunner
from selenium import webdriver

testcase_box = 'D:/test3028/testcase'
discover_case = unittest.defaultTestLoader.discover(testcase_box, pattern = 'test*.py')

if __name__ == '__main__':
	#unittest.main()
	#testunit = unittest.TestSuite()
	#testunit.addTest(Case3028('test_searchname_case'))

	nowtime = time.strftime('%Y-%m-%d %H_%M_%S')

	resfilename ='D:/test3028/TestReport/' + nowtime + '-3028内管平台测试报告.html'
	here = open(resfilename,'wb')

	runner = HTMLTestRunner(stream = here, 
							title = '三年二班内管平台测试报告', 
							description = '用例执行情况：',
							verbosity = 2)

	runner.run(discover_case)

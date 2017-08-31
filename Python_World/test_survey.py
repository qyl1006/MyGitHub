import unittest
from survey import AnonymousSurvey

class TestAnonymousSurvey(unittest.TestCase):
	"""针对AnonymousSurvey类的测试方法使用"""
	#question = 'What language did you first lerm to speak?'
	#self.my_survey = AnonymousSurvey(question)
	#self,responses = ['English', 'Spanish', 'Mandarin']
	def setUp(self):
	"""创建一个调查对象和一组答案，供使用的测试的"""
	question = 'What language did you first lerm to speak?'
	self.my_survey = AnonymousSurvey(question)
	self.responses = ['English', 'Spanish', 'Mandarin']
	
	
	def test_store_single_reponse(self):
		"""测试单个答案会被存储"""
		#question = 'What language did you first lerm to speak?'
		#my_survey = AnonymousSurvey(question)
		self.my_survey.store_response(self.responses[0])
		
		self.assertIn(self.responses[0], self.my_survey.responses)
		
	def test_store_single_reponses(self):
		"""测试三个答案会被存储"""
		question = 'What language did you first lerm to speak?'
		my_survey = AnonymousSurvey(question)
		responses = ['English', 'Spanish', 'Mandarin']
		for response in responses:
			my_survey.store_response(response)
		
		self.assertIn('English',my_survey.responses)
			
		
unittest.main()
		

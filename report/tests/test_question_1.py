import unittest

from report.questions import Questions
from report.report import Report
from report.text import Text


class TestingQuestions(unittest.TestCase):

    def test_question_1(self):
        question = Questions.what_is_your_favorite_activity(
            Questions.survey.Q1)
        result: str = Report.generate(question)
        self.assertEqual(result, Text.STRENGTH_AND_NO_ACTIVITY)

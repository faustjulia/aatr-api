import unittest
from typing import Dict

from report.answer import Answer
from report.questions import Questions
from report.survey import Survey
from report.tests.common.base import TestCommon
from report.text import Text


class TestFavoriteActivity(TestCommon):

    def test_answer_aerobics(self):
        answers: Dict = self.test_answers.copy()
        answers.update({'Q1': Answer.AEROBICS})

        survey = Survey(
            answers=answers
        )
        questions = Questions(survey=survey)

        result: str = questions.what_is_your_favorite_activity()
        self.assertEqual(result, Text.AEROBICS)

    def test_answer_no_activity(self):
        answers: Dict = self.test_answers.copy()
        answers.update({'Q1': Answer.NO_ACTIVITY})

        survey = Survey(
            answers=answers
        )

        questions = Questions(survey=survey)
        result: str = questions.what_is_your_favorite_activity()
        self.assertEqual(result, Text.NO_ACTIVITY)

    def test_answer_strength(self):
        answers: Dict = self.test_answers.copy()
        answers.update({'Q1': Answer.STRENGTH})

        survey = Survey(
            answers=answers
        )

        questions = Questions(survey=survey)
        result: str = questions.what_is_your_favorite_activity()
        self.assertEqual(result, Text.STRENGTH)

    def test_answer_balance(self):
        answers: Dict = self.test_answers.copy()
        answers.update({'Q1': Answer.BALANCE})

        survey = Survey(
            answers=answers
        )
        questions = Questions(survey=survey)
        result: str = questions.what_is_your_favorite_activity()
        self.assertEqual(result, Text.FLEXIBILITY_AND_BALANCE)

    def test_answer_flexibility(self):
        answers: Dict = self.test_answers.copy()
        answers.update({'Q1': Answer.FLEXIBILITY})

        survey = Survey(
            answers=answers
        )

        questions = Questions(survey=survey)
        result: str = questions.what_is_your_favorite_activity()
        self.assertEqual(result, Text.FLEXIBILITY_AND_BALANCE)


if __name__ == '__main__':
    unittest.main()

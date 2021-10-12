import unittest
from typing import Dict, List

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

    def test_answer_flexibility_and_balance(self):
        answers: Dict = self.test_answers.copy()
        test_answers: List = [
            [Answer.FLEXIBILITY],
            [Answer.BALANCE],
            [Answer.FLEXIBILITY, Answer.BALANCE]
        ]
        for answer in test_answers:
            answers['Q1'] = answer

            print("test answer: ", answer)

            survey = Survey(
                answers=answers
            )
            questions = Questions(survey=survey)
            result: str = questions.what_is_your_favorite_activity()
            self.assertEqual(result, Text.FLEXIBILITY_AND_BALANCE)


if __name__ == '__main__':
    unittest.main()

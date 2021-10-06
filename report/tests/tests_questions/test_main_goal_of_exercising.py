import unittest
from typing import Dict, List

from report.answer import Answer
from report.questions import Questions
from report.survey import Survey
from report.tests.common.base import TestCommon
from report.text import Text


class TestMainGoalOfExercising(TestCommon):

    def test_answer_have_a_good_time(self):
        answers: Dict = self.test_answers.copy()
        test_answers: List = [
            [Answer.HAVE_A_GOOD_TIME],
            [Answer.BE_HEALTHY],
            [Answer.HAVE_A_GOOD_TIME, Answer.BE_HEALTHY]
        ]
        for i in test_answers:
            for answer in i:
                answers['Q2'] = answer

            survey = Survey(
                answers=answers
            )

            questions = Questions(survey=survey)
            result: str = questions.what_is_the_main_goal_of_exercising()
            self.assertEqual(result, Text.HAVE_A_GOOD_TIME_OR_BE_HEALTHY)

    def test_answer_loose_weight(self):
        answers: Dict = self.test_answers.copy()
        test_answers: List = [
            [Answer.LOOSE_WEIGHT],
            [Answer.I_DONT_EXERCISE],
            [Answer.LOOSE_WEIGHT, Answer.I_DONT_EXERCISE]
        ]
        for i in test_answers:
            for answer in i:
                answers['Q2'] = answer

            survey = Survey(
                answers=answers
            )

            questions = Questions(survey=survey)
            result: str = questions.what_is_the_main_goal_of_exercising()
            self.assertEqual(result, Text.LOOSE_WEIGHT_OR_NO_EXERCISE)


if __name__ == '__main__':
    unittest.main()
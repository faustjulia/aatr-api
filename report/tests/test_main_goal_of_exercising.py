import unittest
from typing import Dict

from report.answer import Answer
from report.questions import Questions
from report.survey import Survey
from report.tests.common.base import TestCommon
from report.text import Text


class TestMainGoalOfExercising(TestCommon):

    def test_answer_have_a_good_time(self):
        answers: Dict = self.test_answers.copy()
        answers.update({'Q2': Answer.HAVE_A_GOOD_TIME})

        survey = Survey(
            answers=answers
        )

        questions = Questions(survey=survey)
        result: str = questions.what_is_the_main_goal_of_exercising()
        self.assertEqual(result, Text.HAVE_A_GOOD_TIME_OR_BE_HEALTHY)

    def test_answer_be_healthy(self):
        answers: Dict = self.test_answers.copy()
        answers.update({'Q2': Answer.BE_HEALTHY})

        survey = Survey(
            answers=answers
        )

        questions = Questions(survey=survey)
        result: str = questions.what_is_the_main_goal_of_exercising()
        self.assertEqual(result, Text.HAVE_A_GOOD_TIME_OR_BE_HEALTHY)

    def test_answer_loose_weight(self):
        answers: Dict = self.test_answers.copy()
        answers.update({'Q2': Answer.LOOSE_WEIGHT})

        survey = Survey(
            answers=answers
        )

        questions = Questions(survey=survey)
        result: str = questions.what_is_the_main_goal_of_exercising()
        self.assertEqual(result, Text.LOOSE_WEIGHT_OR_NO_EXERCISE)

    def test_answer_I_dont_exercise(self):
        answers: Dict = self.test_answers.copy()
        answers.update({'Q2': Answer.I_DONT_EXERCISE})

        survey = Survey(
            answers=answers
        )

        questions = Questions(survey=survey)
        result: str = questions.what_is_the_main_goal_of_exercising()
        self.assertEqual(result, Text.LOOSE_WEIGHT_OR_NO_EXERCISE)


if __name__ == '__main__':
    unittest.main()

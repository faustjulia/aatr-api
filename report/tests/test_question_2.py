import unittest
from typing import Dict

from report.answer import Answer
from report.questions import Questions
from report.survey import Survey
from report.text import Text

answers_dict: Dict = {
    'Q1': Answer.AEROBICS,
    'Q2': Answer.HAVE_A_GOOD_TIME,
    'Q3': [Answer.DAY_TIME, Answer.NEVER],
    'Q4': Answer.AGE_OR_BIRTHDATE,
    'Q5': {
        'choice': Answer.YES_TO_ACTIVITIES,
        'yes_choices': [
            Answer.HIKING,
            Answer.BIKING
        ]
    }
}


class TestingQuestions(unittest.TestCase):

    def test_question_2_answer_1(self):
        answers: Dict = answers_dict.copy()
        answers.update({'Q2': Answer.HAVE_A_GOOD_TIME})

        survey = Survey(
            answers=answers
        )

        questions = Questions(survey=survey)
        result: str = questions.what_is_the_main_goal_of_exercising()
        self.assertEqual(result, Text.HAVE_A_GOOD_TIME_OR_BE_HEALTHY)

    def test_question_2_answer_2(self):
        answers: Dict = answers_dict.copy()
        answers.update({'Q2': Answer.BE_HEALTHY})

        survey = Survey(
            answers=answers
        )

        questions = Questions(survey=survey)
        result: str = questions.what_is_the_main_goal_of_exercising()
        self.assertEqual(result, Text.HAVE_A_GOOD_TIME_OR_BE_HEALTHY)

    def test_question_2_answer_3(self):
        answers: Dict = answers_dict.copy()
        answers.update({'Q2': Answer.LOOSE_WEIGHT})

        survey = Survey(
            answers=answers
        )

        questions = Questions(survey=survey)
        result: str = questions.what_is_the_main_goal_of_exercising()
        self.assertEqual(result, Text.LOOSE_WEIGHT_OR_NO_EXERCISE)

    def test_question_2_answer_4(self):
        answers: Dict = answers_dict.copy()
        answers.update({'Q2': Answer.I_DONT_EXERCISE})

        survey = Survey(
            answers=answers
        )

        questions = Questions(survey=survey)
        result: str = questions.what_is_the_main_goal_of_exercising()
        self.assertEqual(result, Text.LOOSE_WEIGHT_OR_NO_EXERCISE)


if __name__ == '__main__':
    unittest.main()

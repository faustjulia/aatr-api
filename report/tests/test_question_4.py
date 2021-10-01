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

    def test_question_4_answer_1(self):
        answers: Dict = answers_dict.copy()
        answers.update({'Q4': 23})

        survey = Survey(
            answers=answers
        )
        questions = Questions(survey=survey)

        result: str = questions.what_is_your_age_group()
        self.assertEqual(result, Text.young_adult(self, age=23))

    def test_question_4_answer_2(self):
        answers: Dict = answers_dict.copy()
        answers.update({'Q4': 40})

        survey = Survey(
            answers=answers
        )
        questions = Questions(survey=survey)

        result: str = questions.what_is_your_age_group()
        self.assertEqual(result, Text.middle_age(self, age=40))

    def test_question_4_answer_3(self):
        answers: Dict = answers_dict.copy()
        answers.update({'Q4': 80})

        survey = Survey(
            answers=answers
        )
        questions = Questions(survey=survey)

        result: str = questions.what_is_your_age_group()
        self.assertEqual(result, Text.old_adulthood(self, age=80))


if __name__ == '__main__':
    unittest.main()

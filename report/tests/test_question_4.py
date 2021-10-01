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
    'Q4': '',
    'Q5': {
        'choice': Answer.YES_TO_ACTIVITIES,
        'yes_choices': [
            Answer.HIKING,
            Answer.BIKING
        ]
    }
}

text = Text()


class TestingQuestions(unittest.TestCase):

    def test_question_4_answer_1(self):
        answers: Dict = answers_dict.copy()

        survey = Survey(
            answers=answers
        )
        questions = Questions(survey=survey)

        result: str = questions.what_is_your_age_group(AGE_OR_BIRTHDATE=23)
        self.assertEqual(result, text.young_adult(age=23))

    def test_question_4_answer_2(self):
        answers: Dict = answers_dict.copy()

        survey = Survey(
            answers=answers
        )
        questions = Questions(survey=survey)

        result: str = questions.what_is_your_age_group(AGE_OR_BIRTHDATE=40)
        self.assertEqual(result, text.middle_age(age=40))

    def test_question_4_answer_3(self):
        answers: Dict = answers_dict.copy()

        survey = Survey(
            answers=answers
        )
        questions = Questions(survey=survey)

        result: str = questions.what_is_your_age_group(AGE_OR_BIRTHDATE=80)
        self.assertEqual(result, text.old_adulthood(age=80))

    def test_question_4_answer_4(self):
        answers: Dict = answers_dict.copy()

        survey = Survey(
            answers=answers
        )
        questions = Questions(survey=survey)

        result: str = questions.what_is_your_age_group(
            AGE_OR_BIRTHDATE='1998-03-11')
        self.assertEqual(result, text.old_adulthood(age='1998-03-11'))

        if __name__ == '__main__':
            unittest.main()

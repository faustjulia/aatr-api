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

    def test_question_1_answer_1(self):
        answers: Dict = answers_dict.copy()
        answers.update({'Q1': Answer.AEROBICS})

        survey = Survey(
            answers=answers
        )
        questions = Questions(survey=survey)

        result: str = questions.what_is_your_favorite_activity()
        self.assertEqual(result, Text.AEROBICS)

    def test_question_1_answer_2(self):
        answers: Dict = answers_dict.copy()
        answers.update({'Q1': Answer.BALANCE})

        survey = Survey(
            answers=answers
        )

        questions = Questions(survey=survey)
        result: str = questions.what_is_your_favorite_activity()
        self.assertEqual(result, Text.BALANCE)

    def test_question_1_answer_3(self):
        answers: Dict = answers_dict.copy()
        answers.update({'Q1': Answer.FLEXIBILITY})

        survey = Survey(
            answers=answers
        )

        questions = Questions(survey=survey)
        result: str = questions.what_is_your_favorite_activity()
        self.assertEqual(result, Text.FLEXIBILITY)

    def test_question_1_answer_4(self):
        answers: Dict = answers_dict.copy()
        answers.update({'Q1': Answer.STRENGTH})

        survey = Survey(
            answers=answers
        )
        questions = Questions(survey=survey)
        result: str = questions.what_is_your_favorite_activity()
        self.assertEqual(result, Text.STRENGTH_AND_NO_ACTIVITY)

    def test_question_1_answer_5(self):
        answers: Dict = answers_dict.copy()
        answers.update({'Q1': Answer.NO_ACTIVITY})

        survey = Survey(
            answers=answers
        )

        questions = Questions(survey=survey)
        result: str = questions.what_is_your_favorite_activity()
        self.assertEqual(result, Text.STRENGTH_AND_NO_ACTIVITY)


if __name__ == '__main__':
    unittest.main()

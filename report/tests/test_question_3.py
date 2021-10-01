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

    def test_question_3_answer_1(self):
        answers: Dict = answers_dict.copy()
        answers.update({'Q3': Answer.EARLY_MORNING})

        survey = Survey(
            answers=answers
        )

        questions = Questions(survey=survey)
        result: str = questions.when_do_you_like_to_exercise()
        self.assertEqual(result, Text.MORNING_AND_EVENING_AND_NIGHT)

    def test_question_3_answer_2(self):
        answers: Dict = answers_dict.copy()
        answers.update({'Q3': Answer.EVENING})

        survey = Survey(
            answers=answers
        )

        questions = Questions(survey=survey)
        result: str = questions.when_do_you_like_to_exercise()
        self.assertEqual(result, Text.MORNING_AND_EVENING_AND_NIGHT)

    def test_question_3_answer_3(self):
        answers: Dict = answers_dict.copy()
        answers.update({'Q3': Answer.NIGHT})

        survey = Survey(
            answers=answers
        )

        questions = Questions(survey=survey)
        result: str = questions.when_do_you_like_to_exercise()
        self.assertEqual(result, Text.MORNING_AND_EVENING_AND_NIGHT)

    def test_question_3_answer_4(self):
        answers: Dict = answers_dict.copy()
        answers.update({'Q3': Answer.DAY_TIME})

        survey = Survey(
            answers=answers
        )

        questions = Questions(survey=survey)
        result: str = questions.when_do_you_like_to_exercise()
        self.assertEqual(result, Text.DAY_TIME_AND_NEVER)

    def test_question_3_answer_5(self):
        answers: Dict = answers_dict.copy()
        answers.update({'Q3': Answer.NEVER})

        survey = Survey(
            answers=answers
        )

        questions = Questions(survey=survey)
        result: str = questions.when_do_you_like_to_exercise()
        self.assertEqual(result, Text.DAY_TIME_AND_NEVER)


if __name__ == '__main__':
    unittest.main()

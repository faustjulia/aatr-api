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

    def test_question_5_answer_1(self):
        answers: Dict = answers_dict.copy()
        answers['Q5']['choice'] = Answer.YES_TO_ACTIVITIES
        answers['Q5']['yes_choices'] = [Answer.HIKING, Answer.BIKING]
        survey = Survey(
            answers=answers
        )
        questions = Questions(survey=survey)

        result: str = questions.overall_I_like_activities()
        self.assertEqual(result, Text.YES_HIKING_BIKING)

    def test_question_5_answer_2(self):
        answers: Dict = answers_dict.copy()
        answers['Q5']['choice'] = Answer.YES_TO_ACTIVITIES
        answers['Q5']['yes_choices'] = [Answer.SWIMMING, Answer.PICNIC]
        survey = Survey(
            answers=answers
        )
        questions = Questions(survey=survey)

        result: str = questions.overall_I_like_activities()
        self.assertEqual(result, Text.YES_SWIMMING_PICNIC)

    def test_question_5_answer_3(self):
        answers: Dict = answers_dict.copy()
        answers['Q5']['choice'] = Answer.YES_TO_ACTIVITIES
        answers['Q5']['yes_choices'] = [Answer.SWIMMING, Answer.BIKING]
        survey = Survey(
            answers=answers
        )
        questions = Questions(survey=survey)

        result: str = questions.overall_I_like_activities()
        self.assertEqual(result, Text.YES_AND_ANY_OTHER_CASE)

    def test_question_5_answer_4(self):
        answers: Dict = answers_dict.copy()
        answers['Q5']['choice'] = Answer.YES_TO_ACTIVITIES
        answers['Q5']['yes_choices'] = [Answer.PICNIC, Answer.HIKING]
        survey = Survey(
            answers=answers
        )
        questions = Questions(survey=survey)

        result: str = questions.overall_I_like_activities()
        self.assertEqual(result, Text.YES_AND_ANY_OTHER_CASE)

    def test_question_5_answer_5(self):
        answers: Dict = answers_dict.copy()
        answers['Q5']['choice'] = Answer.YES_TO_ACTIVITIES
        answers['Q5']['yes_choices'] = [Answer.PICNIC, Answer.BIKING]
        survey = Survey(
            answers=answers
        )
        questions = Questions(survey=survey)

        result: str = questions.overall_I_like_activities()
        self.assertEqual(result, Text.YES_AND_ANY_OTHER_CASE)

    def test_question_5_answer_6(self):
        answers: Dict = answers_dict.copy()
        answers['Q5']['choice'] = Answer.YES_TO_ACTIVITIES
        answers['Q5']['yes_choices'] = [Answer.SWIMMING, Answer.HIKING]
        survey = Survey(
            answers=answers
        )
        questions = Questions(survey=survey)

        result: str = questions.overall_I_like_activities()
        self.assertEqual(result, Text.YES_AND_ANY_OTHER_CASE)


if __name__ == '__main__':
    unittest.main()

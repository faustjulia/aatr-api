import unittest
from typing import Dict, List

from report.answer import Answer
from report.questions import Questions
from report.survey import Survey
from report.tests.common.base import TestCommon
from report.text import Text

text = Text()


class TestOverallILikeActivities(TestCommon):

    def test_answer_yes_hiking_biking(self):
        answers: Dict = self.test_answers.copy()
        answers['Q5']['choice'] = Answer.YES_TO_ACTIVITIES
        answers['Q5']['yes_choices'] = [Answer.HIKING, Answer.BIKING]
        survey = Survey(
            answers=answers
        )
        questions = Questions(survey=survey)

        result: str = questions.overall_I_like_activities()
        self.assertEqual(result, text.YES_HIKING_BIKING)

    def test_answer_yes_swimming_picnic(self):
        answers: Dict = self.test_answers.copy()
        answers['Q5']['choice'] = Answer.YES_TO_ACTIVITIES
        answers['Q5']['yes_choices'] = [Answer.SWIMMING, Answer.PICNIC]
        survey = Survey(
            answers=answers
        )
        questions = Questions(survey=survey)

        result: str = questions.overall_I_like_activities()
        self.assertEqual(result, text.YES_SWIMMING_PICNIC)

    def test_answer_yes_swimming_biking(self):
        answers: Dict = self.test_answers.copy()
        answers['Q5']['choice'] = Answer.YES_TO_ACTIVITIES

        test_answers: List = [
            [Answer.SWIMMING, Answer.BIKING],
            [Answer.PICNIC, Answer.HIKING],
            [Answer.PICNIC, Answer.BIKING],
            [Answer.SWIMMING, Answer.HIKING]

        ]
        for answer in test_answers:
            answers['Q5']['yes_choices'] = answer

        survey = Survey(
            answers=answers
        )
        questions = Questions(survey=survey)

        result: str = questions.overall_I_like_activities()
        self.assertEqual(result, text.YES_AND_ANY_OTHER_CASE)

    def test_answer_no(self):
        answers: Dict = self.test_answers.copy()
        answers['Q5']['choice'] = Answer.NO_TO_ACTIVITIES
        answers['Q5']['yes_choices'] = None
        survey = Survey(
            answers=answers
        )
        questions = Questions(survey=survey)

        result: str = questions.overall_I_like_activities()
        self.assertEqual(result, text.I_DONT_LIKE_ACTIVITIES)

    def test_answer_I_dont_know(self):
        answers: Dict = self.test_answers.copy()
        answers['Q5']['choice'] = Answer.I_DONT_KNOW_TO_ACTIVITIES
        answers['Q5']['yes_choices'] = None
        survey = Survey(
            answers=answers
        )
        questions = Questions(survey=survey)

        result: str = questions.overall_I_like_activities()
        self.assertEqual(result, text.I_DONT_KNOW)


if __name__ == '__main__':
    unittest.main()

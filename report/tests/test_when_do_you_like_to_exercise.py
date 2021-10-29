import unittest
from typing import Dict

from report.answer import Answer
from report.questions import Questions
from report.survey import Survey
from report.tests.common.base import TestCommon
from report.text import Text


class TestWhenDoYouLikeToExercise(TestCommon):

    def test_answer_morning_evening_night(self):
        answers: Dict = self.test_answers.copy()
        answers.update(
            {'Q3': [Answer.EARLY_MORNING, Answer.EVENING, Answer.NIGHT]})

        survey = Survey(
            answers=answers
        )

        questions = Questions(survey=survey)
        result: str = questions.when_do_you_like_to_exercise()
        self.assertEqual(result, Text.MORNING_AND_EVENING_AND_NIGHT)

    def test_answer_evening(self):
        answers: Dict = self.test_answers.copy()
        answers.update({'Q3': Answer.EVENING})

        survey = Survey(
            answers=answers
        )

        questions = Questions(survey=survey)
        result: str = questions.when_do_you_like_to_exercise()
        self.assertEqual(result, Text.MORNING_OR_EVENING_OR_NIGHT)

    def test_answer_morning(self):
        answers: Dict = self.test_answers.copy()
        answers.update({'Q3': Answer.EARLY_MORNING})

        survey = Survey(
            answers=answers
        )

        questions = Questions(survey=survey)
        result: str = questions.when_do_you_like_to_exercise()
        self.assertEqual(result, Text.MORNING_OR_EVENING_OR_NIGHT)

    def test_answer_night(self):
        answers: Dict = self.test_answers.copy()
        answers.update({'Q3': Answer.NIGHT})

        survey = Survey(
            answers=answers
        )

        questions = Questions(survey=survey)
        result: str = questions.when_do_you_like_to_exercise()
        self.assertEqual(result, Text.MORNING_OR_EVENING_OR_NIGHT)

    def test_answer_morning_night(self):
        answers: Dict = self.test_answers.copy()
        answers.update({'Q3': [Answer.NIGHT, Answer.EARLY_MORNING]})

        survey = Survey(
            answers=answers
        )

        questions = Questions(survey=survey)
        result: str = questions.when_do_you_like_to_exercise()
        self.assertEqual(result, Text.MORNING_OR_EVENING_OR_NIGHT)

    def test_answer_evening_night(self):
        answers: Dict = self.test_answers.copy()
        answers.update({'Q3': [Answer.NIGHT, Answer.EVENING]})

        survey = Survey(
            answers=answers
        )

        questions = Questions(survey=survey)
        result: str = questions.when_do_you_like_to_exercise()
        self.assertEqual(result, Text.MORNING_OR_EVENING_OR_NIGHT)

    def test_answer_morning_evening(self):
        answers: Dict = self.test_answers.copy()
        answers.update({'Q3': [Answer.EVENING, Answer.EARLY_MORNING]})

        survey = Survey(
            answers=answers
        )

        questions = Questions(survey=survey)
        result: str = questions.when_do_you_like_to_exercise()
        self.assertEqual(result, Text.MORNING_OR_EVENING_OR_NIGHT)

    def test_answer_morning_daytime(self):
        answers: Dict = self.test_answers.copy()
        answers.update({'Q3': [Answer.DAY_TIME, Answer.EARLY_MORNING]})

        survey = Survey(
            answers=answers
        )

        questions = Questions(survey=survey)
        result: str = questions.when_do_you_like_to_exercise()
        self.assertEqual(result, Text.DAY_TIME_AND_EARLY_MORNING)

    def test_answer_never(self):
        answers: Dict = self.test_answers.copy()
        answers.update({'Q3': [Answer.NEVER]})

        survey = Survey(
            answers=answers
        )

        questions = Questions(survey=survey)
        result: str = questions.when_do_you_like_to_exercise()
        self.assertEqual(result, Text.ANY_OTHER_CASE)


if __name__ == '__main__':
    unittest.main()

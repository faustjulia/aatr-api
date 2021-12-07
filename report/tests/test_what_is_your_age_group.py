import unittest
from typing import Dict

from report.questions import Questions
from report.survey import Survey
from report.tests.common.base import TestCommon
from report.text import Text

text = Text()


class TestWhatIsYourAgeGroup(TestCommon):

    def test_birthdate_young_adult(self):
        answers: Dict = self.test_answers.copy()
        answers['Q4'] = '1998-03-11'

        survey = Survey(
            answers=answers
        )
        questions = Questions(survey=survey)

        result: str = questions.what_is_your_age_group()
        self.assertEqual(
            result,
            text.young_adult(age=23)
        )

    def test_birthdate_middle_age(self):
        answers: Dict = self.test_answers.copy()
        answers['Q4'] = '1995-02-01'

        survey = Survey(
            answers=answers
        )
        questions = Questions(survey=survey)

        result: str = questions.what_is_your_age_group()
        self.assertEqual(
            result,
            text.middle_age(age=26)
        )

    def test_birthdate_old_adulthood(self):
        answers: Dict = self.test_answers.copy()
        answers['Q4'] = '1950-03-11'

        survey = Survey(
            answers=answers
        )
        questions = Questions(survey=survey)

        result: str = questions.what_is_your_age_group()
        self.assertEqual(
            result,
            text.old_adulthood(age=71)
        )

    def test_age_young_adult(self):
        answers: Dict = self.test_answers.copy()
        answers['Q4'] = 23

        survey = Survey(
            answers=answers
        )
        questions = Questions(survey=survey)

        result: str = questions.what_is_your_age_group()
        self.assertEqual(
            result,
            text.young_adult(age=23)
        )

    def test_age_middle_age(self):
        answers: Dict = self.test_answers.copy()
        answers['Q4'] = 26

        survey = Survey(
            answers=answers
        )
        questions = Questions(survey=survey)

        result: str = questions.what_is_your_age_group()
        self.assertEqual(
            result,
            text.middle_age(age=26)
        )

    def test_age_old_adulthood(self):
        answers: Dict = self.test_answers.copy()
        answers['Q4'] = 71

        survey = Survey(
            answers=answers
        )
        questions = Questions(survey=survey)

        result: str = questions.what_is_your_age_group()
        self.assertEqual(
            result,
            text.old_adulthood(age=71)
        )


if __name__ == '__main__':
    unittest.main()

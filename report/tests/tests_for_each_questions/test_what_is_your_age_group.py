import unittest
from typing import Dict, List

from report.questions import Questions
from report.survey import Survey
from report.tests.common.base import TestCommon
from report.text import Text

text = Text()


class TestWhatIsYourAgeGroup(TestCommon):

    def test_young_adult(self):
        answers: Dict = self.test_answers.copy()
        test_answers: List[str, int] = ['1998-03-11', 23]
        for answer in test_answers:
            answers['Q4'] = answer

        survey = Survey(
            answers=answers
        )
        questions = Questions(survey=survey)

        result: str = questions.what_is_your_age_group()
        self.assertEqual(
            result,
            text.young_adult(age=23)
        )

    def test_middle_age(self):
        answers: Dict = self.test_answers.copy()
        test_answers: List[str, int] = ['1995-02-01', 26]
        for answer in test_answers:
            answers['Q4'] = answer

            survey = Survey(
                answers=answers
            )
            questions = Questions(survey=survey)

            result: str = questions.what_is_your_age_group()
            self.assertEqual(
                result,
                text.middle_age(age=26)
            )

    def test_old_adulthood(self):
        answers: Dict = self.test_answers.copy()
        test_answers: List[str, int] = ['1950-03-11', 71]
        for answer in test_answers:
            answers['Q4'] = answer

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

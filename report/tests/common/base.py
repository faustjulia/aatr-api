import unittest
from typing import Dict

from report.answer import Answer


class TestCommon(unittest.TestCase):
    test_answers: Dict = {
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

import datetime
from typing import List

from report.answer import Answer
from report.survey import Survey
from report.text import Text

text = Text()


def get_age(born) -> int:
    today = datetime.date.today()
    return int(today.year - born.year - (
        (today.month, today.day) < (born.month, born.day)))


class Questions:

    def __init__(self, survey: Survey):
        self.survey = survey

    def what_is_your_favorite_activity(self) -> str:

        self.survey.Q1.lower()

        if self.survey.Q1 == Answer.AEROBICS:
            return text.AEROBICS
        elif self.survey.Q1 == Answer.NO_ACTIVITY:
            return text.NO_ACTIVITY
        elif self.survey.Q1 == Answer.STRENGTH:
            return text.STRENGTH
        else:
            return text.FLEXIBILITY_AND_BALANCE

    def what_is_the_main_goal_of_exercising(self) -> str:

        if (
            self.survey.Q2 == Answer.HAVE_A_GOOD_TIME or
            self.survey.Q2 == Answer.BE_HEALTHY
        ):
            return text.HAVE_A_GOOD_TIME_OR_BE_HEALTHY
        elif (
            self.survey.Q2 == Answer.LOOSE_WEIGHT or
            Answer.I_DONT_EXERCISE
        ):
            return text.LOOSE_WEIGHT_OR_NO_EXERCISE

    def when_do_you_like_to_exercise(self) -> str:

        if Answer.NEVER in self.survey.Q3:
            return text.ANY_OTHER_CASE

        if (
            Answer.EVENING in self.survey.Q3 and
            Answer.NIGHT in self.survey.Q3 and
            Answer.EARLY_MORNING in self.survey.Q3
        ):
            return text.MORNING_AND_EVENING_AND_NIGHT

        elif (
            Answer.DAY_TIME in self.survey.Q3 and
            Answer.EARLY_MORNING in self.survey.Q3
        ):
            return Text.DAY_TIME_AND_EARLY_MORNING

        elif (
            Answer.EVENING in self.survey.Q3 or
            Answer.NIGHT in self.survey.Q3 or
            Answer.EARLY_MORNING in self.survey.Q3
        ):
            return text.MORNING_OR_EVENING_OR_NIGHT

        else:
            return text.ANY_OTHER_CASE

    def what_is_your_age_group(self) -> str:

        if '-' in str(self.survey.Q4):
            year, month, day = map(int, self.survey.Q4.split('-'))
            date1 = datetime.date(year, month, day)
            AGE: int = get_age(date1)
        else:
            AGE: int = int(self.survey.Q4)

        if AGE >= 60:
            return text.old_adulthood(age=AGE)
        elif 25 < AGE < 60:
            return text.middle_age(age=AGE)
        else:
            return text.young_adult(age=AGE)

    def overall_I_like_activities(self) -> str:

        if self.survey.Q5['choice'] == Answer.NO_TO_ACTIVITIES:
            return text.I_DONT_LIKE_ACTIVITIES

        elif self.survey.Q5['choice'] == Answer.I_DONT_KNOW_TO_ACTIVITIES:
            return text.I_DONT_KNOW

        elif (
            self.survey.Q5['choice'] == Answer.YES_TO_ACTIVITIES and
            Answer.HIKING in self.survey.Q5['yes_choices'] and
            Answer.BIKING in self.survey.Q5['yes_choices']
        ):
            return text.YES_HIKING_BIKING

        elif (
            self.survey.Q5['choice'] == Answer.YES_TO_ACTIVITIES and
            Answer.SWIMMING in self.survey.Q5['yes_choices'] and
            Answer.PICNIC in self.survey.Q5['yes_choices']
        ):
            return text.YES_SWIMMING_PICNIC

        else:
            return text.YES_AND_ANY_OTHER_CASE

    def all(self) -> List[str]:
        return [
            self.what_is_your_favorite_activity(),
            self.what_is_the_main_goal_of_exercising(),
            self.when_do_you_like_to_exercise(),
            self.what_is_your_age_group(),
            self.overall_I_like_activities(),
        ]

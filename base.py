from typing import Dict, List
from texts import Text, Answer
import datetime

def get_age(born) -> int:
    today = datetime.date.today()
    return int(today.year - born.year - ((today.month, today.day) < (born.month, born.day)))

#  Q1: what type of activity you enjoy the most: (aerobics, balance, flexibility, strength, no activity)
#  Q2: What is the main goal of you exercising? (Have a good time, be healthy, loose weight, I don’t exercise)
#  Q3: When do you prefer to exercise? Early morning, during the day, Early evening, late at night, I prefer not to exercise
#  Q4: What age group do you belong to? (Old adulthood, Middle age, Young adult)
# Q5: overall, I enjoy doing activities during my vacation. Yes: what type? swimming in the lake, hiking up the mountain, going dirt biking, or having a picnic with the sunset?

text = Text()

report_text = ''

answers: Dict = {
    # 'Q1': Answer.NO_ACTIVITY,
    # 'Q2': Answer.HAVE_A_GOOD_TIME,
    # 'Q3': [Answer.EVENING, Answer.NIGHT, Answer.EARLY_MORNING],
    # 'Q4': Answer.AGE_OR_BIRTHDATE,
    'Q5': [Answer.YES, Answer.SWIMMING, Answer.PICNIC]
}

if answers['Q5'] == Answer.NO:
    report_text += text.NO

elif answers['Q5'] == Answer.I_DONT_KNOW:
    report_text += text.I_DONT_KNOW

elif (
        Answer.YES in answers['Q5'] and
        Answer.HIKING in answers['Q5'] and
        Answer.BIKING in answers['Q5']
):
    report_text += text.YES_HIKING_BIKING

elif (
        Answer.YES in answers['Q5'] and
        Answer.SWIMMING in answers['Q5'] and
        Answer.PICNIC in answers['Q5']
):
    report_text += text.YES_SWIMMING_PICNIC

else:
    report_text += text.YES_AND_ANY_OTHER_CASE

print(report_text)


# # Question 1
#
# if answers['Q1'] == Answer.AEROBICS:
#     report_text += text.AEROBICS
# elif answers['Q1'] == Answer.BALANCE:
#     report_text += text.BALANCE
# elif answers['Q1'] == Answer.FLEXIBILITY:
#     report_text += text.FLEXIBILITY
# else:
#     report_text += text.STRENGTH_AND_NO_ACTIVITY
#
# # Question 2
# if (
#     answers['Q2'] == Answer.HAVE_A_GOOD_TIME or
#     answers['Q2'] == Answer.BE_HEALTHY
# ):
#     report_text += text.HAVE_A_GOOD_TIME_OR_BE_HEALTHY
# elif (
#     answers['Q2'] == Answer.LOOSE_WEIGHT or
#     Answer.I_DONT_EXERCISE
# ):
#     report_text += text.LOOSE_WEIGHT_OR_NO_EXERCISE
#
# # # Question 3
# if (
#         Answer.EVENING in answers['Q3'] and
#         Answer.NIGHT in answers['Q3'] and
#         Answer.EARLY_MORNING in answers['Q3']
# ):
#     report_text +=  text.MORNING_AND_EVENING_AND_NIGHT
#
# elif (
#         Answer.DAY_TIME in answers['Q3'] and
#         Answer.NEVER in answers['Q3']
# ):
#     report_text += Text.DAY_TIME_AND_NEVER
#
# elif (
#         Answer.EVENING in answers['Q3'] or
#         Answer.NIGHT in answers['Q3'] or
#         Answer.EARLY_MORNING in answers['Q3']
# ):
#     report_text += text.MORNING_OR_EVENING_OR_NIGHT
#
# else:
#     report_text += text.ANY_OTHER_CASE

# print(report_text)

# # Question 4
#
# if '-' in Answer.AGE_OR_BIRTHDATE:
#     year, month, day = map(int, Answer.AGE_OR_BIRTHDATE.split('-'))
#     date1 = datetime.date(year, month, day)
#     AGE: int = get_age(date1)
# else:
#     AGE: int = int(Answer.AGE_OR_BIRTHDATE)
#
# report_text: str = ''
#
# if AGE >= 60:
#     report_text += text.old_adulthood(age=AGE)
# elif 25 < AGE < 60:
#     report_text += text.middle_age(age=AGE)
# else:
#     report_text += text.young_adult(age=AGE)
#
# print(report_text)





from typing import Dict, List
from texts import Text
import datetime

def get_age(born):
    today = datetime.date.today()
    return today.year - born.year - ((today.month, today.day) < (born.month, born.day))

#  Q1: what type of activity you enjoy the most: (aerobics, balance, flexibility, strength, no activity)
#  Q2: What is the main goal of you exercising? (Have a good time, be healthy, loose weight, I don’t exercise)
#  Q3: When do you prefer to exercise? Early morning, during the day, Early evening, late at night, I prefer not to exercise
#  Q4: Calculate optimal heart rate during exercise (Input either age, or birthdate)

AEROBICS: str = 'Aerobics'
BALANCE: str = 'Balance'
FLEXIBILITY: str = 'Flexibility'
STRENGTH: str = 'Strength'
NO_ACTIVITY: str = 'No Activity'

HAVE_A_GOOD_TIME: str = 'Have a good time'
LOOSE_WEIGHT: str = 'Loose Weight'
BE_HEALTHY: str = 'Be healthy'
I_DONT_EXERCISE:str = 'I don\'t exercise'

EARLY_MORNING:str = 'Early morning'
DAY_TIME:str = 'During the day'
EVENING:str = 'Early evening'
NIGHT:str = 'Late at night'
NEVER:str = 'I prefer not to exercise'



# Question 4


AGE_OR_BIRTHDATE: str = input('Enter your birthday in YYYY-MM-DD format or your DOB: ')

if '-' in AGE_OR_BIRTHDATE:
    year, month, day = map(int, AGE_OR_BIRTHDATE.split('-'))
    date1 = datetime.date(year, month, day)
    AGE = get_age(date1)
    print(AGE)

else:
    AGE = AGE_OR_BIRTHDATE
    print('Person\'s age is', AGE)


answers: Dict = {
    # 'Q1': NO_ACTIVITY,
    # 'Q2': HAVE_A_GOOD_TIME,
    # 'Q3': [EVENING, NIGHT, EARLY_MORNING],
    'Q4': AGE
}

report_text: str = ''

if answers['Q4'] >= 60:
    report_text += Text.OLD_ADULTHOOD
elif 25 < answers['Q4'] < 60:
    report_text += Text.MIDDLE_AGE
else:
    report_text += Text.YOUNG_ADULT


# Question 1

# if answers['Q1'] == AEROBICS:
#     report_text += Text.AEROBICS
# elif answers['Q1'] == BALANCE:
#     report_text += Text.BALANCE
# elif answers['Q1'] == FLEXIBILITY:
#     report_text += Text.FLEXIBILITY
# else:
#     report_text += Text.STRENGTH_AND_NO_ACTIVITY

# Question 2
# if answers['Q2'] == HAVE_A_GOOD_TIME or answers['Q2'] == BE_HEALTHY:
#     report_text += Text.HAVE_A_GOOD_TIME_AND_BE_HEALTHY
# elif answers['Q2'] == LOOSE_WEIGHT or I_DONT_EXERCISE:
#     report_text += Text.LOOSE_WEIGHT_AND_NO_EXERCISE

# # Question 3
# if (
#         EVENING in answers['Q3']
#         and NIGHT in answers['Q3']
#         and EARLY_MORNING in answers['Q3']
# ):
#     report_text +=  Text.MORNING_AND_EVENING_AND_NIGHT
#
# elif (
#         DAY_TIME in answers['Q3']
#         and NEVER in answers['Q3']
# ):
#     report_text += Text.DAY_TIME_AND_NEVER
#
# elif (
#         EVENING in answers['Q3']
#         and NIGHT in answers['Q3']
#         or EARLY_MORNING in answers['Q3']
# ):
#     report_text += Text.MORNING_AND_EVENING_OR_NIGHT
#
# else:
#     report_text += Text.ANY_OTHER_CASE
#
# print(report_text)





# from typing import Dict, List
# # from texts import Text
# #
# #
# # #  Q1: what type of activity you enjoy the most: (aerobics, balance, flexibility, strength, no activity)
# # #  Q2: What is the main goal of you exercising? (Have a good time, be healthy, loose weight, I don’t exercise)
# # #  Q3: How many days a week you spend doing outdoor activities? 1-3, 3-5, 5-7, none
# # #  Q4: what’s your height? Inch and sm
# # #  Q5: overall, I enjoy doing activities during my vacation. Yes: what type? swimming in the lake, hiking up the mountain, going dirt biking, or having a picnic with the sunset?
# #
# # class Survey:
# #
# #     def __init__(self,
# #                  Q1_answer: str
# #                  ):
# #
# #         self.Q1_answer = Q1_answer
# #
# #
# #     def question(self,
# #                  question: str) -> str:
# #
# #         report:str = ''
# #
# #         AEROBICS: str = 'Aerobics'
# #         BALANCE: str = 'Balance'
# #         FLEXIBILITY: str = 'Flexibility'
# #         STRENGTH: str = 'Strength'
# #         NO_ACTIVITY: str = 'No Activity'
# #
# #
# #         if question == "What type of activity you enjoy the most?":
# #
# #             answers: Dict[str, str] = {
# #                 AEROBICS: Text.AEROBICS,
# #                 BALANCE: Text.BALANCE,
# #                 FLEXIBILITY: Text.FLEXIBILITY,
# #                 STRENGTH: Text.STRENGTH_AND_NO_ACTIVITY,
# #                 NO_ACTIVITY: Text.STRENGTH_AND_NO_ACTIVITY
# #             }
# #
# #             report += answers[self.Q1_answer]
# #
# #         elif question == 'What is the main goal of you exercising?':
# #
# #             answers: Dict[str, str] = {
# #                 'Have a good time': Text.AEROBICS,
# #                 # 'Be healthy': Text.BALANCE,
# #                 # 'Loose weight': Text.FLEXIBILITY,
# #                 # 'I don\'t exercise': Text.STRENGTH_AND_NO_ACTIVITY,
# #             }
# #
# #             print(answers[0])
# #             print(self.Q1_answer)
# #
# #             if self.Q1_answer == answers[0] or answers[2]:
# #                 report += answers[self.Q1_answer]
# #
# #         return report
# #
# #
# #
# #
# #
# #         # return report
# #
# # survey = Survey(Q1_answer='Loose weight').question(question='What is the main goal of you exercising?')
# # print(survey)
# #
# #         # try:
# #         #     return topics[topic]
# #         # except KeyError:
# #         #     return f'Sorry, I don\'t know what you\'re talking about'
# #
# #         # questions: Dict[str, List[str]] = {
# #         #     'Q1': [
# #         #         'No activity',
# #         #         'Aerobics',
# #         #         'Balance',
# #         #         'Flexibility',
# #         #         'Strength'
# #         #     ]
# #         # }
# #         #
# #         #
# #         # answers: Dict[str, str] = {
# #         #     questions['Q1'][0]:'Lorem ipsum 1. Question - ANSWER_1 '
# #         #                        'dolor sit amet, consectetur adipiscing elit.',
# #         #     questions['Q1'][1]: 'Lorem ipsum 1. Question - ANSWER_2 '
# #         #                         'Ut et augue id leo egestas interdum in eu lectus.',
# #         #     questions['Q1'][2]: 'Lorem ipsum 1. Question - ANSWER_3 '
# #         #                         'Nullam auctor odio vehicula',
# #         #     questions['Q1'][3]: 'Lorem ipsum 1. Question - ANSWER_4 '
# #         #                         'posuere elit in, ullamcorper lectus',
# #         #     questions['Q1'][4]: 'Lorem ipsum 1. Question - ANSWER_5 '
# #         #                         'Mauris pharetra dapibus congue.'
# #         # }
# #
# #         # if self.Q1_answer == questions['Q1'][0]:
# #         #     return 'Lorem ipsum 1. Question - ANSWER_1 dolor sit amet, consectetur adipiscing elit.'
# #         # elif self.Q1_answer == questions['Q1'][1]:
# #         #     return 'Lorem ipsum 1. Question - ANSWER_2 Ut et augue id leo egestas interdum in eu lectus.'
# #         # elif self.Q1_answer == questions['Q1'][2]:
# #         #     return 'Lorem ipsum 1. Question - ANSWER_3 Nullam auctor odio vehicula'
# #         # elif self.Q1_answer == questions['Q1'][3]:
# #         #     return 'Lorem ipsum 1. Question - ANSWER_4 posuere elit in, ullamcorper lectus'
# #         # elif self.Q1_answer == questions['Q1'][4]:
# #         #     return 'Lorem ipsum 1. Question - ANSWER_5 Mauris pharetra dapibus congue.'
# #

import datetime

birthday_entry = input('Enter a date in YYYY-MM-DD format')
year, month, day = map(int, birthday_entry.split('-'))
date1 = datetime.date(year, month, day)


def from_dob_to_age(born):
    today = datetime.date.today()
    return today.year - born.year - ((today.month, today.day) < (born.month, born.day))

age = from_dob_to_age(date1)
print(age)


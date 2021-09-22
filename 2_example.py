from typing import Dict, List
#
#  Q1: what type of activity you enjoy the most: (aerobics, balance, flexibility, strength, no activity)
#  Q2: What is the main goal of you exercising? (Have a good time, be healthy, loose weight, I don’t exercise)
#  Q3: How many days a week you spend doing outdoor activities? 1-3, 3-5, 5-7, none
#  Q4: what’s your height? Inch and sm
#  Q5: overall, I enjoy doing activities during my vacation. Yes: what type? swimming in the lake, hiking up the mountain, going dirt biking, or having a picnic with the sunset?

class Survey:

    def __init__(self,
                 Q1_answer: str,
                 # Q1_question: str = "What type of activity you enjoy the most?"
                 ):

        self.Q1_answer = Q1_answer
        # self.Q1_question = Q1_question

    def question(self):

        questions: Dict[str, List[str]] = {
            'Q1': [
                'No activity',
                'Aerobics',
                'Balance',
                'Flexibility',
                'Strength'
            ]
        }


        answers: Dict = {
            questions['Q1'][0]:'Lorem ipsum 1. Question - ANSWER_1 '
                               'dolor sit amet, consectetur adipiscing elit.',
            questions['Q1'][1]: 'Lorem ipsum 1. Question - ANSWER_2 '
                                'Ut et augue id leo egestas interdum in eu lectus.',
            questions['Q1'][2]: 'Lorem ipsum 1. Question - ANSWER_3 '
                                'Nullam auctor odio vehicula',
            questions['Q1'][3]: 'Lorem ipsum 1. Question - ANSWER_4 '
                                'posuere elit in, ullamcorper lectus',
            questions['Q1'][4]: 'Lorem ipsum 1. Question - ANSWER_5 '
                                'Mauris pharetra dapibus congue.'
        }

        # try:
        #     return topics[topic]
        # except KeyError:
        #     return f'Sorry, I don\'t know what you\'re talking about'

        # if self.Q1_answer == questions['Q1'][0]:
        #     return 'Lorem ipsum 1. Question - ANSWER_1 dolor sit amet, consectetur adipiscing elit.'
        # elif self.Q1_answer == questions['Q1'][1]:
        #     return 'Lorem ipsum 1. Question - ANSWER_2 Ut et augue id leo egestas interdum in eu lectus.'
        # elif self.Q1_answer == questions['Q1'][2]:
        #     return 'Lorem ipsum 1. Question - ANSWER_3 Nullam auctor odio vehicula'
        # elif self.Q1_answer == questions['Q1'][3]:
        #     return 'Lorem ipsum 1. Question - ANSWER_4 posuere elit in, ullamcorper lectus'
        # elif self.Q1_answer == questions['Q1'][4]:
        #     return 'Lorem ipsum 1. Question - ANSWER_5 Mauris pharetra dapibus congue.'


survey = Survey(Q1_answer='No Activity').question()
print(survey)




# class Questions():
#
#     def __init__(self,
#                  question: str,
#                  answer: str
#                  ):
#
#         self.question = question
#         self.answer = answer
#
#
#
#     def questionaire(self, key: int) -> str:
#
#         if self.question == "What type of activity you enjoy the most?":
#
#             answers: Dict[int, str] = {
#                 1: 'No activity',
#                 2: 'Aerobics',
#                 3: 'Balance',
#                 4: 'Flexibility',
#                 5: 'Strength'
#             }
#
#
#
#         else:
#             print('2')
#             # breakpoint()
#             return f'Sorry, this is not the question asked'
#
#
#
#         try:
#             return answers[key]
#         except KeyError:
#             return f'Sorry, I don\'t know what you\'re talking about'
#
#
#
#     def question(self):
#
#         questions: Dict[str, List[str]] = {
#             'What type of activity you enjoy the most?': [
#                 'No activity',
#                 'Aerobics',
#                 'Balance',
#                 'Flexibility',
#                 'Strength'
#             ]
#         }
#
#         # breakpoint()
#
#         for answer in questions.values():
#             return questions[answer]
#
#
# Q1 = Questions(question='smtj', answer='1').questionaire(3)
# print(Q1)
#
# Q2 = Questions(question='smtj', answer='1').question()
# print(Q2)
from typing import Dict, List
#
#  Q1: what type of activity you enjoy the most: (aerobics, balance, flexibility, strength, no activity)
#  Q2: What is the main goal of you exercising? (Have a good time, be healthy, loose weight, I don’t exercise)
#  Q3: How many days a week you spend doing outdoor activities? 1-3, 3-5, 5-7, none
#  Q4: what’s your height? Inch and sm
#  Q5: overall, I enjoy doing activities during my vacation. Yes: what type? swimming in the lake, hiking up the mountain, going dirt biking, or having a picnic with the sunset?

class Questions():

    def __init__(self,
                 question: str,
                 answer: str
                 ):

        self.question = question
        self.answer = answer


    def questionaire(self, key: int) -> str:

        if self.question == "What type of activity you enjoy the most?":

            answers: Dict[int, str] = {
                1: 'No activity',
                2: 'Aerobics',
                3: 'Balance',
                4: 'Flexibility',
                5: 'Strength'
            }

        else:
            return f'Sorry, this is not the question asked'

        try:
            return answers[key]
        except KeyError:
            return f'Sorry, I don\'t know what you\'re talking about'


    def question(self):

        questions: Dict[str, List[str]] = {
            'What type of activity you enjoy the most?': [
                'No activity',
                'Aerobics',
                'Balance',
                'Flexibility',
                'Strength'
            ]
        }

        for answer in questions.values():
            return questions[answer]
from typing import Dict


class Survey:

    def __init__(self,
                 answers: Dict
                 ):
        self.Q1 = answers['Q1']
        self.Q2 = answers['Q2']
        self.Q3 = answers['Q3']
        self.Q4 = answers['Q4']
        self.Q5 = answers['Q5']

    def __str__(self):
        return (
            f'Q1: {self.Q1} \n'
            f'Q2: {self.Q2} \n'
            f'Q3: {self.Q3} \n'
            f'Q4: {self.Q4} \n'
            f'Q5: {self.Q5} \n'
        )

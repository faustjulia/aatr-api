from report.survey import Survey
from report.questions import Questions


class Report:

    def __init__(self,
                 survey: Survey):

        self.survey = survey
        self.questions = Questions(survey=survey)

    def generate(self) -> str:
        report_text = ''

        for question_report_text in self.questions.all():
            report_text += question_report_text

        return report_text
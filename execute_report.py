
from report import Report, Survey, Answer

survey = Survey(
    answers = {
        'Q1': Answer.AEROBICS,
        'Q2': Answer.HAVE_A_GOOD_TIME,
        'Q3': [Answer.DAY_TIME, Answer.NEVER],
        'Q4': Answer.AGE_OR_BIRTHDATE,
        'Q5': {'choice': Answer.YES_TO_ACTIVITIES,
               'yes_choices': [
                   Answer.HIKING,
                   Answer.BIKING
               ]
        }
}
)

report = Report(
    survey = survey
)

report_text: str = report.generate()

print(report_text)



""" Jobscan Replica """


" Step 1: Copy and paste the job posting into the triple quotes below "

job_posting = """



"""


" Step 2: Remove punctuation from job posting "

job_posting_list = job_posting.split()  # Creates a list of words in the job description

clean_job_posting = [  # Remove punctuation from list of words in job description
    word.replace('•', "")
        .replace(",", "")
        .replace("""""", "")
        .replace("-", "")
        .replace("'", "")
        .replace("''", "")
        .replace(":", "")
        .replace(";", "")
        .replace("*", "")
        .replace("!", "")
        .replace("&", "")
        .replace("/n", "")
        .replace("/", "")
        .replace("?", "")
        .replace("(", "")
        .replace(")", "")
    for line in job_posting_list for word in line.lower().split()
    ]

job_count = dict()
for i in clean_job_posting:
    job_count[i] = job_count.get(i, 0) + 1


" Step 3: Remove common filler words in job posting "
# Feel free to add additional words to the list below that appear frequently in job posts (e.g. task, qualification, etc.)

common_job_words = [

    'a',
    'ability',
    'about',
    'added',
    'against',
    'an',
    'and',
    'any'
    'are',
    'as',
    'assist',
    'assisting',
    'at',

    'be',
    'both',
    'but',
    'by',

    'can',

    'demonstrate',
    'demonstrated',
    'duties'

    'employee',
    'every',
    'existing',
    'experience',

    'following',
    'for',
    'from',

    'gpa',

    'have',

    'in',
    'including'
    'identify',
    'into',
    'is',
    'it',

    'make',
    'members',
    'more',
    'must',

    'not',

    'obtain',
    'of',
    'on',
    'opportunity',
    'or',
    'other',
    'our',

    'preferred',

    'qualifications',

    'reach',
    'require',
    'required',

    'skill',
    'skills',
    'strong',
    'such',
    'support',
    'supporting',

    'that',
    'the',
    'their',
    'this',
    'to',

    'upon',
    'us',
    'use',
    'using',

    'we',
    'will',
    'with',
    'work',
    'working',

    'you',
    'your',
    ]


" Step 4: Show top keywords in the job posting and count their frequency "

for key in list(job_count.keys()):
    if key in common_job_words:
        del job_count[key]

job_keywords_count = sorted(job_count.items(), key=lambda x: x[1], reverse=True)
print(job_keywords_count)





" Step 5: Copy your resume below within the triple quotes "

resume = """



"""


" Step 6: Remove punctuation from resume "

resume_list = resume.split()  # Creates a list of words in your resume
clean_resume = [  # Remove punctuation from resume
    word.replace(",", "")
        .replace("""""", "")
        .replace("-", "")
        .replace("'", "")
        .replace("''", "")
        .replace(":", "")
        .replace(";", "")
        .replace("*", "")
        .replace("!", "")
        .replace("&", "")
        .replace("/n", "")
        .replace("/", "")
        .replace("?", "")
        .replace("(", "")
        .replace(")", "")
        .replace("•", "")
    for line in resume_list for word in line.lower().split()
    ]

resume_count = dict()
for i in clean_resume:
    resume_count[i] = resume_count.get(i, 0) + 1


" Step 7: Remove common filler words in resume "
# Feel free to add words to the list that appear frequently in your resume (e.g. cities you have worked in, your name, etc.)

common_resume_words = [
    '2014',
    '2015',
    '2016',
    '2017',
    '2018',
    '2019',
    '2020',
    '2021',
    '2022',

    'a',
    'an',
    'and',
    'as',

    'be',
    'bloomington',

    'dc',
    'december',

    'every',
    'existing',
    'experience',

    'fang',
    'from',
    'for',

    'gpa',

    'have',

    'in',
    'into',
    'is',
    'it',

    'may',

    'obtain',
    'of',
    'on',
    'opportunity',
    'or',
    'our',

    'portland',

    'spea',
    'strong',
    'support',
    'supporting',

    'that',
    'the',
    'their',
    'to',

    'university',
    'us',
    'use',

    'washington',
    'we',
    'will',
    'work',
    'with',

    'you',
    'your',

    ]

for key in list(resume_count.keys()):
    if key in common_resume_words:
        del resume_count[key]


" Step 8: Show top keywords in your resume and count their frequency "

resume_keywords_count = sorted(resume_count.items(), key=lambda x: x[1], reverse=True)
print(resume_keywords_count)


" Step 9: Identify key words in job posting that are not in your resume "

missing = {k: v for k, v in job_count.items() if k not in resume_count}
missing_keywords = sorted(missing.items(), key=lambda x: x[1], reverse=True)
print(missing_keywords)

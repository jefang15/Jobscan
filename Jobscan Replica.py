
""" Jobscan Replica """


"""
Many companies use an online Applicant Tracking System (ATS) to quickly identify top candidates among a large pool 
of applicants. Generally, an ATS does this by ranking applicants by keywords and filters. You may be a qualified 
candidate, but you may not be using the correct or enough keywords to make it past the computer screening. This is 
why you should tailor your resume for each job. 

Jobscan (jobscan.co) helps achieve this tailoring by identifying specific keywords deemed important for a job posting 
in question. However, the website has limited number of free "scans," so this program works to replicate the work of 
JobScan.
"""


" Job Description "


# Step 1: Copy and paste the job description below within the triple quotes.
job_description = """

Minimum qualifications:
Master's degree in Electrical Engineering, Operations Research, Industrial Engineering, Economics, or equivalent practical experience.
2 years of experience as an Energy Analyst or equivalent experience.
Experience with Python/R software and database languages (e.g., SQL).
Experience with research within the energy domain.
Preferred qualifications:
PhD in Electrical Engineering, Operations Research, Industrial Engineering, Economics, or a related field.
4 years of experience working as an energy analyst, trader, or system operator and applying advanced analytics to energy systems’ planning, controlling, and learning problems within universities, national labs, electric utility companies, etc.
Experience designing performance based energy systems optimization and control algorithms.
Experience designing and building statistical forecasting models.
Excellent problem-framing, problem-solving, and project management skills.
Excellent customer service and team collaboration skills.
About the job

At Google, data drives all of our decision-making. Quantitative Analysts work all across the organization to help shape Google's business and technical strategies by processing, analyzing and interpreting huge data sets. Using analytical excellence and statistical methods, you mine through data to identify opportunities for Google and our clients to operate more efficiently, from enhancing advertising efficacy to network infrastructure optimization to studying user behavior. As an analyst, you do more than just crunch the numbers. You work with Engineers, Product Managers, Sales Associates and Marketing teams to adjust Google's practices according to your findings. Identifying the problem is only half the job; you also figure out the solution.

As an Energy Analytics Data Scientist, you will think critically and strategically about Google’s fleet-wide energy assets, cloud as a technology, business and its operation, while thinking about its impact on the environment as a whole. You will apply your understanding of energy systems and market dynamics, optimization and statistical knowledge, and coding experience to develop methods that solve challenges related to optimal energy asset sizing, market participation, forecasting, and scalable control. You will work with different energy stakeholders across the organization and drive innovation of our energy systems stack, while improving its efficiency and global environmental impact.

Behind everything our users see online is the architecture built by the Technical Infrastructure team to keep it running. From developing and maintaining our data centers to building the next generation of Google platforms, we make Google's product portfolio possible. We're proud to be our engineers' engineers and love voiding warranties by taking things apart so we can rebuild them. We keep our networks up and running, ensuring our users have the best and fastest experience possible.

Responsibilities

Lead projects with energy system or market analysis, modeling and optimization, using multiple analytical methods and energy domain expertise to choose the tools/level of complexity to address business challenges.
Engage with the organization to identify, prioritize, frame, and structure complex and ambiguous challenges in the energy domain, where advanced analytics projects or tools can have the biggest impact.
Identify and communicate the challenges and opportunities that the group should be working on.
Help define/influence the analytical direction of the associated engineering and infrastructure work.
Articulate business questions and use mathematical techniques to arrive at an answer using data. Translate analysis results into business recommendations.

"""


# Step 2: Clean up job description posting.

job_description_list = job_description.split()  # Creates a list of words in the job description
clean_job_description = [  # Remove punctuation from list of words in job description
    word.replace('•', "")
        .replace('•', "")
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
    for line in job_description_list for word in line.lower().split()
    ]

job_count = dict()
for i in clean_job_description:
    job_count[i] = job_count.get(i, 0) + 1


# Step 3: Remove common words. Feel free to add words to the list that appear frequently in a job posting,
# but are considered filler words (e.g. "task," "assist," etc.)

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

for key in list(job_count.keys()):
    if key in common_job_words:
        del job_count[key]


# Step 4: Show top keywords in the job posting and their frequency
job_keywords = sorted(job_count.items(), key=lambda x: x[1], reverse=True)
print(job_keywords)





" Resume "


# Step 1: Copy your resume below within the triple quotes.

resume = """



"""


# Step 2: Clean up resume.
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
    for line in resume_list for word in line.lower().split()
    ]



# Step 3: Remove common words in resume. Feel free to add words to the list that appear frequently in your resume,
# but are considered filler words (e.g. cities you have worked in, your name, etc.)

common_job_words = [
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

resume_count = dict()
for i in clean_resume:
    resume_count[i] = resume_count.get(i, 0) + 1


# Step 4: Show top keywords in your resume and their frequency.
resume_keywords = sorted(resume_count.items(), key=lambda x: x[1], reverse=True)
print(resume_keywords)




" Identify Words in Job Posting not in your Resume "

missing = {k: v for k, v in job_count.items() if k not in resume_count}
missing_keywords = sorted(missing.items(), key=lambda x: x[1], reverse=True)
print(missing_keywords)

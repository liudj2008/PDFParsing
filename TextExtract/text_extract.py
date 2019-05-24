from resume_reader import *

import re



# Extract education
text = read_pdf('Resume_Peter.pdf')
education = re.findall(r'ph.d..*?\d+', text.lower())

# Extract skills
skill = re.findall(r'skills[\n](\w+.*?)\n', text.lower())[0]
skill = [i.strip() for i in skill.split(',')]

# Extract skill related experience
skill_experience = {}
if skill:
    for i in skill:
        string = re.compile('\n(.*?{i}.*?)\n'.format(i = i))
        skill_experience[i] = re.findall(string, text.lower())

 # Write to txt file
with open('resume.txt', 'w') as f:
    f.write(text)
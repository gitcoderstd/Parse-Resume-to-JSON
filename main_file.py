def parse_resume_to_json(resume_text):
    import re
    
    # Define regex patterns for extracting information
    name_pattern = re.compile(r"^([A-Z][a-z]+ [A-Z][a-z]+)", re.MULTILINE)
    contact_pattern = re.compile(r"Ph: ([+\d-]+)\nEmail: (.+?)\n", re.MULTILINE)
    linkedin_pattern = re.compile(r"LinkedIn: (https?://[^\s]+)")
    skills_pattern = re.compile(r"\n([A-Z ]{2,}.*?)\n\n", re.MULTILINE)
    education_pattern = re.compile(r"\n(\d{4} - \d{4}.+?)\n\n", re.MULTILINE)
    projects_pattern = re.compile(r"\n(\d{2} .+? Project Link:.+?)\n\n", re.MULTILINE)
    achievements_pattern = re.compile(r"\nACHIEVEMENTS\n\n(.+?)\n\n", re.MULTILINE)
    seminars_pattern = re.compile(r"\nSEMINARS / TRAININGS / WORKSHOPS\n\n(.+?)\n\n", re.MULTILINE)
    extra_curricular_pattern = re.compile(r"\nEXTRA CURRICULAR ACTIVITIES\n\n(.+?)\n\n", re.MULTILINE)
    personal_interests_pattern = re.compile(r"\nPERSONAL INTERESTS / HOBBIES\n\n(.+?)\n\n", re.MULTILINE)
    
    # Extract information using regex patterns
    name = name_pattern.search(resume_text).group(1)
    contact_info = contact_pattern.search(resume_text).groups()
    linkedin = linkedin_pattern.search(resume_text).group(1)
    skills = skills_pattern.search(resume_text).group(1).split()
    education = education_pattern.findall(resume_text)
    projects = projects_pattern.findall(resume_text)
    achievements = achievements_pattern.search(resume_text).group(1).split('\n')
    seminars = seminars_pattern.search(resume_text).group(1).split('\n')
    extra_curricular = extra_curricular_pattern.search(resume_text).group(1).split('\n')
    personal_interests = personal_interests_pattern.search(resume_text).group(1).split('\n')

    # Compile extracted information into a dictionary
    resume_json = {
        "name": name,
        "contact_info": {
            "phone": contact_info[0],
            "email": contact_info[1],
        },
        "linkedin": linkedin,
        "skills": skills,
        "education": education,
        "projects": projects,
        "achievements": achievements,
        "seminars_trainings_workshops": seminars,
        "extra_curricular_activities": extra_curricular,
        "personal_interests_hobbies": personal_interests,
    }

    return resume_json

# Example usage
resume_text = """
<Resume text here>
"""

resume_json = parse_resume_to_json(resume_text)
print(resume_json)

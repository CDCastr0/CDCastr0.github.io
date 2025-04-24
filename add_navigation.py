#!/usr/bin/env python3

import os

# Navigation HTML to add
navigation_html = '''
<div class="navigation-links">
  <a href="https://cdcastr0.github.io/">Home</a>
  <a href="https://cdcastr0.github.io/education">Education</a>
  <a href="https://cdcastr0.github.io/skills">Skills & Expertise</a>
  <a href="https://cdcastr0.github.io/experience">Experience</a>
  <a href="https://cdcastr0.github.io/projects">Projects</a>
  <a href="https://cdcastr0.github.io/research">Research Interests</a>
  <a href="https://cdcastr0.github.io/interests">Personal Interests</a>
  <a href="https://cdcastr0.github.io/resume">Resume</a>
</div>
'''

# Pages to modify (excluding README.md and about.md which we've already updated)
pages = [
    'education.md',
    'skills.md',
    'experience.md',
    'research.md',
    'interests.md',
    'resume.md',
    'projects/index.md'
]

for page in pages:
    if os.path.exists(page):
        with open(page, 'r', encoding='utf-8') as file:
            content = file.read()
        
        # Find position after the "Back to Home" link
        back_link_pos = content.find('[← Back to Home]')
        if back_link_pos != -1:
            # Find the end of that line
            line_end = content.find('\n', back_link_pos)
            if line_end != -1:
                # Insert navigation after that line
                new_content = content[:line_end+1] + navigation_html + content[line_end+1:]
                
                # Write the updated content
                with open(page, 'w', encoding='utf-8') as file:
                    file.write(new_content)
                print(f"Updated {page}")
            else:
                print(f"Couldn't find line end in {page}")
        else:
            print(f"Couldn't find back link in {page}")
    else:
        print(f"File {page} doesn't exist")

print("Navigation added to pages!") 
#!/usr/bin/env python3

import os

# Footer HTML to add
footer_html = '''
<footer class="site-footer">
  <p>&copy; 2025 Christian Castro. All rights reserved.</p>
</footer>
'''

# Pages to modify (excluding README.md which we've already updated)
pages = [
    'about.md',
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
        
        # Find position before the last navigation links
        back_nav_pos = content.rfind('[← Back to Home]')
        if back_nav_pos != -1:
            # Insert footer before the navigation links
            new_content = content[:back_nav_pos] + footer_html + '\n\n' + content[back_nav_pos:]
            
            # Write the updated content
            with open(page, 'w', encoding='utf-8') as file:
                file.write(new_content)
            print(f"Updated {page}")
        else:
            print(f"Couldn't find back navigation in {page}")
    else:
        print(f"File {page} doesn't exist")

print("Footers added to pages!") 
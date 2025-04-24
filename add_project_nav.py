#!/usr/bin/env python3

import os
import glob

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

# Footer HTML to add
footer_html = '''
<footer class="site-footer">
  <p>&copy; 2025 Christian Castro. All rights reserved.</p>
</footer>
'''

# Find all project README.md files
project_pages = glob.glob('projects/*/README.md')

for page in project_pages:
    with open(page, 'r', encoding='utf-8') as file:
        content = file.read()
    
    # Find position after the "Back to Main Page" or "Back to Home" link
    back_link_pos = max(content.find('[← Back to Main Page]'), content.find('[← Back to Home]'))
    
    if back_link_pos != -1:
        # Find the end of that line
        line_end = content.find('\n', back_link_pos)
        if line_end != -1:
            # Insert navigation after that line
            modified_content = content[:line_end+1] + navigation_html + content[line_end+1:]
            
            # Find position before the last navigation links
            back_nav_pos = modified_content.rfind('[← Back to')
            if back_nav_pos != -1:
                # Insert footer before the navigation links
                modified_content = modified_content[:back_nav_pos] + footer_html + '\n\n' + modified_content[back_nav_pos:]
                
                # Update all "Back to Main Page" to "Back to Home" for consistency
                modified_content = modified_content.replace('Back to Main Page', 'Back to Home')
                
                # Write the updated content
                with open(page, 'w', encoding='utf-8') as file:
                    file.write(modified_content)
                print(f"Updated {page}")
            else:
                print(f"Couldn't find back navigation in {page}")
        else:
            print(f"Couldn't find line end in {page}")
    else:
        print(f"Couldn't find back link in {page}")

print("Navigation and footers added to project pages!") 
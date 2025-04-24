// Dark Mode Toggle Functionality

// Function to toggle between dark and light mode
function toggleTheme() {
  const currentTheme = document.documentElement.getAttribute('data-theme');
  const switchToTheme = currentTheme === 'dark' ? 'light' : 'dark';
  
  // Set the theme
  document.documentElement.setAttribute('data-theme', switchToTheme);
  
  // Save the preference to localStorage
  localStorage.setItem('theme', switchToTheme);
}

// Function to add the toggle switch to the page
function addToggleSwitch() {
  const toggleContainer = document.createElement('div');
  toggleContainer.className = 'toggle-container';
  
  const toggleText = document.createElement('span');
  toggleText.className = 'toggle-text';
  toggleText.textContent = 'Theme:';
  
  const themeToggle = document.createElement('label');
  themeToggle.className = 'theme-toggle';
  
  const checkbox = document.createElement('input');
  checkbox.type = 'checkbox';
  checkbox.id = 'theme-toggle';
  checkbox.checked = document.documentElement.getAttribute('data-theme') === 'dark';
  
  checkbox.addEventListener('change', toggleTheme);
  
  const slider = document.createElement('span');
  slider.className = 'slider';
  
  themeToggle.appendChild(checkbox);
  themeToggle.appendChild(slider);
  
  toggleContainer.appendChild(toggleText);
  toggleContainer.appendChild(themeToggle);
  
  document.body.appendChild(toggleContainer);
}

// Function to set theme based on saved preference or system preference
function setInitialTheme() {
  const savedTheme = localStorage.getItem('theme');
  
  if (savedTheme) {
    document.documentElement.setAttribute('data-theme', savedTheme);
    return;
  }
  
  // Check if user prefers dark mode
  const prefersDarkMode = window.matchMedia && window.matchMedia('(prefers-color-scheme: dark)').matches;
  
  if (prefersDarkMode) {
    document.documentElement.setAttribute('data-theme', 'dark');
  } else {
    document.documentElement.setAttribute('data-theme', 'light');
  }
}

// Initialize theme and add toggle switch when DOM is loaded
document.addEventListener('DOMContentLoaded', function() {
  setInitialTheme();
  addToggleSwitch();
}); 
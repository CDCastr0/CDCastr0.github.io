// Theme Switcher Functionality

// Check for saved theme preference or use the system preference
function getPreferredTheme() {
  // Check if user has previously chosen a theme
  const savedTheme = localStorage.getItem('theme');
  if (savedTheme) {
    return savedTheme;
  }
  
  // If no saved preference, check system preference
  return window.matchMedia('(prefers-color-scheme: dark)').matches ? 'dark' : 'light';
}

// Function to set the theme
function setTheme(theme) {
  document.documentElement.setAttribute('data-theme', theme);
  localStorage.setItem('theme', theme);
  
  // Update toggle state if it exists
  const toggleIcon = document.getElementById('theme-toggle-icon');
  if (toggleIcon) {
    toggleIcon.textContent = theme === 'dark' ? '☀️' : '🌙';
    toggleIcon.setAttribute('aria-label', theme === 'dark' ? 'Switch to light mode' : 'Switch to dark mode');
  }
}

// Function to toggle the theme
function toggleTheme() {
  const currentTheme = document.documentElement.getAttribute('data-theme') || 'light';
  const newTheme = currentTheme === 'light' ? 'dark' : 'light';
  setTheme(newTheme);
}

// Apply the theme when the page loads
document.addEventListener('DOMContentLoaded', () => {
  // Set initial theme
  setTheme(getPreferredTheme());
  
  // Add event listener to toggle button if it exists
  const themeToggle = document.getElementById('theme-toggle');
  if (themeToggle) {
    themeToggle.addEventListener('click', toggleTheme);
  }
  
  // Listen for system preference changes
  window.matchMedia('(prefers-color-scheme: dark)').addEventListener('change', e => {
    if (!localStorage.getItem('theme')) {
      setTheme(e.matches ? 'dark' : 'light');
    }
  });
}); 
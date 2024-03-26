const homeTab = document.getElementById("home-tab");
const profileTab = document.getElementById("profile-tab");

var tabLinks = document.querySelectorAll('.tab-nav-link');

// Function to switch between tabs
function switchTab(tabName) {
  // Hide all tab contents
  var tabContents = document.querySelectorAll('.tab-pane');
  tabContents.forEach(function(tabContent) {
    tabContent.classList.remove('show', 'active');
  });

  // Show the selected tab content
  document.getElementById(tabName).classList.add('show', 'active');

  // Update the active class for the tab navigation

  console.log(tabLinks)


  tabLinks.forEach(function(tabLink) {
    tabLink.classList.remove('active');
    tabLink.classList.remove('show-link');
    if (tabLink.getAttribute('href').slice(1) === tabName) {
      tabLink.classList.add('active');
      tabLink.classList.add('show-link');
    }
  });
}

// Add event listeners to the tab links
document.getElementById('home-tab').addEventListener('click', function() {
  switchTab('home');
});

document.getElementById('profile-tab').addEventListener('click', function() {
  switchTab('profile');
});

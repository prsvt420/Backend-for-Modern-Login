const container = document.getElementById('container');
const registerBtn = document.getElementById('register');
const loginBtn = document.getElementById('login');

registerBtn.addEventListener('click', () => {
  container.classList.add("active");
  localStorage.setItem('containerState', 'active');
});

loginBtn.addEventListener('click', () => {
  container.classList.remove("active");
  localStorage.setItem('containerState', 'inactive');
});

document.addEventListener('DOMContentLoaded', () => {
  const containerState = localStorage.getItem('containerState');

  if(containerState === 'active') {
    container.classList.add("active");
  } else {
    container.classList.remove("active");
  }
});
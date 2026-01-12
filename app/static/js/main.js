function toggleTheme()
{
  const root = document.documentElement;
  const currentTheme = getComputedStyle(root).getPropertyValue('--theme');
  const lightTheme = getComputedStyle(root).getPropertyValue('--lightTheme');
  const darkTheme = getComputedStyle(root).getPropertyValue('--darkTheme');
  const sunUnicode = getComputedStyle(root).getPropertyValue('--sunUnicode');
  const moonUnicode = getComputedStyle(root).getPropertyValue('--moonUnicode');

  if (currentTheme === lightTheme)
  {
    root.style.setProperty('--theme', darkTheme);
    document.getElementById("theme").innerHTML = sunUnicode;
    root.style.setProperty('--currentUnicode', sunUnicode);
    localStorage.setItem('theme', darkTheme);
  }
  else if (currentTheme === darkTheme)
  {
    root.style.setProperty('--theme', lightTheme);
    document.getElementById("theme").innerHTML = moonUnicode;
    root.style.setProperty('--currentUnicode', moonUnicode);
    localStorage.setItem('theme', lightTheme);
  }
}

document.getElementById("sidebarToggle").onclick = () => sidebarToggle()
document.getElementById("sidebarBackgroundToggle").onclick = () => sidebarToggle()

function sidebarToggle()
{
  const sidebar = document.querySelector(".sidebar");
  const sidebardim =document.querySelector(".sidebar-dim")
  sidebar.classList.toggle("open");
  sidebardim.classList.toggle("visible");
}

/*
let t = 0;
let light = document.documentElement.getPro

function animateTheme(target) {
  const step = target > t ? 0.02 : -0.02;

  const interval = setInterval(() => {
    t = Math.max(0, Math.min(1, t + step));
    document.documentElement.style.setProperty("--t", t);

    if (t === target) clearInterval(interval);
  }, 16);
}
  */
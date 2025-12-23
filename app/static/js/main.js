function toggleTheme()
{
  const root = document.documentElement;
  const currentTheme = getComputedStyle(root).getPropertyValue('--theme');
  const lightTheme = getComputedStyle(root).getPropertyValue('--lightTheme');
  const darkTheme = getComputedStyle(root).getPropertyValue('--darkTheme');

  if (currentTheme === lightTheme)
  {
    root.style.setProperty('--theme', '0%')
  }
  else if (currentTheme === darkTheme)
  {
    root.style.setProperty('--theme', '100%')
  }
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
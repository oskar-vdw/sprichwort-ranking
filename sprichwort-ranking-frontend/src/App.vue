<template>
  <header>
    <div class="header-content">
      <img alt="Sprichwort-Ranking Website logo" class="logo" src="/public/sprichwort_icon.jpg" width="50"
        height="50" />
      <nav>
        <RouterLink to="/">Abstimmen</RouterLink>
        <RouterLink to="/list">Liste</RouterLink>
      </nav>
    </div>
  </header>

  <RouterView />


</template>

<style scoped>
header {
  position: relative;
  top: 0;
  left: 0;
  right: 0;
  background-color: var(--color-background);
  z-index: 1;
  box-shadow: 0 2px 4px rgba(0, 0, 0, 0.1);
  width: 100%;
}

.header-content {
  margin: 0 auto;
  padding: 1rem;
  display: flex;
  flex-direction: column;
  align-items: center;
}

.logo {
  display: block;
  border-radius: 50%;
  width: 50px;
  height: 50px;
  margin-bottom: 1rem;
}

nav {
  width: 100%;
  font-size: 12px;
  text-align: center;
}

nav a {
  display: inline-block;
  padding: 0.5rem 1rem;
  border-left: 1px solid var(--color-border);
}

nav a:first-of-type {
  border: 0;
}

nav a.router-link-exact-active {
  color: var(--color-text);
}

nav a.router-link-exact-active:hover {
  background-color: transparent;
}

@media (min-width: 768px) {


  .header-content {
    flex-direction: row;
    justify-content: flex-start;
    align-items: center;
  }

  .logo {
    margin: 0 2rem 0 0;
  }

  nav {
    font-size: 1rem;
    text-align: left;
  }
}
</style>
<template>
  <div id="app">
    <Sidebar />
    <h2>Main Content</h2>
  </div>
</template>

<script setup>
import Sidebar from "./components/MySidebar.vue";
</script>

<style Lang="scss">
:root {
  --primary: #00acb4;
  --light: #fff;
  --dark: #000;
  --grey: #c4c4c4;
  --light-gray: #f4f4f4;
  --dark-gray: #333;
  --sidebar-width: 335px;
}
* {
  margin: 0;
  padding: 0;
  box-sizing: border-box;
}
body {
  background: var(--light);
}

button {
  cursor: pointer;
  border: none;
  background: none;
  outline: none;
  appearance: none;
}

.app {
  display: flex;
  main {
    flex: 1 1 0;
    padding: 2rem;
    @media (max-width: 768px) {
      padding: 6rem;
    }
  }
}
</style>

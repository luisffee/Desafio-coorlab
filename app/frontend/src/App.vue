<template>
  <div id="app" class="app">
    <MySidebar />
    <div class="content">
      <div class="top"></div>
      <div class="content-wrapper">
        <TravelCalc />
      </div>
    </div>
  </div>
</template>

<script setup>
import MySidebar from "./components/MySidebar.vue";
import TravelCalc from "./components/TravelCalc.vue";
</script>

<style Lang="scss">
:root {
  --primary: #00acb4;
  --light: #fff;
  --dark: #000;
  --gray: #c4c4c4;
  --light-gray: #f4f4f4;
  --dark-gray: #333;
  --sidebar-width: 20vw;
}
* {
  margin: 0;
  padding: 0;
  box-sizing: border-box;
  font-family: "Fira sans", sans-serif;
}

body {
  background: var(--light);
}

button {
  cursor: pointer;
  appearance: none;
  border: none;
  outline: none;
  background: none;
}

.app {
  display: flex;

  .content {
    flex: 1 1 0;
    display: flex;
    flex-direction: column;
    justify-content: center;

    .top {
      display: flex;
      height: 5rem;
      width: 100%;
      box-shadow: rgba(17, 17, 26, 0.3) 0px 7px 3px;
    }

    .content-wrapper {
      display: flex;
      justify-content: center;
      height: 100%;
      padding-top: 5rem;
    }
  }

  main {
    flex: 1 1 0;
    padding: 2rem;

    @media (max-width: 1024px) {
      padding-left: 6rem;
    }
  }
}
</style>

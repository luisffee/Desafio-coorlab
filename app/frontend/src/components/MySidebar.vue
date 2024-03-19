<template>
  <aside
    :class="`${is_expanded && 'is_expanded'}`"
    @mouseenter="ToggleMenu"
    @mouseleave="ToggleMenu"
  >
    <div class="logo menu-toggle-wrap">
      <img src="../assets/logo.png" alt="Logo" class="menu-toggle" />
    </div>
    <div class="menu">
      <div class="button">
        <span class="material-icons">calculate</span>
        <span class="text">Calculadora de Viagem</span>
      </div>
    </div>
  </aside>
</template>

<script setup>
import { ref } from "vue";

const is_expanded = ref(false);

const ToggleMenu = () => {
  is_expanded.value = !is_expanded.value;
};
</script>

<style Lang="scss" scoped>
aside {
  display: flex;
  flex-direction: column;
  width: calc(4rem);
  min-height: 100vh;
  overflow: hidden;
  padding: 0.5rem;

  background-color: var(--dark-gray);
  color: var(--light);

  transition: 0.2s ease-out;

  img {
    cursor: pointer;
  }

  .logo {
    margin-bottom: 1rem;
    img {
      width: 20.1rem;
    }
  }

  .menu_toggle_wrap {
    display: flex;
    margin-bottom: 1rem;

    position: relative;
    top: 0;
    transition: 0.2s ease-out;
    .menu_toggle {
      transition: 0.2s ease-out;
      cursor: pointer;
    }
  }

  .button .text {
    opacity: 0;
    transition: 0.3s ease-out;
  }

  .menu {
    margin: 0 -1rem;
    cursor: pointer;

    .button {
      display: flex;
      align-items: center;
      text-decoration: none;

      .material-icons {
        cursor: pointer;
        margin-left: 1rem;
        font-size: 2.5rem;
        color: var(--dark-grey);
        transition: 0.2s ease-out;
      }

      .text {
        color: var(--light);
        transition: 0.2s ease-out;
      }

      &:hover {
        background-color: var(--dark-grey);
        .material-icons {
          color: var(--primary);
        }
        .text {
          color: var(--primary);
        }
      }
    }
  }

  &.is_expanded {
    width: var(--sidebar-width);

    .menu-toggle-wrap {
      top: -3rem;
    }

    .menu {
      .button {
        .material-icons {
          transition: 1s ease-out;
        }
        .text {
          opacity: 1;
          transition: 1s ease-out;
        }
      }
    }
  }

  @media (max-width: 768px) {
    position: fixed;
    z-index: 99;
  }
}
</style>

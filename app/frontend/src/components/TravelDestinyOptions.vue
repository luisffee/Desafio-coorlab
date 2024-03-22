<template>
  <select class="form-input" placeholder="Selecione o destino">
    <option value="" hidden disabled selected>Selecione o destino</option>
    <option class="options" v-for="(value, key) in props.options" :key="key">
      {{ value }}
    </option>
  </select>
</template>

<script setup>
import { defineProps } from "vue";

const props = defineProps(["options"]);
</script>

<style Lang="scss">
.form-input {
  display: flex;
  height: 2.5rem;
  width: 100%;
  border-radius: 6px;
  margin: 0.5rem 0 0 0;
  font-weight: 200;
}
</style>

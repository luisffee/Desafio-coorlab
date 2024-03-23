<template>
  <select
    v-model="selectedCityId"
    class="form-input"
    placeholder="Selecione o destino"
  >
    <option value="" hidden disabled selected :key="null">
      Selecione o destino
    </option>
    <option
      class="options"
      v-for="(city, id) in props.options"
      :key="id"
      :value="id"
    >
      {{ city }}
    </option>
  </select>
</template>

<script setup>
import { ref, defineProps, defineEmits, watchEffect } from "vue";

const props = defineProps(["options"]);
const emitCitySelected = defineEmits(["city-selected"]);

const selectedCityId = ref(null);
const cities = ref([]);

watchEffect(() => {
  if (props.options) {
    cities.value = Object.entries(props.options).map(([id, name]) => ({
      id,
      name,
    }));
  }
});

const onCitySelected = () => {
  emitCitySelected("city-selected", selectedCityId.value);
};

watchEffect(() => {
  onCitySelected();
});
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

<template>
  <div class="form-wrapper">
    <div class="form-header">
      <span class="material-icons">local_shipping</span>
      <span class="calc-title">Calculadora de Viagem</span>
    </div>
    <div class="calc-main">
      <div class="form-main">
        <div class="calc-title-wrapper">
          <span class="material-icons">price_check</span>
          <h2 class="calc-text">Calcule o Valor da Viagem</h2>
        </div>
        <form action="" class="calc-form" @submit.prevent="checkEmpty()">
          <h4 class="form-text">Destino</h4>
          <TravelDestinyOptions
            :options="transports_cities"
            @city-selected="onCitySelected"
          />
          <h4 class="form-text">Data</h4>
          <input
            class="form-input"
            type="date"
            v-model="selectedDate"
            placeholder=" "
          />
          <button class="form-button" type="submit">Buscar</button>
        </form>
      </div>
      <div class="results">
        <div v-if="transports_prices != null" class="show-results">
          <h2 class="result-title">
            Estas são as melhores alternativas de viagem para a data selecionada
          </h2>
          <div class="confort-wrapper">
            <div class="confort-info-wrapper">
              <span class="material-icons">monetization_on</span>
              <div class="confort-info">
                <h3 class="confort-name">
                  {{ transports_prices.best_price_confort.name }}
                </h3>
                <p class="confort-bed">
                  Poltrona:
                  {{ transports_prices.best_price_confort.bed }}
                  (Leito)
                </p>
                <p class="confort-duration">
                  Tempo estimado:
                  {{ transports_prices.best_price_confort.duration }}
                  horas
                </p>
              </div>
            </div>
            <div class="confort-price-wrapper">
              <h3 class="confort-price-title">Preço</h3>
              <p class="confort-price">
                R$
                {{ transports_prices.best_price_confort.price_confort }}
              </p>
            </div>
          </div>
          <div class="econ-wrapper">
            <div class="econ-info-wrapper">
              <span class="material-icons">sell</span>
              <div class="econ-info">
                <h3 class="econ-name">
                  {{ transports_prices.best_price_econ.name }}
                </h3>
                <p class="econ-bed">
                  Poltrona:
                  {{ transports_prices.best_price_econ.bed }}
                  (Convencional)
                </p>
                <p class="econ-duration">
                  Tempo estimado:
                  {{ transports_prices.best_price_econ.duration }}
                  horas
                </p>
              </div>
            </div>
            <div class="econ-price-wrapper">
              <h3 class="econ-price-title">Preço</h3>
              <p class="econ-price">
                R$
                {{ transports_prices.best_price_econ.price_econ }}
              </p>
            </div>
          </div>
          <button class="results-clean" @click="resetPage">Limpar</button>
        </div>
        <div v-else class="no-result">
          <h2 class="no-result-text">Nenhum dado selecionado</h2>
        </div>
      </div>
    </div>
    <div v-if="showModal" class="modal-wrapper">
      <div class="modal">
        <span class="material-icons">error</span>
        <h1 class="text">Insira os valores para realizar cotação</h1>
        <button class="button" @click="closeModal">Fechar</button>
      </div>
    </div>
  </div>
</template>

<script setup>
import axios from "axios";
import { ref } from "vue";
import TravelDestinyOptions from "./TravelDestinyOptions.vue";

const transports_cities = ref(null);
const transports_prices = ref(null);
const selectedCity = ref(null);
const selectedDate = ref(null);
const showModal = ref(false);

const fetchTransportes = async () => {
  const { data } = await axios.get("/api/Travels/cities");
  transports_cities.value = data.cities;
};
fetchTransportes();

const mapTransportData = (data) => {
  return {
    bed: data.bed,
    city: data.city,
    duration: data.duration,
    name: data.name,
    price_confort: data.price_confort,
    price_econ: data.price_econ,
    seat: data.seat,
  };
};

const checkEmpty = () => {
  if (!selectedCity.value || !selectedDate.value) {
    showModal.value = true;
    return;
  }
  fetchPrices();
};

const closeModal = () => {
  showModal.value = false;
};

const resetPage = () => {
  window.location.reload();
};

const fetchPrices = async () => {
  try {
    const { data } = await axios.get(
      `/api/Travels/bestprices/${selectedCity.value}`
    );

    transports_prices.value = {
      best_price_econ: mapTransportData(data.best_price_econ),
      best_price_confort: mapTransportData(data.best_price_confort),
    };
  } catch (error) {
    console.error(error);
  }
};

const onCitySelected = (cityId) => {
  selectedCity.value = cityId;
};
</script>

<style Lang="scss">
.form-wrapper {
  display: flex;
  flex-direction: column;
  align-items: center;
  justify-content: center;
  justify-self: center;
  height: 70vh;
  width: 75vw;
  box-shadow: rgba(0, 0, 0, 0.03) 0px 1px 1px, rgba(0, 0, 0, 0.03) 0px 2px 2px,
    rgba(0, 0, 0, 0.03) 0px 4px 4px, rgba(0, 0, 0, 0.03) 0px 8px 8px,
    rgba(0, 0, 0, 0.03) 0px 16px 16px;
  border-radius: 6px;

  .form-header {
    display: flex;
    justify-content: center;
    height: 5rem;
    width: 100%;
    background-color: var(--secundary);

    .material-icons {
      display: flex;
      align-items: center;
      padding: 0 0 0 3rem;
      font-size: 2.5rem;
      color: var(--light);
    }

    .calc-title {
      display: flex;
      align-items: center;
      height: 100%;
      width: 100%;
      padding: 0 0 0 1rem;
      font-size: 30px;
      color: var(--light);
    }
  }

  .calc-main {
    display: flex;
    flex-direction: row;
    height: 100%;
    width: 100%;

    .form-main {
      display: flex;
      width: 40%;
      padding: 2rem 2rem 1rem 2rem;
      border-radius: 10px;
      background-color: var(--light-gray);
      background-clip: content-box;

      .calc-title-wrapper {
        display: flex;
        justify-content: center;
        margin: 5rem 0 0 0;

        .material-icons {
          display: flex;
          align-items: center;
          padding: 0 0.3rem 0 0;
          font-size: 2.5rem;
        }

        .calc-text {
          display: flex;
          align-items: center;
          padding: 0 0.3rem 0 0;
          font-weight: 500;
        }
      }

      form {
        display: flex;
        padding: 1.5rem 0 0 0;

        .form-text {
          display: flex;
          padding: 1.5rem 0 0 0;
          font-size: 1rem;
          font-weight: 400;
        }
      }
    }

    .results {
      display: flex;
      padding: 2rem 1rem 1rem 1rem;
    }
  }

  .form-main {
    display: flex;
    flex-direction: column;

    .calc-form {
      display: flex;
      flex-direction: column;
      margin: 0 2.5rem 0 2.5rem;

      .form-button {
        display: flex;
        align-self: center;
        justify-content: center;
        align-items: center;
        height: 2rem;
        width: 60%;
        border-radius: 6px;
        margin: 3rem 0 0 0;
        color: var(--dark);
        background-color: var(--primary);
      }
    }
  }

  .results {
    display: flex;
    justify-content: center;
    width: 60%;

    .no-result {
      display: flex;
      align-self: center;

      .no-result-text {
        display: flex;
        align-items: center;
        justify-content: center;
        font-size: 1.5rem;
        font-weight: 400;
      }
    }

    .show-results {
      display: flex;
      flex-direction: column;

      .result-title {
        display: flex;
        width: 70%;
        padding: 5.3rem 0 1rem 0;
        font-size: 1.5rem;
        font-weight: 400;
      }

      .confort-wrapper {
        display: flex;
        margin: 0 0 1.5rem 0;
        flex-direction: row;
        height: 7rem;

        .confort-info-wrapper {
          display: flex;
          padding: 0 1rem 0 0;
          width: 70%;
          background-clip: content-box;
          background-color: var(--light-gray);
          border-radius: 10px;

          .material-icons {
            display: flex;
            align-items: center;
            justify-content: center;
            width: 15%;
            background-color: var(--primary);
            color: var(--light);
            font-size: 2.5rem;
          }

          .confort-info {
            display: flex;
            flex-direction: column;
            align-self: center;
            padding: 0 0 0 2rem;

            .confort-name {
              display: flex;
              padding: 0 0 0.3rem 0;
            }

            .confort-bed {
              display: flex;
              padding: 0 0 0.3rem 0;
            }

            .confort-duration {
              display: flex;
            }
          }
        }

        .confort-price-wrapper {
          display: flex;
          padding: 0 0 0 1rem;
          flex-direction: column;
          justify-content: center;
          width: 30%;
          background-color: var(--light-gray);
          border-radius: 10px;
        }
      }

      .econ-wrapper {
        display: flex;
        flex-direction: row;
        height: 7rem;

        .econ-info-wrapper {
          display: flex;
          padding: 0 1rem 0 0;
          width: 70%;
          background-clip: content-box;
          background-color: var(--light-gray);
          border-radius: 10px;

          .material-icons {
            display: flex;
            align-items: center;
            justify-content: center;
            width: 15%;
            background-color: var(--primary);
            color: var(--light);
            font-size: 2.5rem;
          }

          .econ-info {
            display: flex;
            flex-direction: column;
            align-self: center;
            padding: 0 0 0 2rem;
            .econ-name {
              display: flex;
              padding: 0 0 0.3rem 0;
            }

            .econ-bed {
              display: flex;
              padding: 0 0 0.3rem 0;
            }

            .econ-duration {
              display: flex;
            }
          }
        }

        .econ-price-wrapper {
          display: flex;
          padding: 0 0 0 1rem;
          flex-direction: column;
          justify-content: center;
          width: 30%;
          background-color: var(--light-gray);
          border-radius: 10px;

          .econ-price-title {
            display: flex;
            padding: 0 0 0.7rem 0;
          }

          .econ-price {
            display: flex;
          }
        }
      }
    }

    .results-clean {
      display: flex;
      margin: 6rem 0 0 40rem;
      justify-content: center;
      align-items: center;
      height: 2rem;
      width: 10rem;
      background-color: var(--bright);
      color: var(--dark);
      border-radius: 6px;
    }
  }
  .modal-wrapper {
    position: fixed;
    top: 0;
    left: 0;
    width: 100%;
    height: 100%;
    background-color: rgba(0, 0, 0, 0.5);
    display: flex;
    justify-content: center;
    align-items: center;

    .modal {
      display: flex;
      flex-direction: column;
      align-items: center;
      justify-content: center;
      background-color: var(--light);
      padding: 20px;
      border-radius: 10px;

      .material-icons {
        font-size: 4rem;
        color: var(--primary);
      }

      .text {
        background-color: white;
        padding: 20px;
        border-radius: 10px;
        font-size: 1.5rem;
        font-weight: 400;
        padding: 2rem 4rem 2rem 4rem;
      }

      .button {
        display: flex;
        justify-content: center;
        align-items: center;
        height: 2rem;
        width: 10rem;
        background-color: var(--primary);
        color: var(--dark);
        border-radius: 6px;
        margin-top: 1rem;
      }
    }
  }
}
</style>

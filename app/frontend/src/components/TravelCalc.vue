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
        <form action="" class="calc-form">
          <h4 class="form-text">Destino</h4>
          <select class="form-input" placeholder="Selecione o destino">
            <option value="" hidden disabled selected>
              Selecione o destino
            </option>
          </select>
          <h4 class="form-text">Data</h4>
          <input class="form-input" type="date" name="" id="" placeholder=" " />
          <button class="form-button" type="submit">Buscar</button>
        </form>
      </div>
      <div class="results">
        <h2 class="no-result">Nenhum dado selecionado</h2>
      </div>
    </div>
  </div>
</template>

<script setup></script>

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
    background-color: var(--dark);

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

      .form-input {
        display: flex;
        height: 2.5rem;
        width: 100%;
        border-radius: 6px;
        margin: 0.5rem 0 0 0;
        font-weight: 200;
      }

      .form-button {
        display: flex;
        align-self: center;
        justify-content: center;
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
      font-weight: 400;
    }
  }
}
</style>

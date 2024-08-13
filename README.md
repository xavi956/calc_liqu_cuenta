Simulador de Evolución de Cuenta de Trading
Este repositorio contiene un script en Python que simula la evolución de una cuenta de trading a lo largo de diferentes períodos de tiempo (1 mes, 3 meses, 6 meses y 1 año). El simulador utiliza parámetros que el usuario proporciona, como el capital inicial, el porcentaje del balance usado por operación, el número de operaciones semanales, y el porcentaje de beneficio promedio por operación.

Funcionalidad
El programa permite al usuario estimar cómo crecería el balance de su cuenta de trading bajo ciertas condiciones. Los cálculos se realizan semanalmente y consideran el uso de una parte del balance en cada operación.

Parámetros de Entrada
liq_inicial: Valor inicial de la cuenta de trading.
por_opp: Porcentaje del balance de la cuenta que se usa en cada operación.
op_sem: Número de operaciones realizadas semanalmente.
PnL: Porcentaje promedio de beneficio por operación (incluyendo apalancamiento si aplica).
Simulación
El usuario puede elegir uno de los siguientes períodos de simulación:

1 mes: Simula la evolución de la cuenta durante 4 semanas.
3 meses: Simula la evolución de la cuenta durante 12 semanas.
6 meses: Simula la evolución de la cuenta durante 24 semanas.
1 año: Simula la evolución de la cuenta durante 48 semanas.
El simulador calcula y muestra el balance acumulado al final de cada semana dentro del período seleccionado.

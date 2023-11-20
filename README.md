Desafío 2: Un día en la playa con Yasna
=======================================
## Contexto:
Yasna se encamina a la playa Los Placeres para disfrutar del lindo día. Le gusta tener cuerpo y mente sana. Hoy planea nadar hasta una boya que hay en el mar por la ruta de menor consumo y consumir a lo más 5 alimenos buscando minimizar la diferencia de calorías. Busca consumir igual o un poco menos de lo que quemó.
Los alimentos disponibles en la playa son con su respectivo suministro calórico por gramo:
|Alimento|Suministro [kcal/g]|
|-|-|
|Sandía|0.2|
|Helado|1|
|Cuchuflí|3|
|Palmera|5.5|
El oleaje del mar es mapeado en una matriz. En una de las celdas hay una 'B' para indicar la posición de la boya (al llegar aquí no se aplicará gasto calórico adicional y contará como un paso), mientras que en el resto hay números para indicar nivel de oleaje. La primera fila indica la línea de costa, mientra la última indica la línea más mar adentro
Un número positivo en una celda indica que el oleaje va hacia la costa, mientras que un número negativo la ola va mar adentro. El esfuerzo que implica cruzar nadando una grilla viene dado por 1 kcal más el componente del oleaje. Si se entra a la grilla desde una celda que está más a la costa se resta el número, mientras que si se entra desde una celda que está mar adentro se suma y por último si se entra desde una línea horizontal no se contará el componente oleaje y por tanto se gastará 1 kcal. Si el esfuerzo neto es negativo (cuando el nivel de oleaje es mayor a 1), debe considerarse como 0 (se deja por la corriente)
Ayuda a Yasna a equilibrar sus calorías (en caso de que utilice bibliotecas externas debe agregarlas en requirements.txt)

## Parte 1: Calorías consumidas
Implenta la función select_food en utils.py para selecciona los alimentos (no se pueden dejar sobras de lo comprado) que  que retorna un diccionario con 2 items:
* consumed_energy: Número de kilocalorías consumidas
* consumed_food: Lista de enteros, donde cada entero indica la posición del alimento seleccionado a consumir (conteo desdse 0)
Y se recibe 2 parámetros:
* meals: Lista de tuplas de 2 elementos, donde el primer elemento es tipo de alimento y el segundo elemento el peso. Cada tupla 
* goal: Kilocalorías consumidas
representa 1 unidad de alimento.
En caso de que 2 consuntos de alimentos suministren la misma cantidad de energía óptima se elige el de mayor cantidad y luego los que aparezcan primero en la lista entregada. Es decir si se eligen 3 de 5 ABCDE, las solución según prioridad son ABC, ABD, ACD, BCD, ABE, ACE, BCE, ADE, BDE, CDE.

## Parte 2: Calorías gastadas
Implementa la función get_burning_calories en utils.py para trazar la ruta de mínimo consumo para ir y vover de la boya, retornando un diccionario con 2 items
* burning: kcal quemads
* steps: Número total de grillas nadadas (boya cuenta como 1 paso)
y recibiendo 1 parámetro que es el mapa del mar (matriz: Lista de lista) con el nivel de oleaje.
Entre 2 soluciones con el mismo esfuerzo mínimo, se priorizará la que tenga menos pasos. Al entrar al mar desde la playa el esfuerzo es acorde al señalada en fila 0, mientras que la salida del mar a playa no tiene esfuerzo. Los steps corresponden a todos las casillas en que se nada (inclusive la boya)
## Parte 3: Minimizar diferencia calórica
Implementa la función get_calories en utils.py de manera de elegir la opción que minimiza la diferencia calórica a favor de calorías quemadas,  retornando un diccionario con 2 items:
* net_energy: Calorías netas quemadadas (diferencia entre quemadas y consumidas)
* burning_rate: cociente entre kcal quemadas y número de grillas nadadas con un redondeo de 2 decimales
* consumed_food: Diccionario cuya claves sean los tipos de alimentos consumidos y los valores la suma total del peso de aquel alimento
Y recibiendo 2 parámetros:
* meals: Es una lista de tuplas, donde el primer elemento de la tupla es el tipo de alimento y el segundo es el peso del alimento.
* sea: Lista de listas (Matriz) de números que indican cuantas calorías se gastarán al cruzar esa celda
BONUS: Yasna puede bucear hasta en 5 veces en todo su trayecto para sortear los puntos más agitados, requiriendo un costo constante de de sólo 0.5 kcal en el tramo. ¿Cómo sería el gasto y el consumo en este caso? 
Corre los tests con:
python playa.py

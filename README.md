# ALDA_Proyecto

En la carpeta código se encuentra los archivos ejecutables AntColony.py y readCase.py:
  1. Este código hace uso de la libería "numpy", si no cuenta con esta librería ejecutar el comando: $pip3 install numpy 
     para que el instalador de Python descargue las liberías necesarias y poder ejecutar el código sin problemas
  2. Para ejecutar el código, primero toca pasar estos dos archivos a la ruta donde contiene las instancias de prueba, 
     luego ejecutar este comando en la terminal: $py ó python readCase.py <nombre_del_archivo.txt> <tiempo en segundos>
  3. Si el algoritmo retorna una trayectoria y un valor estos hacen referencia a la trayectoria y a la distancia de esa trayectoria:
     ej: shortest_path: ([(0, 14), (14, 13), (13, 9), (9, 18), (18, 4), (4, 8), (8, 5), (5, 6), (6, 7), (7, 16), (16, 19), (19, 11), (11, 17), (17, 1), (1, 3), (3, 12), (12, 10),                         (10, 2), (2, 15), (15, 0)], 550.5027000000001)
     Si el algoritmo no encuentra una trayectoria correcta retornará: shortest_path: ('placeholder', inf)

En la carpeta pruebas se encuentran dos archivos .txt los cuales muestran con que parámetros se hicieron las pruebas y su resultado para cada uno de los archivos SolomonPotvinBengio.

Por último el documento PDF con la descripcion detallada del algoritmo y/o heurıstica implementada. Describe el problema, las estrategias de la solucion, el estado del arte y los resultados con respecto a los casos de prueba.

# Sistemas Distribuidos - Laboratorio semestral

## Integrantes:
- Luis Aguilar 
- Gabriel Venegas

## Análisis y diseño de la arquitectura

![Untitled Diagram](https://user-images.githubusercontent.com/19898908/60762078-89582480-a025-11e9-8b5b-e7913a3dfe25.png)

La arquitectura diseñada como se puede ver en la imagen, en ella se tiene 4 componentes principales:
- FrontEnd: encargado de la interacción con el usuario. Este fue desarrollado en Python con el framework Django.
- Haproxy: Actúa tanto como enrutador y balanceador, es decir los clientes que ingresan al frontend y hacen una consulta es el HAproxy quien los redirige a alguno de servidores de backend para ser respondida su consulta. Para el caso de este laboratorio se utilizó un frontend y 3 servidores de backend.
- Servidores Backend: Son los responsable de servir las consultas mediante una api rest. En este caso los servidores de backend son en NodeJS.
- Base de datos: En la base de datos se encuentran los datos utilizados para este laboratorio. La BD elegida fue postgres, además esta se replicó para cada servidor y particiono para realizar consultas en paralelo en BD.
## Análisis del rendimiento de la arquitectura
![8conex](https://user-images.githubusercontent.com/19898908/60762844-39358e00-a036-11e9-9310-5e98bc7dbaac.PNG)
![14conex](https://user-images.githubusercontent.com/19898908/60762902-1e174e00-a037-11e9-968d-1cbea78c0b08.PNG)
![21conex](https://user-images.githubusercontent.com/19898908/60762852-566a5c80-a036-11e9-8de4-18d4006514fb.PNG)
![38conex](https://user-images.githubusercontent.com/19898908/60762854-5ff3c480-a036-11e9-905c-a5ad2a0dccd6.PNG)

| Cantidad de conexiones | Tiempo de respuesta |
|------------------------|---------------------|
| 8                      | 281 ms              |
| 14                     | 343 ms              |
| 21                     | 360 ms              |
| 38                     | 474 ms              |

Como se puede ver de las imagenes y el cuadro resumen a medida que se agregan conexiones a los servidores el tiempo de respuesta va en aumento este se puede ver más claramente en el gráfico a continuación.
![grafico_conex_time](https://user-images.githubusercontent.com/19898908/60762985-cc6fc300-a038-11e9-8f3a-5d304a51811e.PNG)

## Análisis sobre tolerancia a fallas y disponibilidad por parte del sistema
La tolerancia a fallos se define como "la propiedad que le permite a un sistema seguir funcionando correctamente en caso de fallo de uno o varios de sus componentes"([Wikipedia](https://es.wikipedia.org/wiki/Diseño_de_tolerancia_a_fallos#Criterios)). Esta arquitectura posee una gran toleracia a fallos ya que al contar con más de un servidor y, un proxy y balanceador de carga como lo es HAProxy, el cual elige el servidor menos cargado en el sistema. Permite además en caso de falla de alguno de ellos, detectada al momento de hacer la petición que si no es respondida luego de 5 segundos, direccionar a alguno que esté disponible. Provee por ende una alta disponibilidad en el sistema.

## Selección del servidor o/y enrutamiento de la consulta realizada por el cliente en base a una métrica

## Paralelización de la consulta

## Análisis de la distribución de la base de datos

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
![grafico_conex_time](https://user-images.githubusercontent.com/19898908/60763317-b9acbc80-a03f-11e9-891e-be73327b39f6.PNG)

Los tiempos de respuesta mejorarían sustancialmente si se añadiera un cache en los servidores antes de ir a BD, si agregamos cache a la arquitectura presentada anteriormente se vería como la siguiente imagen.

![Untitled Diagram](https://user-images.githubusercontent.com/19898908/60763191-16f33e80-a03d-11e9-9c7d-ec8eaad8dcc5.png)

## Análisis sobre tolerancia a fallas y disponibilidad por parte del sistema
La tolerancia a fallos se define como "la propiedad que le permite a un sistema seguir funcionando correctamente en caso de fallo de uno o varios de sus componentes"([Wikipedia](https://es.wikipedia.org/wiki/Diseño_de_tolerancia_a_fallos#Criterios)). Esta arquitectura posee una gran toleracia a fallos ya que al contar con más de un servidor y, un proxy y balanceador de carga como lo es HAProxy, el cual elige el servidor menos cargado en el sistema. Permite además en caso de falla de alguno de ellos, detectada al momento de hacer la petición que si no es respondida luego de 5 segundos, direccionar a alguno que esté disponible. Provee por ende una alta disponibilidad en el sistema.

## Selección del servidor o/y enrutamiento de la consulta realizada por el cliente en base a una métrica
La selección del servidor y enrutamiento está a cargo de HAProxy quien cumple la característica de ser un enrutador y balanceador de carga. En este caso la métrica que se escogió para seleccionar un servidor es el de menor conexiones, se escogió esta métrica dado que los 3 servidores de backend poseen las mismas características, por lo cual una métrica de rendimiento para los 3 servidores eran muy similares considerando el tiempo de respuesta de cada uno de ellos.

## Paralelización de la consulta
La paralelización  de la consulta a nivel de servidores se da ya que se pueden realizar  varias consultas en paralelo según la cantidad de servidores dispuestos, esto quiere decir que se pueden resolver varias consultas al mismo tiempo sin interferencia de una con otra.
Para el caso de la consulta a nivel de base datos, se utilizó postgres para distribuir la base de datos en otras 3 bases de datos, en postgres llamadas particiones, entonces de este modo las consultas se hace en paralelo en estas 3 particiones con lo cual disminuye los tiempos de procesamiento de la base de datos.

## Análisis de la distribución de la base de datos



## Refencias
- Partitioning Improvements in PostgreSQL 11: 

https://www.2ndquadrant.com/en/blog/partitioning-improvements-pg11/

- Configuring Load Balancer with HAProxy and Node.js:

https://www.webcodegeeks.com/javascript/node-js/configuring-load-balancer-with-haproxy-and-node-js/

- Building a NodeJS web server with HAProxy and Let’s Encrypt on Debian Stretch:

https://codeburst.io/building-a-nodejs-web-server-with-haproxy-and-lets-encrypt-on-debian-stretch-2fbf16cfba3a

- How to Set Up HAProxy for Load Balancing on Ubuntu 16.04:

https://dzone.com/articles/how-to-setup-haproxy-for-load-balancing-on-ubuntu

- How to Use HAProxy for Load Balancing: 

https://www.linode.com/docs/uptime/loadbalancing/how-to-use-haproxy-for-load-balancing/

- Bases de datos distribuidas en PostgresSQL:

http://www.v-espino.com/~chema/daw1/tutoriales/postgres/distribuidas.htm

- Setting up a RESTful API with Node.js and PostgreSQL:

https://blog.logrocket.com/setting-up-a-restful-api-with-node-js-and-postgresql-d96d6fc892d8/

- How to Configure HAProxy as a Proxy and Load Balancer: 

https://dzone.com/articles/how-to-configure-ha-proxy-as-a-proxy-and-loadbalan

- Tutorial Básico node.js: Cómo Configurar un Servidor HTTP:

https://www.luisllamas.es/tutorial-nodejs-montar-servidor/

- Dataset:"350 000+ movies from themoviedb.org":

https://www.kaggle.com/stephanerappeneau/350-000-movies-from-themoviedborg?fbclid=IwAR1-mnc_dLpuk9ZhKnpbdbRc-2YyeJs7dv4qf8H2GyPSx38c7e2WU9X25NM#220k_awards_by_directors.csv

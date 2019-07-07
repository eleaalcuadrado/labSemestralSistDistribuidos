# Sistemas Distribuidos - Laboratorio semestral

## Integrantes:
- Luis Aguilar 
- Gabriel Venegas

## Análisis y diseño de la arquitectura

![Untitled Diagram](https://user-images.githubusercontent.com/19898908/60762078-89582480-a025-11e9-8b5b-e7913a3dfe25.png)

## Análisis del rendimiento de la arquitectura

## Análisis sobre tolerancia a fallas y disponibilidad por parte del sistema
La tolerancia a fallos se define como "la propiedad que le permite a un sistema seguir funcionando correctamente en caso de fallo de uno o varios de sus componentes"([Wikipedia](https://es.wikipedia.org/wiki/Diseño_de_tolerancia_a_fallos#Criterios)). Esta arquitectura posee una gran toleracia a fallos ya que al contar con más de un servidor y, un proxy y balanceador de carga como lo es HAProxy, el cual elige el servidor menos cargado en el sistema, permite además en caso de falla de algun servidor, direccionar a alguno que esté disponible. Provee por ende una alta disponibilidad en el sistema.

## Selección del servidor o/y enrutamiento de la consulta realizada por el cliente en base a una métrica

## Paralelización de la consulta

## Análisis de la distribución de la base de datos

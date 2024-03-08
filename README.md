# Introducción

Este proyecto se enfoca en construir un sistema de intercambio de archivos P2P que opera en un marco distribuido y descentralizado. Se compone de nodos, cada uno con dos componentes principales: un módulo Servidor y un módulo Cliente, acompañados por una interfaz de consola. Esta interfaz será el medio a través del cual los usuarios podrán subir y acceder a archivos. Para asegurar una comunicación efectiva dentro de este entorno distribuido, se integrarán tecnologías como API REST, gRPC y Middleware MOM. Además, el sistema emplea AWS EC2 para el despliegue de los nodos, facilitando así la simulación y funcionamiento del sistema descentralizado.

## Servicios del sistema

El diseño del sistema P2P se articula en torno a dos módulos esenciales, cada uno con funciones diferenciadas:

### Módulo Servidor (PServidor):

- **Servicios de Listado de Archivos:** Proporciona una lista detallada de los archivos en cada nodo, junto con sus URI/URL, ajustados al directorio definido en la configuración.
- **Servicios de Concurrencia:** Facilita la comunicación simultánea con varios procesos remotos.
- **Servicios de Consultas de Recursos:** Permite realizar consultas sobre los archivos que cada nodo alberga.

### Módulo Cliente (PCliente):

- **Servicios ECO o DUMMY:** Introduce servicios simulados para la carga y descarga de archivos, a la espera de la implementación futura de transferencia real.
- **Interfaz de Cliente en Consola:** Brinda una interfaz accesible para que los usuarios puedan compartir y buscar archivos eficazmente.

## Interacción con componentes

El diseño del sistema P2P se articula en torno a dos módulos esenciales, cada uno con funciones diferenciadas:

### Módulo Servidor:

- **Servicios de Listado de Archivos:** Proporciona una lista detallada de los archivos en cada nodo, junto con sus URI/URL, ajustados al directorio definido en la configuración.
- **Servicios de Concurrencia:** Facilita la comunicación simultánea con varios procesos remotos.
- **Servicios de Consultas de Recursos:** Permite realizar consultas sobre los archivos que cada nodo alberga.

### Módulo Cliente:

- **Servicios ECO o DUMMY:** Introduce servicios simulados para la carga y descarga de archivos, a la espera de la implementación futura de transferencia real.
- **Interfaz de Cliente en Consola:** Brinda una interfaz accesible para que los usuarios puedan compartir y buscar archivos eficazmente.

## Arquitectura del sistema

![Reto1-Arquitectura-Telemática](https://github.com/dgonzalezi/dgonzalezi-st0263/assets/84990769/0897c7b6-6975-4289-9ccf-097f4b155937)


## Plan de desarrollo

![Reto1-Plan de Desarrollo-Telemática](https://github.com/dgonzalezi/dgonzalezi-st0263/assets/84990769/204670b5-ba50-43be-8a04-73f996a93776)


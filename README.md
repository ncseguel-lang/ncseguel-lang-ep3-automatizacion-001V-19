# EP3 - Automatización de Infraestructura de Red

## 1. Objetivo

Implementar un proceso de automatización para un router Cisco IOS-XE utilizando Ansible, NETCONF y RESTCONF, validando posteriormente el estado de la configuración mediante herramientas de automatización y generando evidencias de cumplimiento.

## 2. Alcance

El proyecto considera la automatización de un router Cisco CSR1000v, aplicando configuraciones corporativas, respaldando la configuración inicial y validando posteriormente los cambios mediante NETCONF y RESTCONF.

## 3. Infraestructura

* Cisco CSR1000v
* DEVASC VM
* Ubuntu Linux
* Git y GitHub

## 4. Tecnologías utilizadas

* Python 3
* Ansible
* pyATS / Genie
* NETCONF
* RESTCONF
* SSH
* Git

## 5. Configuración aplicada

Durante el desarrollo se realizaron las siguientes tareas:

* Respaldo de la configuración inicial.
* Configuración del hostname corporativo.
* Configuración del servidor NTP.
* Configuración de la interfaz Loopback10.
* Configuración de la descripción WAN.
* Habilitación de NETCONF.
* Habilitación de RESTCONF.
* Habilitación de los servicios HTTP y HTTPS.

## 6. Resultados obtenidos

Se validó correctamente la configuración mediante NETCONF y RESTCONF.

Las verificaciones confirmaron:

* Hostname corporativo.
* Interfaz Loopback10.
* Dirección IP de la Loopback.
* Servidor NTP.
* Descripción WAN.

Todas las validaciones finalizaron con resultado **CONFORME**.

## 7. Conclusiones

La automatización permitió implementar y verificar la configuración del router de forma consistente utilizando Ansible, NETCONF y RESTCONF. Las herramientas facilitaron la validación del estado del dispositivo y demostraron la importancia de la automatización para la administración de infraestructura de red.

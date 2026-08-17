---
title: "Test Tema 04: Redes Locales LAN, Switching, VLANs 802.1Q, DHCP y DNS"
type: "test"
target: "wiki/sources/bloque4-tema04-redes-lan-dhcp-dns.md"
date: "2026-08-18"
score: ""
tags:
  - test
  - examen-interactivo
  - simulador
created: "2026-08-18"
updated: "2026-08-18"
---

# 🔴 Test Tema 04: Redes Locales LAN, Switching, VLANs 802.1Q, DHCP y DNS

> [!info] 🎯 **Simulador Interactivo de Examen (Motor Nativo)**
> Selecciona las opciones que consideres correctas y pulsa el botón **"✅ Corregir Examen"** al final para calcular tu nota oficial (Acierto: $+1.0$ \| Fallo: $-0.33$) con corrección visual verde/rojo y justificaciones.

```tai-quiz
{
  "title": "Test Tema 04: Redes Locales LAN, Switching, VLANs 802.1Q, DHCP y DNS",
  "questions": [
    {
      "question": "¿Qué estándar del IEEE define el etiquetado de tramas Ethernet para la creación y transporte de VLANs troncales (*Trunking*) añadiendo una etiqueta de 4 bytes a la cabecera?",
      "options": [
        "IEEE 802.1D",
        "IEEE 802.1Q",
        "IEEE 802.3ad",
        "IEEE 802.1X"
      ],
      "answer": "b",
      "explanation": "IEEE 802.1Q inserta una etiqueta (Tag) de 4 bytes con el VLAN ID (12 bits, hasta 4094 VLANs) en la trama Ethernet."
    },
    {
      "question": "¿Qué protocolo de capa de enlace previene la formación de bucles infinitos en topologías de red con switches y enlaces redundantes desactivando puertos en bucle?",
      "options": [
        "STP (Spanning Tree Protocol - IEEE 802.1D).",
        "LACP (Link Aggregation Control Protocol).",
        "ARP (Address Resolution Protocol).",
        "CDP (Cisco Discovery Protocol)."
      ],
      "answer": "a",
      "explanation": "STP (Spanning Tree Protocol) bloquea enlaces redundantes para evitar tormentas de difusión (*broadcast storms*) y bucles de conmutación."
    },
    {
      "question": "En el protocolo DHCP (Dynamic Host Configuration Protocol), ¿cuál es la secuencia cronológica exacta de los 4 mensajes intercambiados entre cliente y servidor (proceso DORA)?",
      "options": [
        "DHCPREQUEST $\rightarrow$ DHCPOFFER $\rightarrow$ DHCPDISCOVER $\rightarrow$ DHCPACK",
        "DHCPDISCOVER $\rightarrow$ DHCPOFFER $\rightarrow$ DHCPREQUEST $\rightarrow$ DHCPACK",
        "DHCPINFORM $\rightarrow$ DHCPOFFER $\rightarrow$ DHCPREQUEST $\rightarrow$ DHCPRELEASE",
        "DHCPSOLICIT $\rightarrow$ DHCPADVERTISE $\rightarrow$ DHCPREQUEST $\rightarrow$ DHCPREPLY"
      ],
      "answer": "b",
      "explanation": "Proceso **DORA**: **D**iscover (cliente broadcast) $\rightarrow$ **O**ffer (servidor unicast/broadcast) $\rightarrow$ **R**equest (cliente broadcast) $\rightarrow$ **A**ck (servidor)."
    },
    {
      "question": "En el sistema de nombres de dominio DNS, ¿qué tipo de registro se utiliza para definir un alias o nombre canónico que apunta a otro nombre de dominio?",
      "options": [
        "Registro A.",
        "Registro CNAME.",
        "Registro MX.",
        "Registro PTR."
      ],
      "answer": "b",
      "explanation": "CNAME (Canonical Name) mapea un alias a su nombre canónico verdadero (ej. `www.ejemplo.es` $\rightarrow$ `ejemplo.es`)."
    },
    {
      "question": "¿Qué tipo de registro DNS permite la resolución inversa (obtener el nombre de dominio a partir de una dirección IP)?",
      "options": [
        "Registro NS.",
        "Registro TXT.",
        "Registro PTR (Pointer).",
        "Registro SOA."
      ],
      "answer": "c",
      "explanation": "El registro PTR en la zona `in-addr.arpa` (IPv4) o `ip6.arpa` (IPv6) realiza la resolución inversa IP $\rightarrow$ Nombre."
    }
  ]
}
```

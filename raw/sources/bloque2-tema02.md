---
title: "Bloque 2 - Tema 02: Periféricos, Conectividad e Interfaces de Comunicación"
type: "raw-source"
topic: "perifericos-conectividad"
date: "2026-08-17"
---

# Bloque 2 - Tema 02: Periféricos: Tipos, Controladores y Puertos de Conectividad (USB, PCIe, NVMe, Thunderbolt)

## 1. Clasificación de Periféricos
- **Periféricos de Entrada**: Teclado, ratón, escáner, tableta digitalizadora, lectores ópticos/biométricos, micrófonos, cámaras web.
- **Periféricos de Salida**: Monitores (tecnologías IPS, OLED, MiniLED, frecuencias de refresco), impresoras (láser electrofotográfico, inyección de tinta piezoeléctrica/térmica, 3D), altavoces.
- **Periféricos de Entrada/Salida (Mixtos)**: Pantallas táctiles, unidades de almacenamiento masivo extraíbles, tarjetas de red (NIC Ethernet, Wi-Fi), módems, gafas de realidad virtual.

## 2. Mecanismos de Transferencia de E/S con la CPU
1. **E/S Programada (Polling / Encuesta)**: La CPU comprueba periódicamente mediante un bucle de software el estado del controlador de periférico. Desperdicia tiempo de CPU (*busy waiting*).
2. **E/S Controlada por Interrupciones (Interrupt-driven I/O)**: El dispositivo periférico genera una señal física de interrupción (**IRQ**) cuando está listo para transferir datos. La CPU suspende la ejecución del programa actual, guarda el contexto y ejecuta la **Rutina de Servicio de Interrupción (ISR)**.
3. **Acceso Directo a Memoria (DMA - Direct Memory Access)**: Un controlador especializado de DMA transfiere bloques enteros de datos directamente entre el periférico y la memoria principal sin pasar por los registros de la CPU. La CPU solo interviene al inicio (configurando dirección origen, destino y longitud) y al final cuando el DMA emite una interrupción de finalización.

## 3. Puertos e Interfaces de Conectividad de Alta Velocidad

### Estándar USB (Universal Serial Bus)
Bus serie diferencial punto a punto con topología en árbol estratificado (hasta 127 dispositivos mediante concentradores/hubs y 5 niveles de cascada).
- **USB 1.1**: Low-Speed (1.5 Mbps) y Full-Speed (12 Mbps).
- **USB 2.0 (High-Speed)**: Tasa bruta de **480 Mbps** (60 MB/s teóricos, ~40 MB/s reales). Conectores Tipo A, Tipo B, Mini-USB y Micro-USB.
- **USB 3.0 / USB 3.1 Gen 1 / USB 3.2 Gen 1 (SuperSpeed)**: **5 Gbps** (codificación 8b/10b, ~500 MB/s). Color azul característico en conector Tipo-A.
- **USB 3.1 Gen 2 / USB 3.2 Gen 2 (SuperSpeed+)**: **10 Gbps** (codificación 128b/132b, ~1.2 GB/s).
- **USB 3.2 Gen 2x2**: **20 Gbps** (utiliza dos pares diferenciales en conector USB Type-C).
- **USB4 (basado en Thunderbolt 3)**:
  - **USB4 Gen 2x2**: 20 Gbps.
  - **USB4 Gen 3x2**: **40 Gbps**.
  - **USB4 2.0**: Hasta **80 Gbps** bidireccional y 120 Gbps asimétrico.
- **USB Type-C**: Conector reversible de 24 pines que soporta transmisión de datos, modos alternativos (DisplayPort Alt Mode, Thunderbolt) y alimentación eléctrica **USB Power Delivery (USB-PD)** de hasta **240W (48V / 5A en EPR)**.

### Thunderbolt (Intel / Apple)
Tecnología de comunicación serie que multiplexa paquetes **PCI Express** y **DisplayPort** sobre un único cable.
- **Thunderbolt 1**: 10 Gbps por canal (2 canales, 20 Gbps total). Conector Mini DisplayPort.
- **Thunderbolt 2**: 20 Gbps agregado.
- **Thunderbolt 3**: **40 Gbps**, utiliza conector USB Type-C y proporciona alimentación USB-PD.
- **Thunderbolt 4**: 40 Gbps garantizados, soporte para dos pantallas 4K o una 8K y PCIe a 32 Gbps mínimo.

### PCI Express (PCIe)
Arquitectura de bus serie punto a punto con canales dúplex dedicados denominados **líneas (lanes: x1, x2, x4, x8, x16)**.
- **PCIe 3.0**: 8 GT/s por línea (codificación 128b/130b) $pprox$ **985 MB/s por línea** (~15.75 GB/s en ranura x16).
- **PCIe 4.0**: 16 GT/s por línea $pprox$ **1.969 GB/s por línea** (~31.5 GB/s en ranura x16).
- **PCIe 5.0**: 32 GT/s por línea $pprox$ **3.938 GB/s por línea** (~63 GB/s en ranura x16).
- **PCIe 6.0**: 64 GT/s utilizando modulación multinivel **PAM4** $pprox$ **7.877 GB/s por línea**.

### NVMe (Non-Volatile Memory Express) vs SATA
- **SATA III (Serial ATA Revision 3.0)**: Diseñado para discos mecánicos, protocolo AHCI, velocidad máxima teórica de **6 Gbps (600 MB/s)**, 1 cola de comandos con profundidad máxima de 32 comandos.
- **NVMe**: Protocolo optimizado diseñado específicamente para almacenamiento en estado sólido Flash no volátil conectado directamente sobre el bus **PCI Express**. Admite hasta **64.000 colas de comandos**, cada una con una profundidad de hasta **64.000 comandos simultáneos**, con paralelismo masivo multicore y mínimas latencias. Formatos físicos: M.2 (2280), U.2, E1.S / E3.

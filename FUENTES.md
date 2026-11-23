# FUENTES.md — Declaración de fuentes e inteligencia artificial

**Proyecto:** Detector de humedad del suelo, TEI201, Arduino Leonardo. Actualización documentada el **22 de noviembre de 2026**. Esta declaración cubre los archivos añadidos o modificados en la actualización y señala lo que debe confirmar el equipo sobre materiales previos.

## 1. Librerías y herramientas utilizadas

| Dependencia / herramienta | Versión declarada | Uso | Fuente |
|---|---|---|---|
| Arduino AVR Boards (core) | La instalada por el equipo; confirmar versión | Compilar firmware Leonardo, Serial, analogRead, analogWrite, map y constrain | https://github.com/arduino/ArduinoCore-avr |
| Arduino IDE | La instalada por el equipo; confirmar versión | Cargar el firmware | https://www.arduino.cc/en/software |
| Python | 3.10+ | Ejecutar registrador y panel local | https://www.python.org/ |
| pyserial | 3.5 o posterior, menor a 4 | Leer USB serial y enumerar puertos | https://pyserial.readthedocs.io/ |
| Streamlit | 1.37 o posterior, menor a 2 | Dashboard con actualización periódica | https://docs.streamlit.io/ |
| pandas | 2.1 o posterior, menor a 3 | Leer y analizar CSV histórico | https://pandas.pydata.org/ |
| OpenSCAD | Versión instalada por el equipo; confirmar | Diseño paramétrico y generación de STL | https://openscad.org/ |

El firmware **no incluye librerías Arduino de terceros**. Las versiones exactas de Python se resuelven mediante **software/dashboard/requirements.txt**; antes de presentar, el equipo debería guardar las versiones instaladas mediante **python -m pip freeze** y comprobar su funcionamiento.

## 2. Código externo y referencias consultadas

- **Firmware Leonardo:** partimos del código de nuestro proyecto, con los pines D9/D10/D11 y la calibración 892/350. Lo adaptamos para utilizar solamente los tres colores finales: rojo (0–19 %), verde (20–39 %) y azul (40–100 %).
- **Ejemplo académico de organización:** https://github.com/jgarcia-dec/sensor-calidad-suelo-TEI201 . Se revisó como ejemplo de secciones de README, FUENTES, carpetas y requisitos de la pauta; **no se trasladaron mediciones, componentes ni resultados** de ese proyecto.
- **Documentación de la API Arduino:** https://docs.arduino.cc/language-reference/ ; funciones de lectura analógica, salida PWM y comunicación serial.
- **Documentación de pyserial:** https://pyserial.readthedocs.io/en/latest/shortintro.html ; lectura de líneas desde puerto serie.
- **Documentación de Streamlit:** https://docs.streamlit.io/develop/api-reference ; interfaz, indicadores, gráficas y actualización.
- **Diseño CAD histórico:** la primera versión del archivo OpenSCAD ya estaba en el repositorio antes de esta actualización. **Pendiente de confirmación del equipo:** origen y autoría de ese archivo, y de los modelos STL, documentación e informe anteriores.

No se debe completar esta sección inventando autores, fechas, versiones ni fuentes; el equipo debe revisar si empleó ejemplos adicionales no reflejados aquí.

## 3. Uso de inteligencia artificial (obligatorio)

### Revisión de repositorio y documentación — 22/11/2026
- **Herramienta:** ChatGPT (OpenAI, GPT-6).
- **Solicitud del equipo:** revisar el repositorio existente y el ejemplo TEI201; adaptarlo a Arduino Leonardo sin protoboard, incorporar el firmware proporcionado y dejar documentados los entregables de la pauta Avance 3.
- **Archivos asistidos:** README.md, FUENTES.md, guías de hardware, BOM de revisión, esquema explicativo, protocolo y checklist de entrega.
- **Adaptación:** se sustituyeron las referencias obsoletas a Arduino UNO y la calibración previa, se distinguieron hechos fotografiados de conexiones no verificadas y cambiamos el programa para mantener únicamente los tres colores que usamos en el prototipo.
- **Comprensión esperada:** debemos poder explicar la cadena sensor → Leonardo → USB serial → CSV → dashboard, y por qué los umbrales son relativos.

### Registro de datos, dashboard y pruebas de parser — 22/11/2026
- **Herramienta:** ChatGPT (OpenAI, GPT-6).
- **Código generado:** software/dashboard/lector_serial.py, software/dashboard/panel.py y testing/test_parser.py.
- **Función:** interpretar las líneas seriales emitidas por el firmware suministrado, guardar mediciones reales con marca temporal en CSV, mostrar histórico/indicadores en una aplicación local y verificar que el parser rechaza líneas inválidas.
- **Adaptación:** adaptamos el parser a los tres estados del código Leonardo; las pruebas unitarias usan líneas sintéticas exclusivamente para validar el código y **no se presentan como datos ambientales reales**.
- **Limitación:** la creación del código no equivale a una demostración del funcionamiento del puerto ni del sensor. Deben comprobarlo con el montaje físico.

### Archivos CAD y planos
- **Herramienta:** ChatGPT (OpenAI, GPT-6), para adaptación o documentación de la versión Leonardo si corresponde.
- **Comprensión:** comprobar dimensiones exteriores, soporte de la placa, taladros, puerto USB, acceso a conexiones y que los archivos STL correspondan a la versión efectivamente instalada.
- **Advertencia:** un STL o archivo OpenSCAD no equivale a un ensamble nativo validado en Fusion 360 (.f3d/.f3z).

## 4. Verificación académica pendiente

Antes de enviar, debemos comprobar que todos comprendemos el código y completar nombres, versiones efectivamente instaladas, fuentes externas adicionales y datos reales de ensayo. El empleo de IA se declara expresamente y no implica que la IA haya realizado pruebas físicas.

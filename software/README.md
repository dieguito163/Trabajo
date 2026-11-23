# Software

Nuestro [programa Arduino](../firmware/detector_humedad/detector_humedad.ino) lee el sensor capacitivo conectado a A0, calcula el índice de humedad y controla el LED RGB con los pines D9, D10 y D11. Utilizamos los estados rojo, verde y azul.

También preparamos un [registrador serial y dashboard](dashboard/README.md) para guardar y visualizar las lecturas desde un computador conectado por USB.

La [calibración y los umbrales](docs/README.md) están explicados en la documentación del sensor. Las dependencias utilizadas se encuentran en [FUENTES.md](../FUENTES.md).

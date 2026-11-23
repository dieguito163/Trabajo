# Hardware | versión actual sin protoboard

## Configuración del prototipo fotografiado

Nuestro dispositivo incluye una **carcasa blanca impresa en 3D**, fijada con tornillos y con el sensor capacitivo externo conectado mediante un cable. La tapa tiene un LED visible. Reemplazamos la placa por un **Arduino Leonardo** y **eliminamos la protoboard**.

Las fotografías exteriores muestran la existencia de la carcasa, la sonda y las fijaciones, pero **no muestran con suficiente detalle** el cableado interno, la orientación del LED ni todos los conectores. Necesitamos revisar las conexiones reales antes de afirmar que el circuito está validado.

## Justificación de componentes

| Componente | Justificación y compatibilidad | Limitación por verificar |
|---|---|---|
| Arduino Leonardo (ATmega32u4) | 1 entrada analógica A0 y tres salidas PWM D9/D10/D11; puerto USB serial para registro local | Alimentación y montaje exactos |
| Sensor capacitivo de humedad | Mide variaciones eléctricas asociadas al entorno de la sonda, con salida analógica | Calibración por tipo de suelo; no equivale directamente a contenido volumétrico |
| LED RGB | Expresa tres estados de humedad sin pantalla adicional | Confirmar ánodo/cátodo, resistencias y cableado |
| Carcasa 3D con tornillos | Aísla la electrónica del contacto accidental y permite retirar la tapa | No es impermeable; comprobar tolerancias |
| Conexiones directas | Reduce volumen al eliminar la protoboard | Deben fijarse y aislarse para evitar cortes y cortocircuitos |
| USB de datos | Alimenta y comunica la placa con el PC | El dashboard solo está disponible con PC conectado |

**Diseño para reparación:** desconectar USB, retirar los tornillos de la tapa y acceder a placa, cableado y módulo LED sin destruir la carcasa. En la presentación debemos abrir la tapa y mostrar que podemos acceder a los componentes.

## Entregables

- [Esquema funcional Leonardo](esquemas/esquema_leonardo.svg) y [tabla de conexiones](esquemas/README.md).
- [BOM actualizada](bom/BOM_leonardo.csv); **los precios unitarios reales siguen pendientes de confirmación**.
- [Fotografías](fotos/README.md) del prototipo ensamblado.
- [Protocolo de pruebas](../testing/protocolo_leonardo.md).

No conectar directamente un LED discreto a los pines sin resistencias limitadoras. Si el módulo posee resistencias integradas, comprobarlo en la placa o datasheet.

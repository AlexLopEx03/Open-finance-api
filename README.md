<!-- ![EN](https://flagcdn.com/w20/gb.png) [English version](https://github.com/AlexLopEx03/Open-finance-api/blob/main/README.en.md) of this readme -->

<div align="center">
  <h1>open-finance-api</h1>
</div>

Servicio de API pública de finanzas que proporciona datos de acciones, criptomonedas y apuestas.

Los datos se pueden consumir en tres formatos: JSON, HTML y SVG, personalizables y dinámicos mediante parámetros en la URL.

<br>

***Proyecto personal de código abierto por AlexLopEx03 bajo licencia AGPLv3.0*** 📜

<br>

<div align="center">
  
| Python | Django |
|:------:|:------:|
| <img src="https://upload.wikimedia.org/wikipedia/commons/c/c3/Python-logo-notext.svg" width="100"/> | <img src="https://www.svgrepo.com/show/353657/django-icon.svg" width="100"/> |

</div>

---

> [!WARNING]
>
> El proyecto se encuentra en una etapa temprana y aún está incompleto.
>
> Actualmente solo están disponibles datos básicos de la sección de Acciones en bolsa. El objetivo es ofrecer respuestas altamente personalizables a través de la API y ampliar la cobertura de datos temáticos más allá de las tres secciones existentes.

---

## Guía de uso

La API se organiza en tres secciones principales, cada una accesible mediante la URL base seguida de su endpoint correspondiente:

```Bash
# URL base
https://open-finance-api.vercel.app
```

| Sección | Endpoint |
|:--------|:---------| 
| Acciones en bolsa | ```/stocks/``` |
| Criptomonedas | ```/crypto/``` |
| Apuestas | ```/bets/``` |

- Tras esto, se agrega un **path param** con el ticker de la entidad cuyos datos se quieren recibir. Por ejemplo, para el valor de la acción de Apple:

```Bash
https://open-finance-api.vercel.app/stocks/AAPL/
```

- Finalmente añadimos query params a la URL para personalizar la respuesta, aquí la lista completa:

| Parámetro | Descripción | Ejemplo | Valor por defecto |
|:---------:|:------------|:-------:|:-----------------:|
| format | Formato de respuesta de los datos | ```/stocks/TSLA/?format=html``` | json |
| start | Fecha desde la que se obtienen los datos | ```/stocks/TSLA/?start=2025-06-01``` | Fecha actual |
| end | Fecha hasta la que se obtienen los datos (No incluida) | ```/stocks/TSLA/?end=2025-07-15``` | Fecha actual |

---

- Ejemplos de uso:

<details>
  <summary>
    Formato de JSON devuelto por la API
  </summary>
  
  <br>

```Bash
https://open-finance-api.vercel.app/stocks/TSLA/?format=json&start=2025-10-01&end=2025-10-03
# Resultado:
{
  "2025-10-01": {
    Close: 459.46,
    High: 462.29,
    Low: 440.75,
    Open: 443.8,
    Volume: 98122300
  },
  "2025-10-02": {
    Close: 436,
    High: 470.75,
    Low: 435.57,
    Open: 470.54,
    Volume: 137009000
  }
}
```

</details>

<details>
<summary>
  Formato de imágen SVG provisional
</summary>
  
  <br>

```Bash
https://open-finance-api.vercel.app/stocks/TSLA/?format=svg
```

<div align="center">

<img src='https://open-finance-api.vercel.app/stocks/TSLA/?format=svg'/>

</div>

</details>

---

> [!NOTE]
>
> En caso de que no se devuelvan datos, es posible que el ticker no exista, sea incorrecto o alguno de los parámetros sea inválido, por ejemplo, si se usan fechas futuras.

---

<div align="center">
    
## Roadmap de desarrollo

| ⚙️ Características pendientes de implementar |
| :-----------------------------------------------------------------|
| Gestión agresiva del caché para optimización                      |
| Mecanismos de prevención de abusos, bloqueo de IP's               |
| Implementación de /cryptos y /bets en la API                      |
| Implementación de más query params y personalización              |

</div>

> [!IMPORTANT]
> 
> El proyecto está abierto a contribuciones, hay varias tareas pendientes que pueden necesitar de creatividad adicional para proponer y diseñar mejor la API.
>
> Puedes encontrar más detalles sobre contribuir al proyecto en el apartado de [Contributing](https://github.com/AlexLopEx03/Open-finance-api?tab=contributing-ov-file).

---

#### Cualquier duda, comentario, sugerencia o propuesta acerca del proyecto puedes dirigirte a la sección de Discussions.

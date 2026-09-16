# Quiz 3: Desarrollo Front-End, UX/A11y, JavaScript ES6+ y TypeScript Avanzado

**Curso:** IF0009 - Desarrollo de Software IV  
**Docente:** Mag. Jonathan Granados C.  
**Puntuación Total:** 25 Puntos  
**Tiempo Límite Recomendado:** 25 - 30 minutos  
**Instrucciones:** Lea detenidamente cada uno de los siguientes 5 casos prácticos y ejercicios de rastreo de código relacionados con la ingeniería de software front-end (Temas 4.1 a 4.3). Seleccione la opción de respuesta que considere correcta. Al finalizar la prueba, puede consultar el solucionario analítico ubicado al final del documento para verificar sus razonamientos técnicos.

---

## 📝 Cuestionario de Evaluación Práctica (< 30 Minutos)

### 1. Arquitectura Front-End y Optimización de Rendimiento (Core Web Vitals) (5 Puntos)

Un equipo de ingeniería de software migra un portal de comercio electrónico desde un esquema tradicional renderizado en servidor (SSR) hacia una aplicación de página única (SPA - *Single-Page Application*) en el cliente. Al auditar la aplicación con Google Lighthouse, observan que el indicador LCP (*Largest Contentful Paint*) empeoró significativamente debido a la descarga de un paquete JavaScript monolítico inicial, y además se generan saltos visuales molestos (*Cumulative Layout Shift - CLS*) al desplegar imágenes y datos asíncronos.

¿Cuál es la combinación de estrategias de arquitectura front-end y optimización de renderizado recomendada para resolver estos defectos de rendimiento?

- [ ] A) Desactivar las hojas de estilo CSS3 y reemplazar todos los componentes de la interfaz por gráficos SVG incrustados en línea dentro del evento `window.onload`.
- [ ] B) Aplicar división de código (*code-splitting*) y carga diferida (*lazy loading*) de rutas/módulos, reservar dimensiones explícitas (`width`/`height` o `aspect-ratio`) en elementos multimedia para evitar CLS, y optimizar el empaquetado eliminando código muerto (*tree-shaking*).
- [ ] C) Reemplazar la API Fetch cliente por peticiones síncronas `XMLHttpRequest` invocadas directamente en el hilo principal para bloquear el DOM hasta recibir todos los datos del servidor.
- [ ] D) Unificar todo el código JavaScript de la aplicación en un script global sin módulos usando declaraciones `var` para acelerar la interpretación del motor V8.

---

### 2. Accesibilidad Web (WCAG 2.1 AA) y Semántica WAI-ARIA (5 Puntos)

En una plataforma bancaria web, un desarrollador construye una ventana modal dinámico de confirmación de transferencia utilizando una etiqueta genérica `<div class="modal">` con estilos CSS. Los usuarios que navegan mediante teclado y lectores de pantalla (NVDA/VoiceOver) reportan tres fallas severas:
1. Al abrir el modal, el foco del teclado se queda atrapado en los elementos del fondo de la página.
2. El lector de pantalla no anuncia la apertura ni el contenido del diálogo de alerta.
3. El usuario puede seguir presionando `Tab` y activar accidentalmente botones ocultos detrás del modal.

¿Qué patrón de accesibilidad (WCAG 2.1 AA - Principios Operable y Robusto) soluciona de forma integral esta falla de interfaz?

- [ ] A) Incorporar `role="dialog"` y `aria-modal="true"` al contenedor del modal, transferir programáticamente el foco del teclado al primer elemento enfocable dentro del diálogo (`element.focus()`), implementar confinamiento de foco (*focus trap*), y utilizar una región viva `aria-live="assertive"` para los mensajes.
- [ ] B) Colocar el atributo `alt="modal-dialog"` en el `<div>` principal y deshabilitar los eventos del teclado del sistema operativo mediante JavaScript.
- [ ] C) Reemplazar la estructura HTML del modal por una imagen PNG estática renderizada con la captura del texto de confirmación.
- [ ] D) Asignar un valor `tabindex="100"` a todos los botones del fondo de la página para forzar al navegador a omitir su navegación por teclado.

---

### 3. Ejercicio de Rastreo de Código: Motor V8, Event Loop y Microtask Queue (5 Puntos)

Analice la siguiente secuencia de ejecución asíncrona en JavaScript moderno (ES6+):

```javascript
console.log("1. Inicio");

setTimeout(() => {
    console.log("2. Timer Macrotarea");
}, 0);

Promise.resolve().then(() => {
    console.log("3. Promesa Microtarea");
});

(async () => {
    await null;
    console.log("4. Async/Await Microtarea");
})();

console.log("5. Fin");
```

¿Cuál es el orden exacto de salida por consola producido al ejecutar este script en el navegador o motor Node.js?

- [ ] A) `1. Inicio` ➔ `5. Fin` ➔ `3. Promesa Microtarea` ➔ `4. Async/Await Microtarea` ➔ `2. Timer Macrotarea`
- [ ] B) `1. Inicio` ➔ `2. Timer Macrotarea` ➔ `3. Promesa Microtarea` ➔ `4. Async/Await Microtarea` ➔ `5. Fin`
- [ ] C) `1. Inicio` ➔ `5. Fin` ➔ `2. Timer Macrotarea` ➔ `3. Promesa Microtarea` ➔ `4. Async/Await Microtarea`
- [ ] D) `1. Inicio` ➔ `3. Promesa Microtarea` ➔ `4. Async/Await Microtarea` ➔ `2. Timer Macrotarea` ➔ `5. Fin`

---

### 4. Ejercicio de Rastreo de Código: Programación Funcional e Inmutabilidad de Arreglos (5 Puntos)

Un desarrollador debe procesar una lista de paquetes de envío representada en el siguiente arreglo de objetos:

```javascript
const paquetes = [
    { id: 'P1', pesoKg: 10, estado: 'ENTREGADO' },
    { id: 'P2', pesoKg: 25, estado: 'EN_TRANSITO' },
    { id: 'P3', pesoKg: 15, estado: 'ENTREGADO' },
    { id: 'P4', pesoKg: 5,  estado: 'CANCELADO' }
];

const totalPesoEntregado = paquetes
    .filter(p => p.estado === 'ENTREGADO')
    .map(p => p.pesoKg)
    .reduce((acum, peso) => acum + peso, 0);
```

¿Cuál es el valor final de la variable `totalPesoEntregado` y cuál es el impacto de esta operación sobre el arreglo original `paquetes`?

- [ ] A) Retorna `25` y modifica directamente el arreglo original `paquetes`, eliminando de la memoria los objetos cuyo estado no sea `'ENTREGADO'`.
- [ ] B) Retorna `25` (suma de 10 + 15) y mantiene el arreglo original `paquetes` completamente inalterado (inmutabilidad estricta), debido a que `filter` y `map` retornan nuevas instancias de arreglos en memoria.
- [ ] C) Retorna `55` porque el método `reduce` omite la condición del filtro y procesa el peso acumulado de los 4 elementos de la colección.
- [ ] D) Lanza un error de ejecución `TypeError` porque el valor inicial `0` en `reduce` no es válido cuando se procesan arreglos de objetos.

---

### 5. TypeScript Avanzado: Utility Types, Genéricos y Payload REST (5 Puntos)

Analice la siguiente declaración de modelos DTO en TypeScript para un módulo de gestión de envíos:

```typescript
export interface EnvioDto {
    id: number;
    trackingCode: string;
    pesoKg: number;
    destinatario: string;
    entregado: boolean;
}

export type ActualizarEnvioPayload = Partial<Omit<EnvioDto, 'id' | 'trackingCode'>>;
```

¿Qué propiedades conforman la estructura del tipo `ActualizarEnvioPayload` y para qué tipo de operación en una API RESTful está diseñado este patrón de tipo?

- [ ] A) Incluye únicamente las propiedades `{ id?: number; trackingCode?: string; }` en formato opcional y está diseñado para peticiones HTTP `DELETE`.
- [ ] B) Incluye las propiedades `{ pesoKg?: number; destinatario?: string; entregado?: boolean; }` totalmente opcionales, omitiendo las llaves inmutables `id` y `trackingCode`, diseñado para peticiones HTTP `PATCH` de actualización parcial.
- [ ] C) Convierte todas las propiedades de `EnvioDto` en campos de sólo lectura (`Readonly`) e inmutables para peticiones HTTP `POST`.
- [ ] D) Genera un error de compilación en `tsc` debido a que TypeScript prohíbe anidar Utility Types como `Partial` y `Omit`.

---

---

## 🎯 Solucionario Analítico y Justificaciones Pedagógicas

### Pregunta 1: Arquitectura Front-End y Optimización de Rendimiento (Core Web Vitals)
- **Respuesta Correcta:** **B**
- **Justificación Analítica:** 
  - En aplicaciones de página única (SPA), la carga inicial de un paquete JavaScript voluminoso retrasa el *Largest Contentful Paint* (LCP). La solución de ingeniería recomendada es implementar **división de código (*code-splitting*)** mediante `import()` dinámico, permitiendo descargar únicamente los módulos requeridos por la vista activa (*lazy loading*). Además, para eliminar el *Cumulative Layout Shift* (CLS) causado por elementos multimedia o asíncronos que cambian el tamaño del DOM repentinamente, se deben reservar explícitamente sus dimensiones en CSS (`aspect-ratio` o `width`/`height`), combinándolo con **tree-shaking** para eliminar código no utilizado durante la fase de compilación.
- **Análisis de Distractores:**
  - **A es incorrecta:** Desactivar CSS3 e insertar SVG inline en `onload` empeora las métricas de rendimiento y destruye la separación semántica del diseño.
  - **C es incorrecta:** Las peticiones síncronas `XMLHttpRequest` en el hilo principal congelan la interfaz de usuario (*Call Stack* bloqueado), degradando drásticamente el *Interaction to Next Paint* (INP) y la UX.
  - **D es incorrecta:** Evitar módulos y utilizar variables globales con `var` contamina el objeto global `window` y previene las optimizaciones de *tree-shaking* del empaquetador.

---

### Pregunta 2: Accesibilidad Web (WCAG 2.1 AA) y Semántica WAI-ARIA
- **Respuesta Correcta:** **A**
- **Justificación Analítica:** 
  - Para cumplir con el estándar WCAG 2.1 AA en componentes interactivos complejos (como modales/diálogos), se requiere semántica WAI-ARIA y gestión estricta del foco de teclado:
    1. **Semántica:** `role="dialog"` indica la naturaleza del componente y `aria-modal="true"` informa a la tecnología asistiva que el contenido exterior está inactivo.
    2. **Gestión de Foco:** Al abrir el modal, se debe transferir el foco al primer elemento interactivo (`element.focus()`) y atrapar la navegación `Tab` (*focus trap*) dentro del modal para evitar que el usuario acceda a controles del fondo.
    3. **Anuncios Asíncronos:** Las regiones vivas `aria-live="assertive"` notifican de inmediato al lector de pantalla sobre eventos críticos.
- **Análisis de Distractores:**
  - **B es incorrecta:** El atributo `alt` solo aplica para imágenes (`<img>`), no para diálogos `<div class="modal">`, y deshabilitar el teclado del SO es técnicamente imposible e inviable.
  - **C es incorrecta:** Usar imágenes PNG para texto viola el principio *Perceptible* de WCAG (no permite escalado de texto ni lectura clara por lectores de pantalla).
  - **D es incorrecta:** Asignar `tabindex` altos (como 100) es una mala práctica que altera el orden natural del DOM y destruye la experiencia de navegación por teclado.

---

### Pregunta 3: Ejercicio de Rastreo de Código: Motor V8, Event Loop y Microtask Queue
- **Respuesta Correcta:** **A**
- **Justificación Analítica:** 
  - El motor V8 ejecuta código siguiendo la arquitectura del **Event Loop**:
    1. **Ejecución Síncrona (Call Stack):** Imprime en orden secuencial `1. Inicio` y luego `5. Fin`.
    2. **Delegación de Asincronía:**
       - `setTimeout(..., 0)` registra su callback en la **Macrotask Queue (Task Queue)**.
       - `Promise.resolve().then(...)` registra su callback en la **Microtask Queue**.
       - La función `async` con `await null` suspende brevemente su ejecución y encola la reanudación como una **Microtarea**.
    3. **Vaciado de Colas:** Al vaciarse el *Call Stack*, el Event Loop atiende primero la **Microtask Queue** por tener prioridad absoluta sobre las macrotareas:
       - Ejecuta la promesa: `3. Promesa Microtarea`.
       - Ejecuta la continuación async: `4. Async/Await Microtarea`.
    4. **Macrotask Queue:** Finalmente procesa el temporizador: `2. Timer Macrotarea`.
- **Análisis de Distractores:**
  - **B es incorrecta:** Asume erróneamente una ejecución puramente secuencial síncrona ignorando la naturaleza no bloqueante del Event Loop.
  - **C es incorrecta:** Un temporizador `setTimeout` a 0ms no se ejecuta de inmediato; debe aguardar en la Macrotask Queue hasta que las microtareas pendientes hayan finalizado.
  - **D es incorrecta:** Las promesas no son bloqueantes y no impiden la ejecución de instrucciones síncronas posteriores como `console.log("5. Fin")`.

---

### Pregunta 4: Ejercicio de Rastreo de Código: Programación Funcional e Inmutabilidad de Arreglos
- **Respuesta Correcta:** **B**
- **Justificación Analítica:** 
  - El código aplica métodos de orden superior encadenados sobre el arreglo:
    1. `.filter(p => p.estado === 'ENTREGADO')`: Retorna un nuevo arreglo con 2 elementos: `{ id: 'P1', pesoKg: 10 }` y `{ id: 'P3', pesoKg: 15 }`.
    2. `.map(p => p.pesoKg)`: Transforma la colección en un nuevo arreglo de números: `[10, 15]`.
    3. `.reduce((acum, peso) => acum + peso, 0)`: Acumula `0 + 10 + 15 = 25`.
  - **Inmutabilidad:** Ninguno de los métodos (`filter`, `map`, `reduce`) muta el arreglo original `paquetes`. La colección original se mantiene 100% intacta en memoria.
- **Análisis de Distractores:**
  - **A es incorrecta:** Métodos como `filter` y `map` son puramente inmutables; no eliminan ni modifican los datos del arreglo fuente.
  - **C es incorrecta:** `reduce` no opera directamente sobre el arreglo original sino sobre la salida filtrada previa de 2 elementos (`[10, 15]`), sumando 25.
  - **D es incorrecta:** El valor inicial `0` en `reduce` es totalmente válido y necesario para acumular valores numéricos.

---

### Pregunta 5: TypeScript Avanzado: Utility Types, Genéricos y Payload REST
- **Respuesta Correcta:** **B**
- **Justificación Analítica:** 
  - Evaluando la composición de Utility Types:
    1. `Omit<EnvioDto, 'id' | 'trackingCode'>`: Elimina del tipo base las claves identificadoras `id` y `trackingCode`, dejando `{ pesoKg: number; destinatario: string; entregado: boolean; }`.
    2. `Partial<...>`: Mapea todas las propiedades resultantes convirtiéndolas en opcionales (`?`), resultando en:
       ```typescript
       {
           pesoKg?: number;
           destinatario?: string;
           entregado?: boolean;
       }
       ```
  - **Aplicación Arquitectónica REST:** En servicios web RESTful, el verbo **`PATCH`** realiza modificaciones parciales sobre un recurso donde el cliente solo envía las propiedades que desea cambiar. Excluir `id` y `trackingCode` garantiza que las claves inmutables de negocio no puedan ser alteradas en el payload.
- **Análisis de Distractores:**
  - **A es incorrecta:** Invierte el comportamiento de `Omit`; `Omit` remueve las llaves especificadas, no las conserva.
  - **C es incorrecta:** Para inmutabilidad de propiedades se utiliza el Utility Type `Readonly<T>`, no `Partial<T>`.
  - **D es incorrecta:** TypeScript permite y promueve la composición flexible de múltiples Utility Types incorporados.

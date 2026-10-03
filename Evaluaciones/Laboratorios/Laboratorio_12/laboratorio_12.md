![UCR Banner](../../../resources/images/UCR_Banner.png)

**UNIVERSIDAD DE COSTA RICA**  
**SEDE DEL ATLÁNTICO - RECINTO PARAÍSO**  
**CARRERA DE INFORMÁTICA EMPRESARIAL**  
**CURSO:** IF0009 - Desarrollo de Software IV  
**PROFESOR:** Mag. Jonathan Granados C.  
**SEMESTRE:** II-2026  

---

# Laboratorio 12: Proyecto Full-Stack Autónomo (Expansión TechConf)

## Resumen

Este laboratorio consiste en una evaluación práctica integral no guiada, 
diseñada para prepararle para su próximo examen. Construyendo sobre el 
sistema **TechConf** desarrollado en la Práctica 11 (a y b), usted 
deberá expandir la plataforma de forma autónoma integrando nuevas 
entidades relacionales en Spring Boot y formularios reactivos más 
complejos en Angular. 

---

## Metadatos del Laboratorio

*   **Tiempo estimado:** 4.0 horas.
*   **Herramientas requeridas:** Java 17+, Spring Boot, H2 Database, Angular CLI 18+, Git, GitHub.
*   **Metas de Aprendizaje:**
    1.  Implementar relaciones `@OneToMany` y `@ManyToOne` en Spring Data JPA con H2.
    2.  Diseñar formularios reactivos anidados (`FormGroup` dentro de `FormGroup`) y validar arreglos dinámicos en Angular.
    3.  Aplicar metodologías de control de versiones mediante Git y entrega de código vía GitHub.

---

## Parte 1: Especificaciones de Expansión del Sistema (Práctica Autónoma)

A diferencia de las prácticas anteriores, en este laboratorio usted deberá 
tomar decisiones de arquitectura e implementar las funcionalidades sin 
código base guiado. 

### Requerimientos de Back-End (Spring Boot)

1.  **Entidad `Asistente`:**
    
    Cree una nueva entidad llamada `Asistente` con los siguientes campos 
    obligatorios: id, nombre completo, correo electrónico y edad.

2.  **Relación Bidireccional (`@OneToMany` / `@ManyToOne`):**
    
    Una `Charla` puede tener múltiples `Asistente`s inscritos. Configure 
    la relación JPA adecuadamente para que al consultar una charla se 
    devuelva la lista de asistentes. Evite problemas de recursividad 
    infinita utilizando anotaciones como `@JsonIgnore`.

3.  **Actualización de `data.sql`:**
    
    Agregue las sentencias SQL necesarias para insertar al menos 5 
    asistentes distribuidos entre las diferentes charlas existentes en su 
    base de datos.

4.  **Endpoint REST Adicional:**
    
    Cree un nuevo endpoint `POST /api/charlas/{id}/asistentes` que reciba 
    el JSON de un asistente y lo vincule a la charla correspondiente.

### Requerimientos de Front-End (Angular con Reactive Forms)

1.  **Formulario Anidado de Inscripción:**
    
    En su interfaz de Angular, agregue un botón "Inscribir Asistente" en 
    cada tarjeta de la agenda. Este botón debe desplegar un nuevo 
    formulario reactivo.

2.  **Validaciones Requeridas:**
    
    El formulario de `Asistente` debe ser un `FormGroup` con:
    
    - [ ] `nombre`: Requerido, longitud mínima de 3 caracteres.
    - [ ] `correo`: Requerido, formato de email válido.
    - [ ] `edad`: Requerido, debe usar un **Validador Personalizado** 
          que verifique que el asistente es mayor de 18 años.

3.  **Consumo de la API:**
    
    Al enviar el formulario válido, invoque el servicio Angular para 
    realizar el `POST` al nuevo endpoint de su servidor y actualice la 
    tarjeta de la charla para mostrar el nuevo asistente.

---

## Parte 2: Análisis y Depuración de Errores

En el proceso de creación de relaciones bidireccionales y serialización 
JSON (Jackson), es sumamente común enfrentar el error de recursión infinita 
(`StackOverflowError`) o excepciones en los tipos soportados de HTTP.

Como parte integral de este laboratorio, usted debe documentar su proceso 
de depuración:

- [ ] Provoque intencionalmente un error de recursividad infinita 
      (removiendo las anotaciones de protección en su relación 
      bidireccional) e intente consultar las charlas mediante un GET.
- [ ] Capture un pantallazo del error (Stack Trace en consola o error 500 
      en el navegador) y guárdelo en su repositorio bajo la ruta 
      `docs/error_recursion.png`.
- [ ] Restaure la solución y documente en el archivo `README.md` de su 
      repositorio cuál fue el procedimiento exacto que aplicó para resolver 
      el problema y qué directivas de Jackson utilizó.

---

## Parte 3: Reto Autónomo y Entrega

Su objetivo final es integrar todos los componentes para que el usuario 
final tenga una experiencia fluida al registrar charlas y asistentes, 
validando todos los datos tanto en frontend como en backend.

### Rúbrica de Evaluación

| Criterio Técnico | Puntos | Detalles |
|---|---|---|
| **Persistencia y JPA** | 25 pts | Entidad Asistente, relación 1:N y script data.sql. |
| **Controlador REST** | 15 pts | Endpoint POST de asistentes implementado y funcional. |
| **Formularios Reactivos** | 30 pts | Formulario anidado con todas sus validaciones. |
| **Validador Custom** | 10 pts | Validador de edad (mayor a 18) implementado. |
| **Depuración** | 10 pts | Captura de error documentada en el README del repositorio. |
| **Control Versiones** | 10 pts | Historial de commits estructurado y entrega correcta. |
| **Total** | **100 pts** | Evaluación final del laboratorio. |

### Instrucciones de Entrega

1.  Inicialice un repositorio local de Git en la raíz de su proyecto.
2.  Realice commits atómicos y descriptivos a medida que avanza.
3.  Cree un repositorio público en GitHub con el nombre 
    `IF0009-Lab12-carnet`.
4.  Suba su código y el archivo `README.md` con la solución a la Parte 2.
5.  Envíe el enlace directo de su repositorio de GitHub a través del 
    entorno virtual de aprendizaje antes de la fecha límite establecida.

¡Mucho éxito en la resolución de este laboratorio preparatorio!

/**
 * PanelBiblioteca - Web Component contenedor principal de la biblioteca.
 * Administra el catálogo de libros, el formulario de registro y la
 * comunicación HTTP asíncrona (Fetch API) con el Backend en Spring Boot.
 */
class PanelBiblioteca extends HTMLElement {
    constructor() {
        super();
        // TODO: Inicializar estado o Shadow DOM si decide usarlo
    }

    connectedCallback() {
        // TODO: Renderizar estructura base (formulario y grilla)
        // TODO: Invocar método para cargar libros desde la API REST
        // TODO: Registrar eventos de escucha para el formulario
    }

    async cargarLibros() {
        // TODO: Realizar petición Fetch (GET) a la API /api/libros
        // TODO: Iterar el listado y crear etiquetas <tarjeta-libro>
    }

    async registrarLibro(event) {
        // TODO: Capturar datos del formulario y serializar a JSON
        // TODO: Validar datos en el cliente antes de enviar
        // TODO: Realizar petición Fetch (POST) a la API /api/libros
        // TODO: Recargar el catálogo tras una respuesta exitosa
    }
}

// TODO: Registrar el Custom Element en el CustomElementRegistry

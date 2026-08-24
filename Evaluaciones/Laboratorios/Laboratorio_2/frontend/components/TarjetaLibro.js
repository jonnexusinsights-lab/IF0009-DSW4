/**
 * TarjetaLibro - Web Component para representar un libro individual.
 * Debe encapsular el HTML y los estilos mediante Shadow DOM.
 */
class TarjetaLibro extends HTMLElement {
    constructor() {
        super();
        // TODO: Crear Shadow Root en modo abierto (open)
        // TODO: Adjuntar plantilla clonada y slots
    }

    // TODO: Registrar atributos observados si desea reaccionar a cambios
    static get observedAttributes() {
        return [
            'data-titulo', 
            'data-autor', 
            'data-categoria', 
            'data-anio', 
            'data-leido', 
            'data-resena'
        ];
    }

    attributeChangedCallback(name, oldValue, newValue) {
        // TODO: Actualizar la representación al cambiar atributos
    }

    connectedCallback() {
        // TODO: Lógica al insertar el componente en el DOM
    }
}

// TODO: Registrar el Custom Element en el CustomElementRegistry

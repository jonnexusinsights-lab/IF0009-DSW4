DROP TABLE IF EXISTS matricula_curso;
DROP TABLE IF EXISTS estudiante;
DROP TABLE IF EXISTS profesor;

CREATE TABLE profesor (
    id BIGINT AUTO_INCREMENT PRIMARY KEY,
    nombre VARCHAR(100) NOT NULL,
    especialidad VARCHAR(80) NOT NULL,
    activo BOOLEAN NOT NULL DEFAULT TRUE
);

CREATE TABLE estudiante (
    id BIGINT AUTO_INCREMENT PRIMARY KEY,
    carnet VARCHAR(20) NOT NULL UNIQUE,
    nombre_completo VARCHAR(120) NOT NULL,
    correo VARCHAR(100) NOT NULL,
    carrera VARCHAR(80) NOT NULL
);

CREATE TABLE matricula_curso (
    id BIGINT AUTO_INCREMENT PRIMARY KEY,
    codigo_matricula VARCHAR(30) NOT NULL UNIQUE,
    estudiante_id BIGINT NOT NULL,
    profesor_id BIGINT NOT NULL,
    nombre_curso VARCHAR(100) NOT NULL,
    creditos INT NOT NULL,
    periodo VARCHAR(20) NOT NULL,
    estado VARCHAR(20) NOT NULL,
    monto_arancel DECIMAL(10,2) NOT NULL,
    fecha_matricula TIMESTAMP NOT NULL,
    CONSTRAINT fk_matricula_estudiante 
        FOREIGN KEY (estudiante_id) REFERENCES estudiante(id),
    CONSTRAINT fk_matricula_profesor 
        FOREIGN KEY (profesor_id) REFERENCES profesor(id)
);

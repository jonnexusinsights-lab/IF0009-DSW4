INSERT INTO profesor (nombre, especialidad, activo) VALUES 
('Dr. Armando Ramos', 'Ciencias de la Computacion', TRUE),
('Dra. Beatriz Solis', 'Sistemas de Informacion', TRUE),
('Ing. Esteban Quirós', 'Redes y Seguridad', FALSE);

INSERT INTO estudiante (carnet, nombre_completo, correo, carrera) VALUES 
('C01234', 'Valeria Monge Vargas', 'valeria.monge@ucr.ac.cr', 'Informática Empresarial'),
('C05678', 'Kevin Alvarado Cruz', 'kevin.alvarado@ucr.ac.cr', 'Informática Empresarial');

INSERT INTO matricula_curso 
(codigo_matricula, estudiante_id, profesor_id, nombre_curso, creditos, periodo, estado, monto_arancel, fecha_matricula) 
VALUES 
('MAT-2026-0001', 1, 1, 'Desarrollo de Software IV', 4, 'II-2026', 'ACTIVA', 45000.00, CURRENT_TIMESTAMP),
('MAT-2026-0002', 2, 2, 'Bases de Datos II', 3, 'II-2026', 'ACTIVA', 35000.00, CURRENT_TIMESTAMP);

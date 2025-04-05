-- Inserción de datos en la tabla de Eventos
INSERT INTO eventos (nombre, fecha, lugar) VALUES
('Concierto de Rock', '2025-06-15', 'Estadio Nacional'),
('Teatro Clásico', '2025-07-20', 'Teatro Central');

-- Inserción de datos en la tabla de Asientos
-- Para el evento 1: Concierto de Rock (id_evento = 1)
INSERT INTO asientos (id_evento, numero_asiento, seccion) VALUES
(1, 1, 'VIP'),
(1, 2, 'VIP'),
(1, 3, 'General'),
(1, 4, 'General'),
(1, 5, 'General'),
(1, 6, 'General'),
(1, 7, 'General'),
(1, 8, 'General'),
(1, 9, 'General'),
(1, 10, 'General');

-- Para el evento 2: Teatro Clásico (id_evento = 2)
INSERT INTO asientos (id_evento, numero_asiento, seccion) VALUES
(2, 1, 'Platea'),
(2, 2, 'Platea'),
(2, 3, 'Platea'),
(2, 4, 'Platea'),
(2, 5, 'Platea');

-- Inserción de datos en la tabla de Reservas
-- Reservas para el evento 1: Concierto de Rock
INSERT INTO reservas (id_evento, id_asiento, usuario) VALUES
(1, 1, 'usuario1'),
(1, 2, 'usuario2'),
(1, 3, 'usuario3'),
(1, 4, 'usuario4');

-- Reservas para el evento 2: Teatro Clásico
INSERT INTO reservas (id_evento, id_asiento, usuario) VALUES
(2, 1, 'usuario5'),
(2, 3, 'usuario6');

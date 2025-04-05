-- Creación de la tabla de Eventos
CREATE TABLE eventos (
    id_evento SERIAL PRIMARY KEY,
    nombre VARCHAR(100) NOT NULL,
    fecha DATE NOT NULL,
    lugar VARCHAR(100)
);

-- Creación de la tabla de Asientos
CREATE TABLE asientos (
    id_asiento SERIAL PRIMARY KEY,
    id_evento INT NOT NULL,
    numero_asiento INT NOT NULL,
    seccion VARCHAR(50),
    FOREIGN KEY (id_evento) REFERENCES eventos(id_evento)
);

-- Creación de la tabla de Reservas
CREATE TABLE reservas (
    id_reserva SERIAL PRIMARY KEY,
    id_evento INT NOT NULL,
    id_asiento INT NOT NULL,
    usuario VARCHAR(100),
    fecha_reserva TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (id_evento) REFERENCES eventos(id_evento),
    FOREIGN KEY (id_asiento) REFERENCES asientos(id_asiento),
    CONSTRAINT reserva_unica UNIQUE (id_evento, id_asiento)
);

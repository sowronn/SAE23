-- Table des aéroports
CREATE TABLE aeroports (
id INT PRIMARY KEY,
nom VARCHAR(100),
pays VARCHAR(100)
);

-- Table des pistes d'atterrissage
CREATE TABLE pistes_atterrissage (
numero INT,
aeroport_id INT,
longueur INT,
FOREIGN KEY (aeroport_id) REFERENCES aeroports(id)
);

-- Table des compagnies
CREATE TABLE compagnies (
id INT PRIMARY KEY,
nom VARCHAR(100),
description VARCHAR(500),
pays_rattachement VARCHAR(100)
);

-- Table des types d'avions
CREATE TABLE types_avions (
id INT PRIMARY KEY,
marque VARCHAR(100),
modele VARCHAR(100),
description VARCHAR(500),
images VARCHAR(500),
longueur_piste_necessaire INT
);

-- Table des avions
CREATE TABLE avions (
id INT PRIMARY KEY,
nom VARCHAR(100),
compagnie_id INT,
type_id INT,
FOREIGN KEY (compagnie_id) REFERENCES compagnies(id),
FOREIGN KEY (type_id) REFERENCES types_avions(id)
);

-- Table des vols
CREATE TABLE vols (
id INT PRIMARY KEY,
avion_id INT,
pilote VARCHAR(50),
aeroport_depart_id INT,
date_heure_depart DATETIME,
aeroport_arrivee_id INT,
date_heure_arrivee DATETIME,
FOREIGN KEY (avion_id) REFERENCES avions(id),
FOREIGN KEY (aeroport_depart_id) REFERENCES aeroports(id),
FOREIGN KEY (aeroport_arrivee_id) REFERENCES aeroports(id)
);
CREATE DATABASE IF NOT EXISTS partsdb;
USE partsdb;

CREATE TABLE IF NOT EXISTS parts (
    id INT AUTO_INCREMENT PRIMARY KEY,
    category VARCHAR(50),
    model VARCHAR(100),
    specs VARCHAR(255)
);

INSERT INTO parts (category, model, specs) VALUES
('CPU','Intel Core i9','12 cores, 3.6GHz'),
('CPU','AMD Ryzen 9','12 cores, 3.8GHz'),
('GPU','NVIDIA RTX 3080','10GB GDDR6X'),
('RAM','Corsair Vengeance','32GB DDR4 3600MHz'),
('Motherboard','ASUS ROG STRIX','ATX, Z790'),
('PSU','Corsair RM850','850W, 80+ Gold');

CREATE TABLE IF NOT EXISTS users (
    id INT AUTO_INCREMENT PRIMARY KEY,
    username VARCHAR(50) UNIQUE NOT NULL,
    password VARCHAR(255) NOT NULL,
    role ENUM('admin', 'editor', 'viewer') NOT NULL
);

INSERT INTO users (username, password, role) VALUES (
    'admin',
    'scrypt:32768:8:1$RPwf3n4vd0kOFUR4$42fa4d1abe85b25994b9362fc282f5ff079e68f56b3815c2414411307600cefbc3efe033b61e286f2b5793f1472c7b0c3b869ad8b4972354ffabc3042183bbaa',
    'admin'
);

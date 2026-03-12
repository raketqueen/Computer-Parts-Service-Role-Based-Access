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

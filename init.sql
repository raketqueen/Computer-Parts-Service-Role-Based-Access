CREATE DATABASE IF NOT EXISTS partsdb;
USE partsdb;

CREATE TABLE IF NOT EXISTS parts (
    id INT AUTO_INCREMENT PRIMARY KEY,
    category VARCHAR(50),
    model VARCHAR(100),
    specs VARCHAR(255)
);

INSERT INTO parts (category, model, specs) VALUES
('CPU','Intel Core i9-12900K','12th Desktop Processor'),
('CPU','AMD Ryzen 7 5800X','AM4 Socket 8-core/16-thread'),
('GPU','ZOTAC GAMING Geforce RTX 3080 Ti','NVIDIA RTX 3080 Ti Trinity OC 12GB'),
('GPU','Red Devil AMD Radeon™ RX 9070 XT','16GB GDDR6 RX9070XT'),
('RAM','Corsair VENGEANCE RGB PRO SL 32GB','DDR4 DRAM 3600MHz C18 Memory Kit'),
('RAM','G.Skill DDR5 FLARE X5','AMD EXPO Single Channel'),
('Motherboard','ROG STRIX B550-F GAMING WIFI II','AMD Ryzen™ AM4 Socket'),
('Motherboard','ROG MAXIMUS XI EXTREME','Intel® Socket 11519th / 8th Gen Intel® Core™ CPU'),
('PSU','CoolerMaster V850 SFX Gold','80+Gold Full-Modular SFX'),
('PSU','Seasonic Focus GX-1000','80+GOLD Gen5 Full Modular ATX Power Supply');

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

CREATE TABLE IF NOT EXISTS activity_logs (
    id INT AUTO_INCREMENT PRIMARY KEY,
    username VARCHAR(50) NOT NULL,
    action VARCHAR(50) NOT NULL,
    details VARCHAR(255),
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

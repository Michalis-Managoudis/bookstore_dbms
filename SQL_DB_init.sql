DROP TABLE IF EXISTS TilefonaS;
DROP TABLE IF EXISTS TilefonaE;
DROP TABLE IF EXISTS TilefonaP;
DROP TABLE IF EXISTS Anikei;
DROP TABLE IF EXISTS Pragmateuetai;
DROP TABLE IF EXISTS Brabeia;
DROP TABLE IF EXISTS Graftike_Apo;
DROP TABLE IF EXISTS Exei;
DROP TABLE IF EXISTS Typos;
DROP TABLE IF EXISTS Agorazoun;
DROP TABLE IF EXISTS Partida;
DROP TABLE IF EXISTS Apothema;
DROP TABLE IF EXISTS Ekdosi;
DROP TABLE IF EXISTS Biblio;
DROP TABLE IF EXISTS Katigoria;
DROP TABLE IF EXISTS Thema;
DROP TABLE IF EXISTS Siggrafeas;
DROP TABLE IF EXISTS Ergazomenoi;
DROP TABLE IF EXISTS Pelatis;

CREATE TABLE Biblio (
	id_bibliou INT NOT NULL,
	titlos VARCHAR(255) NOT NULL,
	perigrafi TEXT NOT NULL,
	glossa_prototypou VARCHAR(255) NOT NULL,
	metafrasmeno BOOLEAN DEFAULT 0,
	PRIMARY KEY (id_bibliou)
);
INSERT INTO Biblio (id_bibliou, titlos, perigrafi, glossa_prototypou, metafrasmeno) VALUES
(1, 'Πιάστε τους!', 'Αγώνες-μυστήριο στο δάσος των μουσώνων. Για παιδιά από 8 ετών.', 'Ελληνικά', 0),
(2, 'Μικρό Νεοελληνικό Λεξικό', '25.000 λήμματα με συνοπτικές και περιεκτικές ερμηνείες.', 'Ελληνικά', 0),
(3, 'Θεμελιώδες αρχές συστημάτων Βάσεων Δεδομένων', 'Το βιβλίο παρουσιάζει τις θεμελιώδεις έννοιες...', 'Αγγλικά', 1),
(4, 'Ο Ηρακλής και τα κατορθώματα του', 'Οι περιπέτειες από τη γέννηση ως το τέλος του Ηρακλή.', 'Ελληνικά', 0),
(5, 'Mastering Grammar and Lexis for B2 Exams', 'Mastering Grammar and Lexis for B2 Exams presents the grammatical structures and vocabulary required for the B2 level exams.', 'Αγγλικά', 0),
(6, 'On Screen Student\'s Book', 'On Screnn B1 is a modular course at CEF Level B1.', 'Αγγλικά', 0);

CREATE TABLE Ekdosi (
	id_ekdosis INT NOT NULL,
	aa INT(2) NOT NULL,
	id_bibliou INT NOT NULL,
	ISBN VARCHAR(17) NOT NULL UNIQUE,
	etos_kikloforias INT(4) NOT NULL,
	best_seller BOOLEAN DEFAULT 0,
	url_ekdosis VARCHAR(255) UNIQUE,
	eksofyllo VARCHAR(255) NOT NULL,
	bibliodesia VARCHAR(255) NOT NULL,
	selides INT(4) NOT NULL,
	poiotita_fyllou VARCHAR(255) NOT NULL,
	melani VARCHAR(255) NOT NULL,
	megethos_selidas CHAR(2) NOT NULL,
	varos_fyllou INT(3) NOT NULL,
	PRIMARY KEY (id_ekdosis),
	FOREIGN KEY (id_bibliou) REFERENCES Biblio(id_bibliou) ON DELETE CASCADE ON UPDATE CASCADE
);

INSERT INTO Ekdosi (id_ekdosis, aa, id_bibliou, ISBN, etos_kikloforias, best_seller, url_ekdosis, eksofyllo, bibliodesia, selides, poiotita_fyllou, melani, megethos_selidas, varos_fyllou) VALUES
(14, 4, 1, '960-16-0870-2', 2006, 0, 'www.piaste.com/...', 'Μαλακό', '---', 280, '---', '---', 'Β3', 8),
(21, 1, 2, '978-960-360-018-3', 1994, 1, 'www.lexiko.gr/...', 'Μαλακό', '---', 800, '---', '---', 'B6', 3),
(35, 5, 3, '978-960-531-01', 2010, 0, 'www.diavlosbooks.gr/.../', 'Μαλακό', '---', 980, '---', '---', 'Α4', 14),
(37, 7, 3, '978-960-531-343-2', 2016, 0, 'www.diavlosbooks.gr/...', 'Μαλακό', '---', 1000, '---', '---', 'Α4', 14),
(41, 1, 4, '976-4-46-474-8', 1990, 0, '---', 'Σκληρό', '---', 150, '---', '---', 'Β4', 11),
(51, 1, 5, '978-9963-48-792-9', 2012, 0, 'www.burlingtonbooks.uk/...', 'Μαλακό', '---', 215, '---', '---', 'Α4', 15),
(63, 3, 6, '978-1-4715-5453-7', 2018, 0, 'www.expresspublishing.co.uk/...', 'Μαλακό', '---', 150, '---', '---', 'Α4', 15),
(65, 5, 6, '978-1-4715-12', 2020, 0, 'www.expresspublishing.co.uk/.../', 'Μαλακό', '---', 160, '---', '---', 'Α4', 15);

CREATE TABLE Katigoria (
	id_katigorias INT NOT NULL,
	Konoma VARCHAR(255) NOT NULL UNIQUE,
	PRIMARY KEY (id_katigorias)
);

INSERT INTO Katigoria (id_katigorias, Konoma) VALUES
(3, 'Εκπαιδευτικά'),
(2, 'Ελληνική Λογοτεχνία'),
(1, 'Θετικές Επιστήμες'),
(4, 'Λεξικό'),
(5, 'Παιδικό');

CREATE TABLE Thema (
	id_thematos INT NOT NULL,
	Tonoma VARCHAR(255) NOT NULL UNIQUE,
	PRIMARY KEY (id_thematos)
);

INSERT INTO Thema (id_thematos, Tonoma) VALUES
(2, 'Αστυνομικό'),
(6, 'Εκμάθηση Αγγλικών'),
(4, 'Νεανική Λογοτεχνία'),
(5, 'Παραμύθι'),
(3, 'Πληροφορική'),
(1, 'Σύγχρονη Λογοτεχνία');

CREATE TABLE Siggrafeas (
	id_siggrafea INT NOT NULL,
	AFM VARCHAR(20) NOT NULL UNIQUE,
	onoma VARCHAR(255) NOT NULL,
	eponimo VARCHAR(255) NOT NULL,
	fylo CHAR(1) NOT NULL CHECK (fylo IN ('Γ','Α')),
	ethnikotita VARCHAR(255) NOT NULL,
	xora VARCHAR(255) NOT NULL,
	poli VARCHAR(255) NOT NULL,
	TK VARCHAR(10) NOT NULL,
	dieuthinsi VARCHAR(255) NOT NULL,
	email VARCHAR(255) NOT NULL UNIQUE,
	IBAN VARCHAR(34) NOT NULL UNIQUE,
	idiotita VARCHAR(255),
	PRIMARY KEY (id_siggrafea)
);

INSERT INTO Siggrafeas (id_siggrafea, AFM, onoma, eponimo, fylo, ethnikotita, xora, poli, TK, dieuthinsi, email, IBAN, idiotita) VALUES
(10, 1010, 'Φίλιππος', 'Μανδηλάρας', 'Α', 'Έλληνας', 'Ελλάδα', 'Αθήνα', '15000', 'Μαρούσι 15', 'mandil@mail.com', 'GR 101010', NULL),
(11, 1011, 'Μαρία', 'Παπαγιάννη', 'Γ', 'Ελληνίδα', 'Ελλάδα', 'Αθήνα', '15000', 'Φάληρο 60', 'papa@mail.com', 'GR 1110', NULL),
(30, 321, 'Ramez', 'Elmasri', 'Α', 'Αιγύπτιος', 'ΗΠΑ', 'Τέξας', '555', 'Alexandria 7219', 'elsmari@mail.com', 'US 302010', 'Καθηγητής Πανεπιστημίου'),
(31, 3210, 'Shamkant B.', 'Navathe', 'Α', 'Αμερικανός', 'ΗΠΑ', 'Atlanta', '553', 'Pearson 1520', 'navathe@mail.com', 'US 3210', 'Καθηγητής Πανεπιστημίου'),
(40, 4321, 'Άλκης', 'Γουλίμη', 'Γ', 'Ελληνίδα', 'Ελλάδα', 'Αθήνα', '13500', 'Περιστέρι 111', 'goulimi@mail.com', 'GR 403020', NULL),
(50, 54321, 'Georgia', 'Graham', 'Γ', 'Αγγλίδα', 'Ηνωμένο Βασίλειο', 'Λονδίνο', '888', 'Big Ben 52', 'graham@mail.com', 'UK 504030', 'Φιλόλογος Αγγλικής Γλώσσας'),
(51, 543210, 'Alan', 'Walker', 'Α', 'Ιρλανδός', 'Ηνωμένο Βασίλειο', 'Λονδίνο', '888', 'London Eye 68', 'walker@mail.com', 'UK 514131', 'Φιλόλογος Αγγλικής Γλώσσας'),
(60, 654321, 'Jenny', 'Dooley', 'Γ', 'Αγγλίδα', 'Ηνωμένο Βασίλειο', 'Νιούμπερι', '4619', 'Greenham Park', 'dooley@mail.com', 'UK 605040', NULL),
(61, 6543210, 'Virginia', 'Evans', 'Γ', 'Αγγλίδα', 'Ηνωμένο Βασίλειο', 'Νιούμπερι', '4619', 'Liberty House 432', 'evas@mail.com', 'UK 605041', NULL);

CREATE TABLE TilefonaS (
	id_siggrafea INT NOT NULL,
	Stilefono BIGINT NOT NULL,
	PRIMARY KEY (id_siggrafea,Stilefono),
	FOREIGN KEY (id_siggrafea) REFERENCES Siggrafeas(id_siggrafea) ON DELETE CASCADE ON UPDATE CASCADE
);

CREATE TABLE Ergazomenoi (
	id_ergazomenou INT NOT NULL,
	AFM VARCHAR(20) NOT NULL UNIQUE,
	onoma VARCHAR(255) NOT NULL,
	eponimo VARCHAR(255) NOT NULL,
	fylo CHAR(1) NOT NULL CHECK (fylo IN ('Γ','Α')),
	xora VARCHAR(255) NOT NULL,
	poli VARCHAR(255) NOT NULL,
	TK VARCHAR(10) NOT NULL,
	dieuthinsi VARCHAR(255) NOT NULL,
	email VARCHAR(255) NOT NULL UNIQUE,
	IBAN VARCHAR(34) NOT NULL UNIQUE,
	typeErgazomenou CHAR(1) NOT NULL CHECK (typeErgazomenou IN ('Σ','Μ','Γ','Ε')),
	PRIMARY KEY (id_ergazomenou)
);

INSERT INTO Ergazomenoi (id_ergazomenou, AFM, onoma, eponimo, fylo, xora, poli, TK, dieuthinsi, email, IBAN, typeErgazomenou) VALUES
(10, 101010, 'Μιχάλης', 'Κουντούρης', 'Α', 'Ελλάδα', 'Αθήνα', '15000', 'Μαρούσι 100', 'kountouris@mail.com', 'GR 101010', 'Γ'),
(11, 111111, 'Κατερίνα', 'Λελούδη', 'Γ', 'Ελλάδα', 'Αθήνα', '15000', 'Μαρούσι 100', 'leloudi@mail.com', 'GR 111111', 'Ε'),
(12, 121212, 'Παναγιώτης ', 'Σαράτσης', 'Α', 'Ελλάδα', 'Αθήνα', '15000', 'Κυψέλη 40', 'sar@mail.com', 'GR 121212', 'Σ'),
(20, 202020, 'Άννα', ' Ιορδανίδου', 'Γ', 'Ελλάδα', 'Θεσσαλονική', '16000', 'Εγνατίας 10', 'ior@mail.com', 'GR 202020', 'Ε'),
(21, 212121, 'Στέλλα', ' Μπαταβάνη', 'Γ', 'Ελλάδα', 'Θεσσαλονίκη', '16000', 'Αγίου Δημητρίου 20', 'mpat@mail.com', 'GR 212121', 'Ε'),
(30, 303030, 'Μιχάλης', 'Χατζόπουλος', 'Α', 'Ελλάδα', 'Αθήνα', '15000', 'Πανεπιστημίου 100', 'xatz@mail.com', 'GR 303030', 'Μ'),
(40, 40, 'Παύλος', 'Βαλασάκης', 'Α', 'Ελλάδα', 'Πάτρα', '26440', 'Πανεπιστημίου 40', 'bal@mail.com', 'GR 404040', 'Γ'),
(50, 505050, 'Angela', 'Simons', 'Γ', 'Ηνωμένο Βασίλειο', 'Λονδίνο', '1420', 'London Eye 1635', 'simon@mail.com', 'UK 505050', 'Σ');

CREATE TABLE TilefonaE (
	id_ergazomenou INT NOT NULL,
	Etilefono BIGINT NOT NULL,
	PRIMARY KEY (id_ergazomenou,Etilefono),
	FOREIGN KEY (id_ergazomenou) REFERENCES Ergazomenoi(id_ergazomenou) ON DELETE CASCADE ON UPDATE CASCADE
);
CREATE TABLE Apothema (
	id_apothematos INT NOT NULL,
	posotita_apothematos INT(5) NOT NULL,
	timi_lianikis FLOAT NOT NULL,
	timi_xondrikis FLOAT NOT NULL,
	ekptosi INT(2) NOT NULL DEFAULT (00),
	thesi_apothikis CHAR(4) NOT NULL UNIQUE,
	PRIMARY KEY (id_apothematos)
);

INSERT INTO Apothema (id_apothematos, posotita_apothematos, timi_lianikis, timi_xondrikis, ekptosi, thesi_apothikis) VALUES
(14, 500, 10, 8.5, 0, 'ΑΑ34'),
(21, 3000, 8, 5, 10, 'ΑΙ76'),
(35, 11000, 100, 86, 10, 'ΓΑ31'),
(37, 2000, 130, 95, 0, 'ΑΑ21'),
(41, 50, 20, 18, 0, 'ΧΡ33'),
(51, 1000, 45, 33, 5, 'ΞΑ34'),
(63, 800, 31, 25, 5, 'ΞΚ78'),
(65, 200, 45, 40, 20, 'ΞΚ99');

CREATE TABLE Partida (
	id_ekdosis INT NOT NULL,
	aa INT NOT NULL,
	id_apothematos INT NOT NULL,
	arithmos_antitipwn INT(5) NOT NULL DEFAULT 10000,
	im_tiposis DATE NOT NULL,
	PRIMARY KEY (id_ekdosis,aa),
	FOREIGN KEY (id_apothematos) REFERENCES Apothema(id_apothematos) ON DELETE CASCADE ON UPDATE CASCADE,
	FOREIGN KEY (id_ekdosis) REFERENCES Ekdosi(id_ekdosis) ON DELETE CASCADE ON UPDATE CASCADE
);

INSERT INTO Partida (id_ekdosis, aa, id_apothematos, arithmos_antitipwn, im_tiposis) VALUES
(14, 3, 14, 2000, '2010-01-01'),
(21, 1, 21, 10000, '1994-01-01'),
(21, 3, 21, 10000, '2010-02-01'),
(21, 10, 21, 10000, '2013-04-01'),
(35, 1, 35, 10000, '2007-01-01'),
(37, 1, 37, 10000, '2007-02-01'),
(41, 1, 41, 10000, '2007-03-01'),
(51, 1, 51, 10000, '2007-05-01'),
(63, 1, 63, 10000, '2020-01-01'),
(63, 2, 63, 10000, '2020-02-01'),
(63, 3, 63, 10000, '2020-03-01');

CREATE TABLE Pelatis (
	id_pelati INT NOT NULL,
	onoma VARCHAR(255) NOT NULL,
	eponimo VARCHAR(255) NOT NULL,
	email VARCHAR(255) UNIQUE,
	eidiki_ekptosi INT(2) NOT NULL DEFAULT (00),
	typePelati CHAR(1) NOT NULL CHECK (typePelati IN ('Λ','Χ')),
	eponimia_etairias VARCHAR(255),
	idiotita_etairias VARCHAR(255),
	AFM VARCHAR(20) UNIQUE,
	PRIMARY KEY (id_pelati)
);

INSERT INTO Pelatis (id_pelati, onoma, eponimo, email, eidiki_ekptosi, typePelati, eponimia_etairias, idiotita_etairias, AFM) VALUES
(-1, 'Αγορά', 'Φυσικού Καταστήματος', NULL, 0, 'Λ', NULL, NULL, NULL),
(1, 'Μιχάλης', 'Μ.', 'man@mail.com', 0, 'Λ', NULL, NULL, NULL),
(2, 'Μάριος', 'Τ.', NULL, 0, 'Λ', NULL, NULL, NULL),
(3, 'Hλίας', 'Μ.', NULL, 15, 'Χ', 'BookLiakos', 'Βιβλιοπωλείο', 302010),
(4, 'Χρήστος', 'Χ.', NULL, 30, 'Χ', 'BookChris', 'Ιδιωτική Βιβλιοθήκη', 40302010),
(5, 'Σοφία', 'Μ.', 'mam@mail.com', 10, 'Λ', NULL, NULL, NULL),
(6, 'Φωτεινή', 'Κ', NULL, 10, 'Λ', NULL, NULL, NULL),
(7, 'Άννα', 'Σ.', 'ser@mail.com', 20, 'Χ', "Anna\'s Bookstore", 'Βιβλιοπωλείο', 70707);


CREATE TABLE TilefonaP (
	id_pelati INT NOT NULL,
	Ptilefono BIGINT NOT NULL,
	PRIMARY KEY (id_pelati,Ptilefono),
	FOREIGN KEY (id_pelati) REFERENCES Pelatis(id_pelati) ON DELETE CASCADE ON UPDATE CASCADE
);

CREATE TABLE Anikei (
	id_thematos INT NOT NULL,
	id_katigorias INT NOT NULL,
	PRIMARY KEY (id_thematos,id_katigorias),
	FOREIGN KEY (id_thematos) REFERENCES Thema(id_thematos) ON DELETE CASCADE ON UPDATE CASCADE,
	FOREIGN KEY (id_katigorias) REFERENCES Katigoria(id_katigorias) ON DELETE CASCADE ON UPDATE CASCADE
);
INSERT INTO Anikei (id_thematos, id_katigorias) VALUES
(3, 1),
(1, 2),
(2, 2),
(4, 2),
(6, 3);

CREATE TABLE Pragmateuetai (
	id_bibliou INT NOT NULL,
	id_thematos INT NOT NULL,
	PRIMARY KEY (id_bibliou,id_thematos),
	FOREIGN KEY (id_bibliou) REFERENCES Biblio(id_bibliou) ON DELETE CASCADE ON UPDATE CASCADE,
	FOREIGN KEY (id_thematos) REFERENCES Thema(id_thematos) ON DELETE CASCADE ON UPDATE CASCADE
);
INSERT INTO Pragmateuetai (id_bibliou, id_thematos) VALUES
(3, 3),
(1, 4),
(5, 6),
(6, 6);

CREATE TABLE Brabeia (
	brabeio VARCHAR(255) NOT NULL,
	id_bibliou INT NOT NULL,
	PRIMARY KEY (brabeio),
	FOREIGN KEY (id_bibliou) REFERENCES Biblio(id_bibliou) ON DELETE CASCADE ON UPDATE CASCADE
);
INSERT INTO Brabeia (brabeio, id_bibliou) VALUES
('Καλύτερο παιδικό βιβλίο 2018', 4);

CREATE TABLE Graftike_Apo (
	id_bibliou INT NOT NULL,
	id_siggrafea INT NOT NULL,
	PRIMARY KEY (id_bibliou,id_siggrafea),
	FOREIGN KEY (id_bibliou) REFERENCES Biblio(id_bibliou) ON DELETE CASCADE ON UPDATE CASCADE,
	FOREIGN KEY (id_siggrafea) REFERENCES Siggrafeas(id_siggrafea) ON DELETE CASCADE ON UPDATE CASCADE
);
INSERT INTO Graftike_Apo (id_bibliou, id_siggrafea) VALUES
(3, 30),
(3, 31),
(2, 40),
(4, 40),
(5, 50),
(6, 50),
(5, 51),
(6, 60),
(6, 61);

CREATE TABLE Exei (
	id_ergazomenou INT NOT NULL,
	id_ekdosis INT NOT NULL,
	PRIMARY KEY (id_ergazomenou,id_ekdosis),
	FOREIGN KEY (id_ergazomenou) REFERENCES Ergazomenoi(id_ergazomenou) ON DELETE CASCADE ON UPDATE CASCADE,
	FOREIGN KEY (id_ekdosis) REFERENCES Ekdosi(id_ekdosis) ON DELETE CASCADE ON UPDATE CASCADE
);
INSERT INTO Exei (id_ergazomenou, id_ekdosis) VALUES
(10, 14),
(11, 14),
(12, 14),
(20, 21),
(21, 21),
(30, 35),
(30, 37),
(40, 41),
(50, 51),
(50, 63),
(50, 65);

CREATE TABLE Typos (
	id_ekdosis INT NOT NULL,
	Etypos CHAR(1) NOT NULL CHECK (Etypos IN ('A','E')),
	PRIMARY KEY (id_ekdosis,Etypos),
	FOREIGN KEY (id_ekdosis) REFERENCES Ekdosi(id_ekdosis) ON DELETE CASCADE ON UPDATE CASCADE
);
INSERT INTO Typos (id_ekdosis, Etypos) VALUES
(35, 'E'),
(37, 'E'),
(41, 'A');

CREATE TABLE Agorazoun (
	id_apothematos INT NOT NULL,
	id_pelati INT NOT NULL,
	im_agoras DATE NOT NULL,
	-- Proairetiki dieu8insi apostolis
	poli VARCHAR(255),
	dieuthinsi VARCHAR(255),
	TK INT,
	xora VARCHAR(255),
	-- gia agores lianikis
	posotita INT NOT NULL,
	teliki_timi FLOAT NOT NULL,
	agora_allagis BOOLEAN DEFAULT 0,
	PRIMARY KEY (id_apothematos,id_pelati, im_agoras),
	FOREIGN KEY (id_apothematos) REFERENCES Apothema(id_apothematos) ON DELETE CASCADE ON UPDATE CASCADE,
	FOREIGN KEY (id_pelati) REFERENCES Pelatis(id_pelati) ON DELETE CASCADE ON UPDATE CASCADE
);

INSERT INTO Agorazoun (id_apothematos, id_pelati, im_agoras, poli, dieuthinsi, TK, xora, posotita, teliki_timi, agora_allagis) VALUES
(14, 5, '2020-01-31', NULL, NULL, NULL, NULL, 3, 10, 0),
(21, 5, '2020-09-30', NULL, NULL, NULL, NULL, 3, 7.2, 0),
(35, 3, '2020-10-20', NULL, NULL, NULL, NULL, 200, 77.4, 0),
(37, 5, '2020-10-30', NULL, NULL, NULL, NULL, 2, 130, 0),
(37, 7, '2020-08-30', NULL, NULL, NULL, NULL, 9, 95, 0),
(41, 5, '2019-12-20', NULL, NULL, NULL, NULL, 3, 20, 0),
(51, -1, '2020-08-20', NULL, NULL, NULL, NULL, 50, 42.75, 0),
(51, 6, '2019-09-30', NULL, NULL, NULL, NULL, 15, 42.75, 0),
(63, 5, '2018-02-13', NULL, NULL, NULL, NULL, 10, 31, 0),
(63, 5, '2020-09-10', NULL, NULL, NULL, NULL, 5, 29.5, 0),
(65, 5, '2020-06-17', NULL, NULL, NULL, NULL, 1, 36, 0);
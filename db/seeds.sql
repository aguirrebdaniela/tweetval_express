DROP TABLE IF EXISTS users CASCADE;
DROP TABLE IF EXISTS terms CASCADE;
DROP TABLE IF EXISTS results CASCADE;

CREATE TABLE users (
  id BIGSERIAL PRIMARY KEY,
  name VARCHAR NOT NULL,
  email VARCHAR NOT NULL UNIQUE,
  password_digest VARCHAR NOT NULL,
  token VARCHAR NOT NULL
);

INSERT INTO users (name, email, password_digest, token) VALUES
('Daniela', 'daniela@aguirre.com', 'demo', 'demo'), 
('Jose', 'jose@suarez.com', 'demo', 'demo');

CREATE TABLE terms (
  id BIGSERIAL PRIMARY KEY,
  word VARCHAR, 
  search_date TIMESTAMP,
  user_id SERIAL REFERENCES users(id)
);

INSERT INTO terms (word, search_date, user_id) VALUES
('Peru', TIMESTAMP '2011-05-16 15:36:38', 1),
('Trump', TIMESTAMP '2011-05-16 15:36:38', 1),
('Moore', TIMESTAMP '2011-05-16 15:36:38', 1),
('Spacey', TIMESTAMP '2011-05-16 15:36:38', 2),
('Mcdonalds', TIMESTAMP '2011-05-16 15:36:38', 2),
('Nike', TIMESTAMP '2011-05-16 15:36:38', 2),
('Adidas', TIMESTAMP '2011-05-16 15:36:38', 2);

CREATE TABLE results (
	id BIGSERIAL PRIMARY KEY,
	tweet_text TEXT,
	score DECIMAL,
	magnitude DECIMAL, 
	evaluation VARCHAR,
	id_terms SERIAL REFERENCES terms(id)
);

INSERT INTO results (tweet_text, score, magnitude, evaluation, id_terms) VALUES
('Result for peru', 1, 1, 'positive', 1),
('Result for trump', 2, 2, 'negative', 2),
('Result for Nike', 3, 2, 'neutral', 6);

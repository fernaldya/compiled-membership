CREATE TABLE memberships (
	id serial4 NOT NULL,
	"name" varchar(255) NULL,
	membership_uri varchar(255) NULL,
	membership_number varchar(150) NULL,
	created_at timestamp DEFAULT CURRENT_TIMESTAMP NULL,
	"owner" varchar(50) NULL,
	CONSTRAINT memberships_name_key UNIQUE (name),
	CONSTRAINT memberships_pkey PRIMARY KEY (id)
);

CREATE TABLE owners (
	OWNER varchar(50) PRIMARY KEY,
	created_at timestamp NULL DEFAULT current_timestamp
);

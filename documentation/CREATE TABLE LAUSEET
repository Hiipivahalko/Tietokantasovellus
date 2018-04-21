# CHANNEL

CREATE TABLE channel (
	id INTEGER NOT NULL,
	date_created DATETIME,
	date_modified DATETIME,
	name VARCHAR(144) NOT NULL,
	PRIMARY KEY (id)
);

# ACCOUNT

CREATE TABLE account (
	id INTEGER NOT NULL,
	date_created DATETIME,
	date_modified DATETIME,
	username VARCHAR(144) NOT NULL,
	password VARCHAR(144) NOT NULL,
	motto VARCHAR(144) NOT NULL,
	admin BOOLEAN NOT NULL,
	email VARCHAR(144) NOT NULL,
	PRIMARY KEY (id),
	CHECK (admin IN (0, 1))
);

# MESSAGE

CREATE TABLE message (
	id INTEGER NOT NULL,
	date_created DATETIME,
	date_modified DATETIME,
	body TEXT NOT NULL,
	writer VARCHAR(144) NOT NULL,
	account_id INTEGER NOT NULL,
	channel_id INTEGER NOT NULL,
	PRIMARY KEY (id),
	FOREIGN KEY(account_id) REFERENCES account (id),
	FOREIGN KEY(channel_id) REFERENCES channel (id)
);

# channel-account joint table

CREATE TABLE accounts (
	account_id INTEGER NOT NULL,
	channel_id INTEGER NOT NULL,
	PRIMARY KEY (account_id, channel_id),
	FOREIGN KEY(account_id) REFERENCES account (id),
	FOREIGN KEY(channel_id) REFERENCES channel (id)
);

# COMMENT

CREATE TABLE comment (
	id INTEGER NOT NULL,
	date_created DATETIME,
	date_modified DATETIME,
	body TEXT NOT NULL,
	writer VARCHAR(144) NOT NULL,
	message_id INTEGER NOT NULL,
	account_id INTEGER NOT NULL,
	PRIMARY KEY (id),
	FOREIGN KEY(message_id) REFERENCES message (id),
	FOREIGN KEY(account_id) REFERENCES account (id)
);

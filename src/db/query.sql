CREATE TABLE clients(
    idclient        int             AUTO_INCREMENT,
    nome            varchar(50)     NOT NULL,
    email           varchar(50)     NOT NULL,
    cpf             int(11)         NOT NULL,
    PRIMARY KEY (idclient)
);

CREATE TABLE participant(
    idparticipant   int             AUTO_INCREMENT,
    nome            varchar(50)     NOT NULL,
    PRIMARY KEY(idparticipant)
);

CREATE TABLE votation(
    idvotation      int             AUTO_INCREMENT,
    participant     varchar(50)     NOT NULL,
    client          varchar(50)     NOT NULL,
    PRIMARY KEY (idvotation)
);

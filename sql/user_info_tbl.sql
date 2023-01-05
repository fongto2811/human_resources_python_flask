-- ADMIN
CREATE TABLE user_info (
    id NUMBER GENERATED ALWAYS AS IDENTITY(START WITH 1 INCREMENT BY 1),
    first_name VARCHAR2(50),
    last_name VARCHAR2(50),
    username VARCHAR2(50) NOT NULL,
    password VARCHAR2(256) NOT NULL,
    email VARCHAR2(50),
    phone VARCHAR2(20),
    address VARCHAR2(200),
    img VARCHAR2(500),
    PRIMARY KEY(id)
);

--admin admin
INSERT INTO user_info VALUES(1,'admin','admin','admin','$2b$12$N1VLixyVW9dE.bIJCSKQA.Kgf7mmUpY.CvvAcv89VMRZyXUA9DWFG', 'admin@admin.com','0987385499','admin address','https://cdn.pixabay.com/photo/2015/04/23/22/00/tree-736885__480.jpg');


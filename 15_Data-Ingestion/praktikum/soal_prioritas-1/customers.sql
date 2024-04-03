-- create customers table
CREATE TABLE customers (
    ID INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(100),
    email VARCHAR(100),
    address VARCHAR(255)
);

-- insert customers data
INSERT INTO customers (name, email, address)
VALUES
    ('John Doe', 'john.doe@example.com', '123 Main St, City, Country'),
    ('Jane Smith', 'jane.smith@example.com', '456 Elm St, City, Country'),
    ('Michael Johnson', 'michael.johnson@example.com', '789 Oak St, City, Country'),
    ('Emily Brown', 'emily.brown@example.com', '101 Pine St, City, Country'),
    ('William Taylor', 'william.taylor@example.com', '202 Maple St, City, Country'),
    ('Sophia Anderson', 'sophia.anderson@example.com', '303 Cedar St, City, Country'),
    ('James Wilson', 'james.wilson@example.com', '404 Birch St, City, Country'),
    ('Olivia Martinez', 'olivia.martinez@example.com', '505 Walnut St, City, Country'),
    ('Benjamin Garcia', 'benjamin.garcia@example.com', '606 Cherry St, City, Country'),
    ('Ethan Lopez', 'ethan.lopez@example.com', '707 Oak St, City, Country'),
    ('Emma Rodriguez', 'emma.rodriguez@example.com', '808 Pine St, City, Country'),
    ('Mason Lee', 'mason.lee@example.com', '909 Elm St, City, Country'),
    ('Ava Hernandez', 'ava.hernandez@example.com', '1010 Maple St, City, Country'),
    ('Logan Gonzales', 'logan.gonzales@example.com', '1111 Cedar St, City, Country'),
    ('Harper Young', 'harper.young@example.com', '1212 Birch St, City, Country'),
    ('Evelyn Evans', 'evelyn.evans@example.com', '1313 Walnut St, City, Country'),
    ('Owen Hall', 'owen.hall@example.com', '1414 Cherry St, City, Country'),
    ('Liam Green', 'liam.green@example.com', '1515 Oak St, City, Country'),
    ('Avery Hill', 'avery.hill@example.com', '1616 Pine St, City, Country'),
    ('Lucas Baker', 'lucas.baker@example.com', '1717 Elm St, City, Country');



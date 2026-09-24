-- ============================================
-- LIBRARY MANAGEMENT SYSTEM
-- Python and SQL Task
-- ============================================

-- 1. Create Database
CREATE DATABASE IF NOT EXISTS library_db;

USE library_db;


-- ============================================
-- 2. Create Books Table
-- ============================================

CREATE TABLE IF NOT EXISTS Books (
    book_id INT PRIMARY KEY AUTO_INCREMENT,
    title VARCHAR(100) NOT NULL,
    author VARCHAR(100) NOT NULL,
    category VARCHAR(50) NOT NULL,
    price DECIMAL(10,2) NOT NULL CHECK (price >= 0),
    available_copies INT NOT NULL DEFAULT 1 CHECK (available_copies >= 0)
);


-- ============================================
-- 3. Create Members Table
-- ============================================

CREATE TABLE IF NOT EXISTS Members (
    member_id INT PRIMARY KEY AUTO_INCREMENT,
    member_name VARCHAR(100) NOT NULL,
    email VARCHAR(100) NOT NULL UNIQUE,
    phone VARCHAR(15) UNIQUE,
    join_date DATE NOT NULL
);


-- ============================================
-- 4. Create Borrow_Records Table
-- ============================================

CREATE TABLE IF NOT EXISTS Borrow_Records (
    borrow_id INT PRIMARY KEY AUTO_INCREMENT,
    book_id INT NOT NULL,
    member_id INT NOT NULL,
    borrow_date DATE NOT NULL,
    return_date DATE,

    FOREIGN KEY (book_id)
        REFERENCES Books(book_id)
        ON DELETE CASCADE
        ON UPDATE CASCADE,

    FOREIGN KEY (member_id)
        REFERENCES Members(member_id)
        ON DELETE CASCADE
        ON UPDATE CASCADE
);


-- ============================================
-- 5. Insert Book Records
-- ============================================

INSERT INTO Books
(title, author, category, price, available_copies)
VALUES
('Python Programming', 'Mark Lutz', 'Programming', 850.00, 5),
('Database Systems', 'Raghu Ramakrishnan', 'Database', 950.00, 4),
('Clean Code', 'Robert C. Martin', 'Programming', 750.00, 3),
('Data Science Basics', 'John Smith', 'Data Science', 650.00, 6),
('Web Development', 'David Miller', 'Web', 550.00, 2);


-- ============================================
-- 6. Insert Member Records
-- ============================================

INSERT INTO Members
(member_name, email, phone, join_date)
VALUES
('Vishnu', 'vishnu@gmail.com', '9876543210', '2026-01-10'),
('Rahul', 'rahul@gmail.com', '9876543211', '2026-01-15'),
('Priya', 'priya@gmail.com', '9876543212', '2026-02-05'),
('Anjali', 'anjali@gmail.com', '9876543213', '2026-02-20');


-- ============================================
-- 7. Insert Borrow Records
-- ============================================

INSERT INTO Borrow_Records
(book_id, member_id, borrow_date, return_date)
VALUES
(1, 1, '2026-03-01', '2026-03-10'),
(2, 2, '2026-03-05', '2026-03-15'),
(3, 1, '2026-03-12', NULL),
(4, 3, '2026-03-15', '2026-03-22'),
(1, 4, '2026-03-20', NULL);


-- ============================================
-- 8. CRUD Operations on Books
-- ============================================

-- CREATE
INSERT INTO Books
(title, author, category, price, available_copies)
VALUES
('Machine Learning', 'Tom Mitchell', 'AI', 900.00, 4);


-- READ
SELECT * FROM Books;


-- UPDATE
UPDATE Books
SET price = 950.00,
    available_copies = 5
WHERE book_id = 6;


-- DELETE
DELETE FROM Books
WHERE book_id = 6;


-- ============================================
-- 9. JOIN Query
-- ============================================

SELECT
    br.borrow_id,
    b.title AS book_title,
    m.member_name,
    br.borrow_date,
    br.return_date
FROM Borrow_Records br
JOIN Books b
    ON br.book_id = b.book_id
JOIN Members m
    ON br.member_id = m.member_id;


-- ============================================
-- 10. GROUP BY Query
-- ============================================

SELECT
    category,
    COUNT(*) AS total_books
FROM Books
GROUP BY category;


-- ============================================
-- 11. ORDER BY Query
-- ============================================

SELECT *
FROM Books
ORDER BY price DESC;


-- ============================================
-- 12. Aggregate Functions
-- ============================================

SELECT
    COUNT(*) AS total_books,
    AVG(price) AS average_price,
    MAX(price) AS highest_price,
    MIN(price) AS lowest_price,
    SUM(available_copies) AS total_available_copies
FROM Books;


-- ============================================
-- 13. Borrow Count for Each Member
-- ============================================

SELECT
    m.member_name,
    COUNT(br.borrow_id) AS books_borrowed
FROM Members m
LEFT JOIN Borrow_Records br
    ON m.member_id = br.member_id
GROUP BY m.member_id, m.member_name
ORDER BY books_borrowed DESC;


-- ============================================
-- 14. SQL View for Borrowed Book Report
-- ============================================

CREATE OR REPLACE VIEW borrowed_book_report AS
SELECT
    br.borrow_id,
    b.title AS book_title,
    b.author,
    m.member_name,
    m.email,
    br.borrow_date,
    br.return_date
FROM Borrow_Records br
JOIN Books b
    ON br.book_id = b.book_id
JOIN Members m
    ON br.member_id = m.member_id;


-- ============================================
-- 15. Display the View
-- ============================================

SELECT *
FROM borrowed_book_report;

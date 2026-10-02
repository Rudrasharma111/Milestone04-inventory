# Database Design

I have used PostgreSQL database with 2 tables: `users` and `items`.

## 1. ERD Diagram

users (id, email, password, role) 
   |
   | 1 to Many (One user can add many items)
   v
items (id, name, quantity, price, user_id)

## 2. Table Definitions

### 1. users table
- id : Integer (Primary Key)
- email : String (Unique)
- password : String
- role : String ("admin" or "user")

### 2. items table
- id : Integer (Primary Key)
- name : String (Item name)
- quantity : Integer (Available stock)
- price : Float (Item price)
- user_id : Integer (Foreign Key from users.id)

## 3. Primary Key, Foreign Key & Relationship
- Primary Keys: `users.id` and `items.id`
- Foreign Key: `items.user_id` connects to `users.id`
- Relationship: One-to-Many (1 user can create multiple inventory items)
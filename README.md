# Library Management System

This service is a library management system which supports following actions

1. User Registration
2. Librarian Registration
3. Borrow Book
4. Return Book
5. Extend Book
6. Pay fine

## Components

### Use case diagram

![Use case diagram](/01_usecase.png)

### Use case diagram - Detailed

![Use case diagram](/02_usecase_detailed.png)

### Class diagram

![Class Diagram](/04_class_diagram_1.png)

### Flow chart

![Flow Chart](/03_flow_chart.png)

## Development Environment

```bash
Programming Language: Python 3.8.3
Dependency Managament Tools: Pip
Interface: CLI
Preferred IDE: VS Code
```

## Development

```bash
python3 TestFunctions.py

# To import data from TSV files
python3 TestFunctions.py --books-file ./data/books.tsv --book-items-file ./data/book_items.tsv --users-file ./data/users.tsv
```


# https://www.guru99.com/joins.html
# https://javarevisited.blogspot.com/2013/05/difference-between-left-and-right-outer-join-sql-mysql.html

#https://www.youtube.com/watch?v=8flf3G48W8E

"""
retrives  data from one table
       select * from table_name
"""
"""
What are JOINS?
Joins help retrieving data from two or more database tables.
The tables are mutually related using primary and foreign keys.
"""

"""
Types of joins?
1.INNER JOIN
2.Outer JOINs
    LEFT JOIN
    RIGHT JOIN
    FULL JOIN
    CROSS JOIN

-----------------Cross JOIN-------------------
Cross JOIN is a simplest form of JOINs which matches each row from one database table to all rows of another.
In other words it gives us combinations of each row of first table with all records in second table.
syntax:
    SELECT * FROM `table 1` CROSS JOIN `table 2`
    
example:
    Suppose we want to get all member records against all the movie records, 
    we can use the script shown below to get our desired results.
    
    SELECT * FROM `movies` CROSS JOIN `members`
        WITHOUT CROSS USING
    SELECT * FROM TABLE1,TABLE2

------------------INNER JOIN-----------------------
The inner JOIN is used to return rows from both tables that satisfy the given condition.
            or
#The INNER JOIN matches each row in one table with every row in other tables and allows 
#you to query rows that contain columns from both tables.
            or 
#The INNER JOIN keyword selects records that have matching values in both tables.
syntax:
    SELECT select_list FROM t1 INNER JOIN t2 ON join_condition;
                with out using inner join
    select columns_names from table1,table2 where table1.col = table2.col
            or 
    SELECT column_name(s) FROM table1 INNER JOIN table2 ON table1.column_name = table2.column_name;

    for multiple tables:
        SELECT select_list FROM t1
        INNER JOIN t2 ON join_condition1
        INNER JOIN t3 ON join_condition2 ...;
    example:
        SELECT Orders.OrderID, Customers.CustomerName, Shippers.ShipperName
        FROM ((Orders
        INNER JOIN Customers ON Orders.CustomerID = Customers.CustomerID)
        INNER JOIN Shippers ON Orders.ShipperID = Shippers.ShipperID);


---------------------LEFT JOIN -------------------
The LEFT JOIN keyword returns all records from the left table (table1),
 and the matched records from the right table (table2). The result is NULL from the right side, if there is no match.
  In some databases LEFT JOIN is called LEFT OUTER JOIN.
synatx:
    SELECT column_name(s)
    FROM table1
    LEFT JOIN table2
    ON table1.column_name = table2.column_name;
----------------- RIGHT JOIN --------------------
The RIGHT JOIN keyword returns all records from the right table (table2), and the matched records from the left table (table1). 
The result is NULL from the left side, when there is no match.
In some databases RIGHT JOIN is called RIGHT OUTER JOIN.

syntax:
    SELECT column_name(s)
    FROM table1
    RIGHT JOIN table2
    ON table1.column_name = table2.column_name;

------------ FULL JOIN---------------------
The FULL OUTER JOIN keyword returns all records when there is a match in left (table1) or right (table2) table records.

syntax:
    SELECT column_name(s)
    FROM table1
    FULL JOIN table2
    ON table1.column_name = table2.column_name;
"""
"""
---------------Summary------------------
JOINS allow us to combine data from more than one table into a single result set.
JOINS have better performance compared to sub queries
INNER JOINS only return rows that meet the given criteria.
OUTER JOINS can also return rows where no matches have been found. The unmatched rows are returned with the NULL keyword.
The major JOIN types include Inner, Left Outer, Right Outer, Cross JOINS etc.
The frequently used clause in JOIN operations is "ON". "USING" clause requires that matching columns be of the same name.
JOINS can also be used in other clauses such as GROUP BY, WHERE, SUB QUERIES, AGGREGATE FUNCTIONS etc."""
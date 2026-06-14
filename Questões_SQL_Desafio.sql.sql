SHOW TABLES;
/*
TABLES
DATA_PRODUCT: PRODUCT INFO
DATA_PRODUCT_SALES: PRODUCT SALES
DATA_STORE_CAD: STORE INFO
DATA_STORE_SALES: SALES PER STORE
*/

# Verify the columns and their types
DESCRIBE data_product;
DESCRIBE data_product_sales;
DESCRIBE data_store_cad;
DESCRIBE data_store_sales;

/*
===================================
QUESTION 1
What are the 10 most expensive products in the company?
===================================
Obs: 
1) I used SubQuery to select the correct columns to answer the question
2) The Distinct is to confirm that each product is trully unique
*/

SELECT PRODUCT_NAME AS MOST_EXPENSIVE_PRODUCTS
FROM (

SELECT DISTINCT PRODUCT_COD, PRODUCT_NAME, PRODUCT_VAL
FROM data_product
ORDER BY PRODUCT_VAL DESC
LIMIT 10

) AS Top_Products;

/*
===================================
QUESTION 2
What sections do the 'BEBIDAS' and 'PADARIA' departments have?
===================================
*/

SELECT DISTINCT DEP_NAME, SECTION_NAME
FROM data_product
WHERE DEP_NAME = 'BEBIDAS' OR DEP_NAME = 'PADARIA'
ORDER BY DEP_NAME, SECTION_NAME ASC;

/*
===================================
QUESTION 3
What was the total sale of products (in $) of each Business Area in the first quarter of 2019?
===================================
Obs:
1) I used SubQuery to select the correct columns to answer the question
2) We could Join 'data_store_cad' whith 'DATA_PRODUCT_SALES' too to reach the same result
*/

SELECT BUSINESS_NAME, TOTAL_SALES_VALUE
FROM(

SELECT B.BUSINESS_CODE, B.BUSINESS_NAME, SUM(A.SALES_VALUE) AS TOTAL_SALES_VALUE
FROM data_store_sales as A
LEFT JOIN data_store_cad as B
ON A.STORE_CODE = B.STORE_CODE
WHERE A.DATE BETWEEN '2019-01-01' AND '2019-03-31'
GROUP BY B.BUSINESS_CODE, B.BUSINESS_NAME
ORDER BY TOTAL_SALES_VALUE DESC

) AS data_store_sales_cad_left_join;

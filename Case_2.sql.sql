/*
Case 2:
Please filter the period between this given range: ['2019-10-01','2019-12-31']
===================================
Columns: 
- Loja: STORE_NAME - data_store_cad (Asc Order)
- Categoria: BUSINESS_NAME - data_store_cad
- TM: SALES_VALUE / SALES_QTY - data_store_sales -> STORE_CODE - Key to connect both tables

Obs:
-- Query 1 and Query 2 were kept unchanged as requested
-- CTEs are used only to consume their results and generate the final visualization.
*/
-- Query 1
WITH CAD AS(
SELECT
      STORE_CODE,
      STORE_NAME,
      START_DATE,
      END_DATE,
      BUSINESS_NAME,
      BUSINESS_CODE
FROM data_store_cad),

-- Query 2
SALES AS(
SELECT
        STORE_CODE,
		DATE,
        SALES_VALUE,
        SALES_QTY
FROM data_store_sales
WHERE DATE BETWEEN '2019-01-01' AND '2019-12-31')

SELECT 
	B.STORE_NAME AS Loja, 
	B.BUSINESS_NAME AS Categoria,
	ROUND(SUM(A.SALES_VALUE) / SUM(A.SALES_QTY), 2) AS TM
    FROM SALES A
    LEFT JOIN CAD B ON A.STORE_CODE = B.STORE_CODE
	WHERE A.DATE BETWEEN '2019-10-01' AND '2019-12-31'
    GROUP BY B.STORE_NAME, B.BUSINESS_NAME
    ORDER BY B.STORE_NAME ASC;
    

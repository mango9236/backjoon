-- 코드를 입력하세요
SELECT BOOK_ID,	DATE_FORMAT(PUBLISHED_DATE, "%Y-%m-%d") as PUBLISHED_DATE
FROM BOOK
WHERE 
    CATEGORY = "인문" 
    AND PUBLISHED_DATE between "2021-01-01" and "2021-12-31"
ORDER BY PUBLISHED_DATE
    -- AND PUBLISHED_DATE = "2021-%m-%d"
-- 코드를 입력하세요
SELECT BOOK_ID, AUTHOR_NAME, DATE_FORMAT(PUBLISHED_DATE, '%Y-%m-%d') as PUBLISHED_DATE
FROM book b
join author a on b.AUTHOR_ID = a.AUTHOR_ID
where CATEGORY="경제"
order by PUBLISHED_DATE asc
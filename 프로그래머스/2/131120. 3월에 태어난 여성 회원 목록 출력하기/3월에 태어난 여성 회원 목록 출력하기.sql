-- 코드를 입력하세요
SELECT MEMBER_ID, MEMBER_NAME, GENDER, DATE_FORMAT(DATE_OF_BIRTH, "%Y-%m-%d") as DATE_OF_BIRTH
FROM MEMBER_PROFILE
WHERE DATE_OF_BIRTH like "%-03-%" AND TLNO IS NOT NULL AND GENDER = "W"
ORDER BY MEMBER_ID ASC;
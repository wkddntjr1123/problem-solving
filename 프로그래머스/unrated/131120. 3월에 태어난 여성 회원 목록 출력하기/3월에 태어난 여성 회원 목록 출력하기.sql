SELECT MEMBER_ID, MEMBER_NAME, GENDER, DATE_OF_BIRTH
FROM MEMBER_PROFILE
WHERE GENDER='W' AND MONTH(DATE_OF_BIRTH)=3 AND TLNO IS NOT NULL
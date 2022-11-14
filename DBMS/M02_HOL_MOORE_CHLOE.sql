--CHLOE MOORE
--M02 ASSIGNMENT: CONSTRUCTING A DATABASE
--8/30/2022


-- PART B. CREATING TABLES

create table CUSTOMERS(
    CUSTOMER_ID number(6) not null enable,
    FIRST_NAME varchar2(25) not null enable,
    LAST_NAME varchar2(25) not null enable,
    STREET_ADDRESS varchar2(50) not null enable,
    CITY varchar2(50) not null enable,
    STATE varchar2(50) not null enable,
    ZIP_CODE varchar2(10) not null enable,
    COUNTRY char(50),
    PHONE_NUMBER varchar2(25),
    EMAIL varchar2(50),
    DATE_OF_BIRTH date,
    GENDER varchar2(1)
);

create table BOOKS(
    BOOK_ID number(6) not null enable,
    BOOK_TITLE varchar2(250) not null enable,
    BOOK_DESCRIPTION varchar2(2000),
    BOOK_CATEGORY_CD char(2) not null enable,
    BOOK_PRICE number(8,2),
    BOOK_REVIEWS number(5),
    USER_RATING number(2,1)
);

create table BOOK_CATEGORY(
    BOOK_CATEGORY_CD char(2) not null enable,
    BOOK_CATEGORY_NAME varchar2(100) not null enable,
    BOOK_CATEGORY_DESCRIPTION varchar2(2000)
);

create table ORDERS(
    ORDER_NBR number(12) not null enable,
    CUSTOMER_ID number(6) not null enable,
    ORDER_DATE timestamp not null enable,
    ORDER_TOTAL number(8,2),
    SALESPERSON_ID number(6)
);

create table ORDER_ITEMS(
    ORDER_ITEM_ID number(20) not null enable,
    ORDER_NBR number(12) not null enable,
    BOOK_ID number(6) not null enable,
    UNIT_PRICE number(8,2),
    QUANTITY number(8)
);


-- PART C. CREATING CONSTRAINTS

--PRIMARY KEYS
alter table CUSTOMERS add constraint PK_CUSTOMERS primary key (CUSTOMER_ID);
alter table BOOKS add constraint PK_BOOKS primary key (BOOK_ID);
alter table BOOK_CATEGORY add constraint PK_BOOK_CATEGORY primary key (BOOK_CATEGORY_CD);
alter table ORDERS add constraint PK_ORDERS primary key (ORDER_NBR);
alter table ORDER_ITEMS add constraint PK_ORDER_ITEMS primary key (ORDER_ITEM_ID);

--FOREIGN KEYS
alter table BOOKS add constraint FK_BOOK_BOOK_CAT foreign key (BOOK_CATEGORY_CD) references BOOK_CATEGORY(BOOK_CATEGORY_CD) enable;
alter table ORDERS add constraint FK_ORD_CUST foreign key (CUSTOMER_ID) references CUSTOMERS(CUSTOMER_ID) enable;
alter table ORDERS add constraint FK_ORD_EMP foreign key (SALESPERSON_ID) references EMPLOYEES(EMPLOYEE_ID) enable;
alter table ORDER_ITEMS add constraint FK_ORD_ITM_ORD foreign key (ORDER_NBR) references ORDERS(ORDER_NBR) enable;
alter table ORDER_ITEMS add constraint FK_ORD_ITM_PROD foreign key (BOOK_ID) references BOOKS(BOOK_ID) enable;

--UNIQUE CONSTRAINTS
alter table ORDER_ITEMS add constraint UK_ORD_ITM unique (ORDER_NBR,BOOK_ID);


--PART D. COMMENTS

/*
create table ORDER_ITEMS(
    ORDER_ITEM_ID number(20) not null enable,
    ORDER_NBR number(12) not null enable,
    BOOK_ID number(6) not null enable,
    UNIT_PRICE number(8,2),
    QUANTITY number(8)
    constraint PK_ORDER_ITEMS primary key (ORDER_ITEM_ID),
    constraint FK_ORD_ITM_ORD foreign key (ORDER_NBR) references ORDERS(ORDER_NBR) enable,
    constraint FK_ORD_ITM_PROD foreign key (BOOK_ID) references BOOKS(BOOK_ID) enable
);
*/

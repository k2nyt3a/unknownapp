# unknownapp
This is an unknown application written in Java

---- For Submission (you must fill in the information below) ----
### Use Case Diagram
![alt text](<Untitled Diagram.drawio.png>)

### Flowchart of the main workflow

``` mermaid
flowchart TD
    start[Start] --> opt1{Select Option}
    opt1 --> stu[Login as Student]
    opt1 --> admin[Login as Admin]
    opt1 --> exit[Exit]

    stu --> opt2{New Student?}
    opt2 --No--> stuid[Enter Student ID]
    opt2 --Yes--> newstu[Create Student Profile]
    newstu --> id[Input ID]
    id --> fullname[Input Name]
    fullname --> major[Input Major]
    
    stuid --> s1[Successfully Logged In]
    major --> s1

    s1 --> opt3{Select Action}
    opt3 --> A[View Course Catalog]
    opt3 --> B[Register for a Course]
    opt3 --> C[Drop a Course]
    opt3 --> D[View My Schedule]
    opt3 --> E[Billing Summary]
    opt3 --> F[Edit My Profile]
    opt3 --> G[Logout and Save]

    A --> opt3
    D --> opt3

    B --> opt4{Enter Course Code?}
    opt4 --Code--> Ccode[Successfully Enroll]
    Ccode --> opt3
    opt4 --Enter--> opt3

    C --> opt5{Enter Course Code?}
    opt5 --Code--> Ccode2[Successfully Drop]
    opt5 --Enter--> opt3
    Ccode2 --> opt3

    E --> bill[Show Billing Summary]
    bill --> opt3

    F --> opt6{Edit Profile?}
    opt6 --Enter--> opt3
    opt6 --> newname[Enter New Name]
    newname --> newmajor[Enter New Major]
    newmajor --> success[Profile Updated]
    success --> opt3

    G --> opt1
    
    admin --> pwd[Enter Password]
    pwd --> opt7{Admin Options}
    opt7 --> H[View Course Catalog]
    opt7 --> I[View Class Roster]
    opt7 --> J[View All Students]
    opt7 --> K[Add New Students]
    opt7 --> L[Edit Student Profile]
    opt7 --> M[Add New Course]
    opt7 --> N[Edit Course]
    opt7 --> O[View Student Schedule]
    opt7 --> P[Billing Summary]
    opt7 --> Q[Logout and Save]

    H --> opt7
    J --> opt7
    Q --> opt1

    I --> opt8{Enter Course Code?}
    opt8 --Course Code--> Ccode3[Show Enrolled Student]
    Ccode3 --> opt7
    opt8 --Enter--> opt7

    K --> newstu1[Enter Student ID]
    newstu1 --> name1[Enter Full Name]
    name1 --> major1[Enter Major]
    major1 --> opt7

    L --> opt9{Enter Student ID?}
    opt9 --> id1[Enter Student ID]
    id1 --> newname2[Enter New Name]
    newname2 --> major2[Enter New Major]
    major2 --> opt7
    opt9 --Enter--> opt7

    M --> Ccode4[Enter Course Code]
    Ccode4 --> title[Enter Title]
    title --> credit[Enter Credit]
    credit --> cap[Enter Capacity]
    cap --> day[Enter Days]
    day --> opt7

    N --> opt10{Enter Course Code?}
    opt10 --> Ccode5[Enter Course Code]
    Ccode5 --> newtitle[Enter New Title]
    newtitle --> newcredit[Enter New Credit]
    newcredit --> opt7
    opt10 --Enter--> opt7

    O --> opt11{Enter Student ID?}
    opt11 --> id2[Enter Student ID]
    id2 --> show[Show Schedule]
    show --> opt7
    opt11 --Enter--> opt7

    P --> opt12{Enter Student ID?}
    opt12 --> id3[Enter Student ID]
    id3 --> bill2[Show Billing Summary]
    bill2 --> opt7
    opt12 --Enter--> opt7

```

### Prompts
create an equivalent Python version of the program fro view catalog. Put the Python program in a new folder called “python.” 
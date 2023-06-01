# CA_Werner
  B8IT150 Advanced Programming

EDUCATION MANAGEMENT SYSTEM

      The Education Management System report aims to outline the user requirements, functional requirements, and non-functional requirements for the development of a comprehensive system that manages various aspects of an educational institution. This system is designed to handle student information management, course management, instructor management, enrolment management, attendance and grade tracking, financial management, communication tools, security and access control, as well as user interface and user experience.
      The user requirements section of the report identifies the key functionalities that the Education Management System should offer, including student information management, course creation and management, instructor management, enrolment management, attendance and grade tracking, financial management, communication tools, security and access control, and user interface and user experience.
      The functional requirements section further elaborates on these functionalities, providing specific details on how each requirement should be implemented. It includes the ability to create and update student profiles, manage course information, create and update instructor profiles, handle enrolment processes, track attendance and grades, manage financial information, provide communication tools, ensure security and access control, and deliver a user-friendly interface.
      The non-functional requirements section outlines the performance, reliability, security, scalability, accessibility, usability, compatibility, integration, maintainability, and performance and data monitoring aspects of the Education Management System. These requirements ensure that the system performs well under high user loads, maintains high availability, ensures data security, can accommodate future growth, is accessible to all users, offers a seamless user experience, works well across different devices and browsers, integrates with other systems, is easy to maintain and update, and provides continuous monitoring of its performance and data.
      The report also covers the front-end and back-end technologies used in the development of the Education Management System. The front-end utilizes HTML, CSS, JavaScript, jQuery, and Bootstrap 4 to create an interactive and user-friendly interface, while the back-end incorporates FastAPI, middleware, authentication mechanisms, database operations with SQLAlchemy, routers and endpoints definitions, Pydantic models for data validation, and controller functions for handling instructor-related operations.




User Requirements

1. Student Information Management
1.1. Personal details: the system should be able to store and manage personal information about students, such as name, address, date of birth, and other relevant demographic information.
1.2. Contact information: the system should allow for the storage and management of student contact information, including email, phone number, and emergency contacts.
1.3. Academic records: the system should be able to store and manage student academic records, including courses taken, grades received, and other academic achievements.

2. Course Management
2.1. Course creation: the system should allow administrators to create new courses, including specifying course details such as course name, description, prerequisites, and course content.
2.2. Course editing: the system should allow administrators to edit existing courses, including updating course details, modifying course content, and adjusting scheduling details.
2.3. Course deletion: the system should allow administrators to delete courses that are no longer being offered.
2.4. Instructor assignment: the system should allow administrators to assign instructors to courses, based on their availability and areas of expertise.
2.5. Schedule creation: the system should allow administrators to create schedules for courses, including specifying course times, locations, and other scheduling details.

3. Instructor Management
3.1. Personal details: the system should be able to store and manage personal information about instructors, such as name, address, date of birth, and other relevant demographic information.
3.2. Contact information: the system should allow for the storage and management of instructor contact information, including email, phone number, and other relevant contact details.
3.3. Teaching schedules: the system should allow administrators to manage instructor teaching schedules, including assigning instructors to courses and specifying their availability.

4. Enrolment Management
4.1. Payment processing: the system should allow for the processing of student tuition payments, including accepting payment online and tracking payment status.
4.2. Waitlist management: the system should allow administrators to manage waitlists for courses that have reached maximum enrolment capacity.
4.3. Enrolment status communication: the system should enable the school to communicate with students about their enrolment status, including notifying them of their enrolment status and any changes to course schedules.

5. Attendance and Grade Tracking
5.1. Attendance tracking: the system should allow instructors to track student attendance, including taking attendance in class and marking students absent or present.
5.2. Grade tracking: the system should allow instructors to track student grades, including entering grades for assignments, exams, and other assessments.
5.3. Report generation: the system should allow instructors to generate reports on student attendance and grades, as well as transcripts and other academic records.

6. Financial Management
6.1. Tuition tracking: the system should allow for the tracking of student tuition payments, including monitoring payment status and generating reports on student tuition payments.
6.2. Instructor salary tracking: the system should allow for the tracking of instructor salaries, including monitoring salary payments and generating reports on instructor salaries.
6.3. Budget tracking: the system should allow for the tracking of the overall budget for the school of arts, including monitoring expenditures and generating reports on the school's financial status.

7. Communication Tools
7.1. Email notifications: the system should allow for the sending of email notifications to students, instructors, and administrators.
7.2. Chat functionality: the system should allow for real-time chat between users, including students, instructors, and administrators.
7.3. Discussion forums: the system should allow for the creation of discussion forums, where users can post and respond to messages.

8. Security and Access Control
8.1. User authentication: the system should require users to authenticate themselves before accessing the system, including requiring usernames and passwords, and implementing two-factor authentication.
8.2. Access control: the system should allow administrators to control access to the system, based on user roles and permissions. Access should be limited to only those who need it.
8.3. Data encryption: the system should encrypt sensitive data, such as student and instructor personal information, to prevent unauthorized access. The system should also implement secure protocols for data transmission.

9. User Interface and User Experience:
9.1. Navigation and layout: the system should have a clear and intuitive layout that allows users to easily navigate and find the information they need. Navigation menus and buttons should be easy to understand and use.
9.2. Responsiveness: the system should be responsive and work well on different devices and screen sizes, including desktops, laptops, tablets, and smartphones.
9.3. Customization: the system should allow users to customize their experience, such as choosing a preferred language, color scheme, or layout.
9.4. Help and support: the system should provide clear and concise instructions and help documentation to guide users through the system's features and functionality. The system should also provide easy access to customer support and technical assistance.


Functional Requirements

1. Student Information Management
1.1. The system should allow administrators to create and update student profiles, including personal details, contact information, and academic records.
1.2. The system should allow students to view and update their own profiles, including their personal information and academic progress.

2. Course Management
2.1. The system should allow administrators to create, update, and delete course information, including course titles, descriptions, prerequisites, and schedules.
2.2. The system should allow administrators to assign instructors to courses and manage instructor schedules.

3. Instructor Management
3.1. The system should allow administrators to create and update instructor profiles, including personal details, contact information, and teaching schedules.
3.2. The system should allow instructors to view their own profiles and schedules, and to update their availability.

4. Enrolment Management
4.1. The system should allow students to enrol in courses and pay tuition fees online.
4.2. The system should allow administrators to manage student enrolment, including accepting payments, managing waitlists, and communicating with students about enrolment status.

5. Attendance and Grade Tracking
5.1. The system should allow instructors to track student attendance and grades, and generate reports and transcripts.
5.2. The system should allow administrators to view student academic records and track student progress.

6. Financial Management
6.1. The system should allow administrators to manage financial information related to the school of arts, including student tuition payments, instructor salaries, and overall budget tracking.
6.2. The system should provide financial reports and data visualization tools to help administrators analyse financial data.

7. Communication Tools
7.1. The system should provide communication tools for students, instructors, and administrators, including email notifications, chat functionality, and discussion forums.
7.2. The system should allow administrators to send mass notifications to students and instructors.

8. Security and Access Control
8.1. The system should require user authentication before allowing access to the system.
8.2. The system should limit access to sensitive data based on user roles and permissions.
8.3. The system should encrypt sensitive data to prevent unauthorized access.

9. User Interface and User Experience
9.1. The system should have a clear and intuitive layout that allows users to easily navigate and find the information they need.
9.2. The system should be responsive and work well on different devices and screen sizes.
9.3. The system should allow users to customize their experience.
9.4. The system should provide clear and concise instructions and help documentation to guide users through the system's features and functionality.




Non-Functional Requirements

1. Performance: The system should be able to handle a large volume of user requests without experiencing significant slowdowns or outages.

2. Reliability: The system should be highly available and reliable, with minimal downtime or service disruptions.


3. Security: The system should be designed with security in mind, using encryption, firewalls, and other security measures to protect user data and prevent unauthorized access.

4. Scalability: The system should be designed to accommodate growth and increased usage over time, with the ability to scale up resources as needed.
5. Accessibility: The system should be accessible to users with disabilities, with features such as text-to-speech, high-contrast mode, and keyboard navigation.

6. Usability: The system should be easy to use and intuitive, with a clean and modern user interface that is consistent across all pages and features.


7. Compatibility: The system should be compatible with a range of different devices and browsers, including desktop computers, laptops, tablets, and smartphones.

8. Integration: The system should be able to integrate with other systems and platforms, such as payment gateways, learning management systems, and student information systems.


9. Maintainability: The system should be easy to maintain and update, with clear documentation, well-organized code, and regular testing and debugging.

10. Performance and Data Monitoring: The system should provide continuous monitoring of its performance and data to ensure that it is functioning properly, and notify administrators when issues arise.


THE FRONT-END

In the realm of web development, a combination of technologies is often employed to create dynamic and user-friendly interfaces. By leveraging HTML, CSS, JavaScript, jQuery, and Bootstrap 4, this project achieves an interactive and efficient system for managing educational and scheduling information.

HTML is used to structure the web pages and define the elements and content of the forms. It provides the foundational structure necessary for creating user-friendly and accessible forms. CSS, on the other hand, enhances the visual presentation of the web pages. By applying CSS styles, the project ensures a visually appealing and consistent design for buttons, forms, and overall layout.

To expedite development and enhance responsiveness, the project utilizes Bootstrap 4, a comprehensive CSS framework. Bootstrap offers a wide range of pre-designed components, a responsive grid system, and CSS styles that streamline the development process and ensure compatibility across different devices and screen sizes.

JavaScript plays a pivotal role in adding interactivity and dynamic behaviour to the web form. It enables the project to handle events such as adding and removing form fields dynamically, providing users with a flexible and convenient form management system.

To simplify DOM manipulation and event handling, the project incorporates the jQuery library, which is built on top of JavaScript. By utilizing jQuery, the project benefits from a simplified API that accelerates the process of interacting with the Document Object Model (DOM). It facilitates efficient addition and removal of form fields, enhancing the overall user experience.

By harnessing these technologies, the project achieves an interactive and user-friendly interface. Users are empowered to effortlessly add and remove form fields according to their specific requirements. Through the combined efforts of HTML, CSS, JavaScript, jQuery, and Bootstrap 4, this project establishes an efficient and effective form management system, elevating the usability and functionality of the overall application.



THE BACKEND

FASTAPI INTEGRATION AND MIDDLEWARE

      In the file main.py it imports requisite modules and establishes a FastAPI instance to facilitate the definition of routes and execution of the API.
      Cross-Origin Resource Sharing (CORS) middleware is integrated into the application using the `add_middleware` method of the FastAPI instance. This integration enables requests from any origin while encompassing credentials, HTTP methods, and headers.
      A middleware function, adorned with the `@app.middleware("http")` decorator, is defined to efficiently log incoming requests and outgoing responses. It captures pertinent request details, invokes the subsequent middleware or endpoint, captures the response, logs the corresponding status code, and finally returns it to the client.


AUTHENTICATION

      Within the auth folder, we have organized the files containing functions authentication-related functionalities, such as user login, registration, token verification, and retrieval of user information.
      Furthermore, it incorporates Pydantic models for data validation and type checking, as well as SQLAlchemy for seamless database operations.


AUTHENTICATION AND SECURITY

      The dependencies.py imports the `HTTPBearer` class from the `fastapi.security` module to establish the security scheme for bearer token authentication. Bearer tokens are commonly employed for safeguarding API endpoints and are typically included in the Authorization header of HTTP requests.
      An instance of the `HTTPBearer` class is instantiated and assigned to the `security` variable. This instance serves as the fundamental configuration for the bearer token authentication mechanism within the API.
      Custom functions implemented in the `jwt.py` file facilitate JSON Web Token (JWT) authentication. These functions encompass token creation, decoding, and verification, thereby engendering a secure authentication process.

DATABASE OPERATIONS AND MODELS

      The `create_all` method is executed on the metadata attribute of the Base object to construct the database tables. This operation relies on the provided engine object for seamless table creation.
      The `model.py` file defines the `UserModel` class, which represents the corresponding "user" table within the database. The SQLAlchemy Object-Relational Mapping (ORM) library is employed for database operations, including querying, inserting, updating, and deleting records.
      The `UserModel` class inherits from the Base class and associates itself with the "user" table by setting the `__tablename__` attribute. The class encompasses three columns: id (Integer), username (String), and password (String), representing the structure and fields of the "user" table.

ROUTER AND ENDPOINT DEFINITIONS

There is the inclusion of imported routers (`auth_router`, `student_router`, and `instructor_router`) into the application through the `include_router` method. This step facilitates the definition of distinctive routes and endpoints for the application, thereby ensuring organization and handling of various functionalities.

The `router.py` file aptly encapsulates authentication-related endpoints, such as user login, registration, token verification, and retrieval of user information. These endpoints rely on custom dependencies, schemas, database models, and JWT functions to handle the authentication process, engendering security and structured data validation.

PYDANTIC MODELS AND DATA VALIDATION

      Within the `schema.py` file there are Pydantic models, namely `User` and `UserLogin`. These models serve as instruments for enforcing data validation and type checking on user-related data, guaranteeing adherence to specified structure and types for data passed to and returned from API endpoints.
      The incorporation of Pydantic models within the code snippet facilitates data consistency and integrity throughout the application. Additionally, it offers an structure for efficient handling of user-related data.


THE “INSTRUCTOR” FOLDER AND CONTROLLER FUNCTIONS

Within the instructor folder, we have organized the files containing functions relevant to instructor operations.

The controller.py file encompasses functions responsible for interacting with instructor-related data stored in the database.
      
      get_instructor(instructor_id: int): Retrieves an instructor from the database based on the specified instructor_id. It establishes a database session, utilizes the crud module's get_instructor function with the session and ID, and raises an appropriate exception if the instructor is not found.
      
      get_all_instructors(): Retrieves all instructors from the database. It creates a database session, employs the crud module's get_all_instructors function with the session, and returns the retrieved instructors.
      
      create_instructor(instructor: InstructorCreate): Creates a new instructor in the database using the provided instructor data. It initiates a database session, invokes the crud module's create_instructor function with the session and instructor data, and returns the created instructor.
      
      update_instructor(instructor_id: int, instructor_update: InstructorUpdate): Updates an existing instructor in the database. It establishes a database session, retrieves the instructor using the given instructor_id, raises an exception if the instructor is not found, utilizes the crud module's update_instructor function with the session, retrieved instructor, and instructor update data, and returns the updated instructor.
      
      delete_instructor(instructor_id: int): Deletes an instructor from the database based on the specified instructor_id. It initiates a database session, retrieves the instructor using the ID, raises an exception if the instructor is not found, employs the crud module's delete_instructor function with the session and instructor to be deleted, and returns a message confirming the successful deletion.
      
      These functions serve as intermediaries between the API endpoints and the CRUD operations defined in the crud module. They handle database sessions, execute data retrieval, creation, update, and deletion operations, and appropriately handle exceptions when required.

CRUD OPERATIONS IN CRUD.PY

The crud.py file encapsulates CRUD (Create, Read, Update, Delete) operations for the instructor model.

      get_instructor(db: Session, instructor_id: int): Retrieves an instructor from the database based on the specified instructor_id. It utilizes the SQLAlchemy ORM to query the Instructor model, employing joinedload to eagerly load the instructor's qualifications and minimize database queries. The function returns the first matching instructor or None if not found.
      
      get_all_instructors(db: Session): Retrieves all instructors from the database. It performs a query on the Instructor model, eagerly loading the qualifications. The function returns a list of all instructors.
      
      create_instructor(db: Session, instructor: InstructorCreate): Creates a new instructor in the database based on the provided instructor data. It takes a database session and an InstructorCreate object as input. The function generates Qualification objects from the qualifications in the instructor data. It then creates an Instructor object with the remaining data, adds it to the session, commits the transaction, refreshes the instructor object, and returns it.
      
      update_instructor(db: Session, instructor: Instructor, instructor_update: InstructorUpdate): Updates an existing instructor in the database. It takes a database session, the instructor to update, and an InstructorUpdate object as input. The function deletes the existing qualifications associated with the instructor, updates the remaining fields based on the update data, creates new Qualification objects from the updated qualifications, assigns them to the instructor, commits the transaction, refreshes the instructor object, and returns it.
      delete_instructor(db: Session, instructor: Instructor): Deletes an instructor from the database. It takes a database session and the instructor object to delete as input. The function removes the instructor object from the session and commits the transaction.

SQLALCHEMY MODELS IN MODEL.PY

The model.py file introduces two SQLAlchemy models: Qualification and Instructor.

QUALIFICATION MODEL

      Represents the qualifications of an instructor. Contains the following columns: id (primary key), education, institution, and instructor_id (foreign key referencing the id column of the Instructor model). This model defines the structure and relationships of the qualifications table in the database.
      
INSTRUCTOR MODEL

      Represents an instructor. Contains several columns, including id (primary key), first_name, last_name, pps_number (with a unique constraint), email (with a unique constraint), phone, address, eir_code, city, county, and country. It establishes a one-to-many relationship with the Qualification model through the qualifications attribute.
      
      The qualifications attribute uses the SQLAlchemy relationship function to define the relationship between instructors and their qualifications.
      These models provide the necessary structure and relationships for storing instructor-related data, including their qualifications. The Instructor model allows for multiple qualifications to be associated with a single instructor.

API ROUTER IN ROUTER.PY

      The router.py file presents an API router for instructors using FastAPI.
      
      GET /: Handles a GET request to retrieve all instructors. Uses the get_user function for user authentication. Returns a response with a list of instructors serialized according to the Instructor schema.
      
      GET /{instructor_id}: Handles a GET request to retrieve a specific instructor by their instructor_id. Uses the get_user function for user authentication. Returns a response with the instructor information serialized according to the Instructor schema.
      
      POST /: Handles a POST request to create a new instructor. Expects the instructor data to be provided in the request body, serialized according to the InstructorCreate schema. Uses the get_user function for user authentication. Returns a response with the created instructor serialized according to the Instructor schema.
      
      PUT /{instructor_id}: Handles a PUT request to update an existing instructor. Expects the instructor_id as a path parameter and the updated instructor data in the request body, serialized according to the InstructorUpdate schema. Uses the get_user function for user authentication. Returns a response with the updated instructor serialized according to the Instructor schema.
      
      DELETE /{instructor_id}: Handles a DELETE request to delete an instructor. Expects the instructor_id as a path parameter. Uses the get_user function for user authentication. Returns a response indicating the success of the deletion. These endpoints facilitate CRUD operations for managing instructors. They authenticate users using the get_user function and invoke corresponding functions from the controller module to perform database operations.

PYDANTIC MODELS IN SCHEMA.PY

      The schema.py file presents Pydantic models that define the instructor schema.
      
      QUALIFICATION: Represents an instructor's qualifications. Contains fields for education and institution. The Config class with orm_mode=True enables the model to be used for input and output data in ORM mode.

      INSTRUCTORBASE: Represents the common fields of an instructor. Includes personal information such as name, contact details, address, and a list of Qualification objects. Derived from InstructorBase.

      INSTRUCTORCREATE: Derived from InstructorBase. Represents the data required to create a new instructor.
      
      INSTRUCTORUPDATE: Derived from InstructorBase. Represents the data required to update an existing instructor.
      
      INSTRUCTOR: Derived from InstructorBase. Includes an additional id field representing the instructor's unique identifier. The Config class with orm_mode=True enables the model to be used for input and output data in ORM mode. These Pydantic models establish the structure and validation rules for instructor-related data in our FastAPI application. They facilitate data serialisation, deserialisation, input validation, and provide clear data schemas for API documentation and automatic generation of OpenAPI schemas.

THE “STUDENT” FOLDER

      The implementation of CRUD (Create, Read, Update, Delete) operations for student entities is facilitated through the controller.py and crud.py files.
      The controller.py file contains functions that enable interaction with student data, while the crud.py file handles the actual CRUD operations using SQLAlchemy and the provided Student model and schema.
      Furthermore, the model.py file defines the structure of the Student model, and the schema.py file provides Pydantic models for the Student resource.
      The implementation shares similarities with the Instructors' CRUD operations, considering the specific data requirements associated with students.


FUNCTIONALITIES IMPLEMENTED AND SCOPE OF THE SYSTEM DESIGN

      The system design report outlines the current stage of development for the application. The functionalities that have been successfully implemented include login and authentication, managing a list of students and instructors, registering students, viewing and editing student profiles, and performing various actions related to student and instructor management.
      However, it is important to note that additional desired functions such as Course Management, Attendance and Grade Tracking, Financial Management, and Communication Tools are currently out of scope. These functions require more development time and are not included in the current system design.

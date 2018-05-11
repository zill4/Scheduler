package api.Athena.model;

import org.springframework.data.annotation.Id;
import org.springframework.data.mongodb.core.mapping.Document;

@Document(collection = "Courses")
public class Course {

    /*
    COURSE MATH1A
    CRN": "30202",
               "Crse": "F001A",
               "Sec": "07",
               "Cmp": "FH",
               "Cred": "5.000",
               "Title": "CALCULUS",
               "Days": "TR",
               "Time": "06:00 pm-08:15 pm",
               "Cap": "40",
               "Act": "38",
               "WL Cap": "10",
               "WL Act": "0",
               "Instructor": "Yuh,Ni",
               "Date": "01/08-03/30",
               "Location": "FH 4606",
               "Attribute": "Comm and Analytical Thinking",
               "Lab Time": []
               "Lab Time": [
                  {
                     "Days": "F",
                     "Time": "10:00 am-10:50 am",
                     "Instructor": "Young,Hee,Park,Lee",
                     "Date": "01/08-03/30",
                     "Location": "FH 4603"
                  }
               ]
     */
    private final String crn;
    @Id
    private final String courseCode;
    //Id number for map look up.
    private final String section; //idk if this is necessary.
    private final String campus;
    private final float credits;
    private final String title;
    private final String days; //Also probably should make a map accessible day object.
    private final String time; //Probably should make a time object.



    private final int studentCap;
    private int studentActual; //idk if this is necessary.
    private final int waitlistCap;
    private int waitlistAct; //idk if this is necessary.
    private final String instructor; //need to link with RMP
    private final String date; //Should include in time object.
    private final String location; //Would be cool if we could make a location/GPS/Map based obj.
    private final String attribute; //This is like a message, about the class;
    private  Lab lab; //idk if this is the best implementation. but I like the object


    public Course(String crn, String courseCode, String section, String campus, float credits, String title, String days,
                  String time, int studentCap, int waitlistCap, String instructor, String date, String location,
                  String attribute, Lab lab) {
        this.crn = crn;
        this.courseCode = courseCode;
        this.section = section;
        this.campus = campus;
        this.credits = credits;
        this.title = title;
        this.days = days;
        this.time = time;
        this.studentCap = studentCap;
        this.waitlistCap = waitlistCap;
        this.instructor = instructor;
        this.date = date;
        this.location = location;
        this.attribute = attribute;
        this.lab = lab;
    }

    public Course(String crn, String courseCode, String section, String campus, float credits, String title, String days,
                  String time, int studentCap, int waitlistCap, String instructor, String date, String location,
                  String attribute) {
        this.crn = crn;
        this.courseCode = courseCode;
        this.section = section;
        this.campus = campus;
        this.credits = credits;
        this.title = title;
        this.days = days;
        this.time = time;
        this.studentCap = studentCap;
        this.waitlistCap = waitlistCap;
        this.instructor = instructor;
        this.date = date;
        this.location = location;
        this.attribute = attribute;

    }
    public String getCrn(){
        return crn;
    }

    public String getCourseCode() {
        return courseCode;
    }

    public String getSection() {
        return section;
    }

    public String getCampus() {
        return campus;
    }

    public float getCredits() {
        return credits;
    }

    public String getTitle() {
        return title;
    }

    public String getDays() {
        return days;
    }

    public String getTime() {
        return time;
    }

    public int getStudentCap() {
        return studentCap;
    }

    public int getStudentActual() {
        return studentActual;
    }

    public int getWaitlistCap() {
        return waitlistCap;
    }

    public int getWaitlistAct() {
        return waitlistAct;
    }

    public String getInstructor() {
        return instructor;
    }

    public String getDate() {
        return date;
    }

    public String getLocation() {
        return location;
    }

    public String getAttribute() {
        return attribute;
    }

    public Lab getLab() {
        return lab;
    }

    private class Lab{

        private final String days;
        private final String time;
        private final String Instructor;
        private final String date;
        private final String location;

        public Lab(String days, String time, String instructor, String date, String location) {
            this.days = days;
            this.time = time;
            Instructor = instructor;
            this.date = date;
            this.location = location;
        }


        public String getDays() {
            return days;
        }

        public String getTime() {
            return time;
        }

        public String getInstructor() {
            return Instructor;
        }

        public String getDate() {
            return date;
        }

        public String getLocation() {
            return location;
        }
    }

}


package app.athena.restapi.model;

import org.springframework.data.annotation.Id;
import org.springframework.data.annotation.TypeAlias;
import org.springframework.data.mongodb.core.mapping.Document;


@Document(collection ="courses")
@TypeAlias("course")
public class Course {

    @Id
    private  String crn;
    private  String crse;
    //Id number for map look up.
    private  String sec; //idk if this is necessary.
    private  String cmp;
    private String cred;
    private  String title;
    private  String days; //Also probably should make a map accessible day object.
    private  String time; //Probably should make a time object.
    private String cap;
    private String act; //idk if this is necessary.
    private String wl_cap;
    private String wl_act; //idk if this is necessary.
    private  String instructor; //need to link with RMP
    private  String date; //Should include in time object.
    private  String location; //Would be cool if we could make a location/GPS/Map based obj.
    private  String attribute; //This is like a message, about the class;
    private  String lab_days;
    private  String lab_time;
    private  String lab_instructor;
    private  String lab_date;
    private  String lab_location;

    public Course(){}


    public Course(String crn, String crse, String sec, String cmp, String cred, String title, String days, String time, String cap, String act, String wl_cap, String wl_act, String instructor, String date, String location, String attribute, String lab_days, String lab_time, String lab_instructor, String lab_date, String lab_location) {
        this.crn = crn;
        this.crse = crse;
        this.sec = sec;
        this.cmp = cmp;
        this.cred = cred;
        this.title = title;
        this.days = days;
        this.time = time;
        this.cap = cap;
        this.act = act;
        this.wl_cap = wl_cap;
        this.wl_act = wl_act;
        this.instructor = instructor;
        this.date = date;
        this.location = location;
        this.attribute = attribute;
        this.lab_days = lab_days;
        this.lab_time = lab_time;
        this.lab_instructor = lab_instructor;
        this.lab_date = lab_date;
        this.lab_location = lab_location;
    }


    public String getLab_days() {
        return lab_days;
    }

    public void setLab_days(String lab_days) {
        this.lab_days = lab_days;
    }

    public void setLab_time(String lab_time) {
        this.lab_time = lab_time;
    }
    public String getLab_time(){ return this.lab_time;}

    public String getLab_instructor() {
        return lab_instructor;
    }

    public void setLab_instructor(String lab_instructor) {
        this.lab_instructor = lab_instructor;
    }

    public String getLab_date() {
        return lab_date;
    }

    public void setLab_date(String lab_date) {
        this.lab_date = lab_date;
    }

    public String getLab_location() {
        return lab_location;
    }

    public void setLab_location(String lab_location) {
        this.lab_location = lab_location;
    }


    public String getCrn() {
        return crn;
    }

    public void setCrn(String crn) {
        this.crn = crn;
    }

    public String getCrse() {
        return crse;
    }

    public void setCrse(String crse) {
        this.crse = crse;
    }

    public String getSec() {
        return sec;
    }

    public void setSec(String sec) {
        this.sec = sec;
    }

    public String getCmp() {
        return cmp;
    }

    public void setCmp(String cmp) {
        this.cmp = cmp;
    }

    public String getCred() {
        return cred;
    }

    public void setCred(String cred) {
        this.cred = cred;
    }

    public String getTitle() {
        return title;
    }

    public void setTitle(String title) {
        this.title = title;
    }

    public String getDays() {
        return days;
    }

    public void setDays(String days) {
        this.days = days;
    }

    public String getTime() {
        return time;
    }

    public void setTime(String time) {
        this.time = time;
    }

    public String getCap() {
        return cap;
    }

    public void setCap(String cap) {
        this.cap = cap;
    }

    public String getAct() {
        return act;
    }

    public void setAct(String act) {
        this.act = act;
    }

    public String getWl_cap() {
        return wl_cap;
    }

    public void setWl_cap(String wl_cap) {
        this.wl_cap = wl_cap;
    }

    public String getWl_act() {
        return wl_act;
    }

    public void setWl_act(String wl_act) {
        this.wl_act = wl_act;
    }

    public String getInstructor() {
        return instructor;
    }

    public void setInstructor(String instructor) {
        this.instructor = instructor;
    }

    public String getDate() {
        return date;
    }

    public void setDate(String date) {
        this.date = date;
    }

    public String getLocation() {
        return location;
    }

    public void setLocation(String location) {
        this.location = location;
    }

    public String getAttribute() {
        return attribute;
    }

    public void setAttribute(String attribute) {
        this.attribute = attribute;
    }


}


/*

COURSE MATH1A
    CRN": "30202",
    "Crse": "F001A",
    "Sec": "07",
    "Cmp": "FH",
    "Cred": "5.000",
    "Title": "CALCULUS",
               "Days": "TR",
               "Calendar": "06:00 pm-08:15 pm",
               "Cap": "40",
               "Act": "38",
               "WL Cap": "10",
               "WL Act": "0",
               "Instructor": "Yuh,Ni",
               "Date": "01/08-03/30",
               "Location": "FH 4606",
               "Attribute": "Comm and Analytical Thinking",
               "Lab Calendar": []
               "Lab Calendar": [
                  {
                     "Days": "F",
                     "Calendar": "10:00 am-10:50 am",
                     "Instructor": "Young,Hee,Park,Lee",
                     "Date": "01/08-03/30",
                     "Location": "FH 4603"
                  }
               ]
 */
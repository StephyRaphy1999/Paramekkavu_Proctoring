$(document).ready(function(){
  $("input[type=submit]").on("click",function(){
    fname=$("input[name=fname]").val()
    lname=$("input[type=lname]").val()
    gender=$("select[name=gender]").val()
    dob=$("input[type=dob]").val()
    email=$("input[type=email]").val()
    contact=$("input[type=contact]").val()
    password=$("input[type=password]").val()
    admission=$("input[type=admission]").val()
    department=$("select[name=department]").val()
    sem=$("select[name=sem]").val()



    if(fname==""){
        alert("Please enter first name");
        return false;
    }
    if(lname==""){
        alert("Please enter last name");
        return false;
    }
    if(gender==null){
        alert("Please select your gender");
        return false;
    }
    if(dob==""){
        alert("Please enter your date of birth");
        return false;
    }
    if(email==""){
        alert("Please enter your email");
        return false;
    }
    if(contact==""){
        alert("Please enter your phone number");
        return false;
    }
    if(password==""){
        alert("Please enter your password");
        return false;
    }
    if(admission==""){
        alert("Please enter your admission number");
        return false;
    }
    if(department==null){
        alert("Please select your department");
        return false;
    }
    if(sem==null){
        alert("Please select your semester");
        return false;
    }
  })
})
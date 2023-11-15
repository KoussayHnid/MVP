function firstname(){
    var firstname=document.getElementById("firstname");
    
    if(firstname.value.length>0){
    for (let i = 0; i < firstname.value.length; i++){
        if((firstname.value.charAt(i).toUpperCase()<"A")||(firstname.value.charAt(i).toUpperCase()>"Z")){
        alert("Enter a first name");
        return false;
    }
}
return true;
}
else{
alert("Enter a first name");
return false;
}
}

function lastname(){
    var lastname=document.getElementById("lastname");
    
    if(lastname.value.length>0){
    for (let i = 0; i < lastname.value.length; i++){
        if((lastname.value.charAt(i).toUpperCase()<"A")||(lastname.value.charAt(i).toUpperCase()>"Z")){
        alert("Enter a last name");
        return false;
    }
}
return true;
}
else{
alert("Enter a last name");
return false;
}
}

function email(){
    var email=document.getElementById("email");

if((!email.value)||(email.value.indexOf("@")<1)||(email.value.indexOf(".")<0)||(email.value.charAt(0).toUpperCase()<"A" )||(email.value.charAt(0).toUpperCase()>"Z"))
{
    alert("Enter an email");
    return false;
}
else
return true;
}

function pwd(){
    var pwd=document.getElementById("pwd");

    if(pwd.value.length<8) 
{
   alert("Enter a password");
   return false;
}
return true;
}


function confpwd(){
    var pwd=document.getElementById("pwd");
    var confpwd=document.getElementById("confpwd");

    if(pwd.value!=confpwd.value) 
{
   alert("Both password fields must match");
   return false;
}
return true;
}

function birthday(){
    var birthday=document.getElementById("birthday");

    if(!birthday.value) 
{
   alert("Enter a birthday");
   return false;
}
return true;
}

function gender(){
    var male=document.getElementById("male");
    var female=document.getElementById("female");
if((!male.checked)&&(!female.checked)){
    alert("check a gender");
    return false;
 }
 return true;
 }




function controle(){
    var b=document.getElementById("post1");
    if(firstname() && lastname() && email() && pwd() && confpwd() && birthday() && gender()){
         b.href="post2.html";

}   
}

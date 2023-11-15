function email(){
    var email=document.getElementById("email");

if((!email.value)||(email.value.indexOf("@")<1)||(email.value.indexOf(".")<email.value.indexOf("@"))||(email.value.charAt(0).toUpperCase()<"A" )||(email.value.charAt(0).toUpperCase()>"Z"))
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


function controle(){
    return(email() && pwd());
         
 
}
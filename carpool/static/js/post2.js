function From(){
var from =document.getElementById("from").value;
if (!from){
    alert("Enter a start location");
    return false;
}
return true;
}

function to(){
    var to =document.getElementById("to").value;
    if (!to){
        alert("Enter a destination");
        return false;
    }
    return true;
}

function datetime(){
    var datetime=document.getElementById("datetime");

    if(!datetime.value) 
{
   alert("Enter date and time");
   return false;
}
return true;
}

function car(){
    var car =document.getElementById("carbrand").value;
    if (!car){
        alert("Enter a car brand");
        return false;
    }
    return true;
}


function passengers(){
    var passengers =document.getElementById("passengers").value;
    if ((!passengers)||(isNaN(passengers))||(passengers.length <4)){
        alert("Enter the number of seats available");
        return false;
    }
    return true;
}

function price(){
    var price =document.getElementById("price").value;
    if ((!price)||(isNaN(price))){
        alert("Enter a price");
        return false;
    }
    return true;
}

function number(){
    var number =document.getElementById("phone").value;
    if ((number.length <8)||(isNaN(number))){
        alert("Enter a phone number");
        return false;
    }
    return true;
}



function checke(){
    var check=document.getElementById("check");
    var button=document.getElementById("button");
if(check.checked){
    button.disabled=false;
 }
 else{
    button.disabled=true;
    
 }
}



function controle(){
    if(from() && to() && datetime() && car() && passengers() && price() && number() ){
    return true;
}   
}

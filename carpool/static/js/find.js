
function from(){
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

    function passengers(){
        var passengers =document.getElementById("passengers").value;
        if ((!passengers)||(isNaN(passengers))){
            alert("Enter the number of seats available");
            return false;
        }
        return true;
    }

    function controle(){
        var b=document.getElementById("button");
    if(from() && to() && datetime() && passengers()){
         if((document.getElementById("from").value=="gabes")&&(document.getElementById("to").value=="tunis")){
            b.href="gabes.html";
        }
         return true;
} 
    return false;
}
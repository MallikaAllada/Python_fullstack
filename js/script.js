alert("Welcome to NRIIT learning management system")
let heading=document.getElementById("welcome");
heading.innerHTML = "Welcome  Future Software Engineers"
console.log("Heading Element:", heading) 
let msg=document.getElementById("message")
msg.innerHTML="Javascript is fun"
console.log("Message element:",msg)
function showmessage(){
    alert("Welcome to NRIIT Learning management System")
}
function ChangeHeading(){
    document.getElementById("welcome").innerHTML="Welcome to Python Fullstack Develepors"
}
let heading=document.querySelector("#welcome");
console.log("Heading element:", heading)
let button=document.getElementById("btnGreeting");
button.addEventListener("click", function(){
    alert("Welcome to Javascript Event Handling");
});

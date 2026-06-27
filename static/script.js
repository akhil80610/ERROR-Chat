async function sendPrompt() {

const prompt=document.getElementById("prompt").value;

const responseDiv=document.getElementById("response");

responseDiv.innerHTML="Thinking...";

const response=await fetch("/predict",{

method:"POST",

headers:{
"Content-Type":"application/json"
},

body:JSON.stringify({
prompt:prompt
})

});

const data=await response.json();

responseDiv.innerHTML = marked.parse(data.response);

}
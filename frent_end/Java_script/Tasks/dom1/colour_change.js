const doc = document;
const h1=doc.createElement("h1")
h1.style.width="200px"
h1.style.height="200px"
h1.style.backgroundColor="red"

doc.body.appendChild(h1)


const colour = ["blue", "black", "yellow", "pink", "orange", "gray","gold"]

function Randoms(){
    const index= Math.floor(Math.random()*colour.length)
return colour[index]
}

function read(){
    const colour=Randoms()
    h1.style.backgroundColor=colour;
    doc.querySelector("h2").textContent=`Colour is :${colour}`
}

// function read() {
//     doc.body.style.backgroundColor = mode();
// }
doc.querySelector(".change").addEventListener("click", read);

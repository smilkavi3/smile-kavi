const doc = document;
// doc.body.className="center"//value  center style to html body file( value , toggle ,remove this are class inbuild)

function count() {
    // console.log("click increment")
    let value = Number(doc.querySelector(".value").textContent)
    doc.querySelector(".value").textContent = ++value
}

function uncount() {
    // console.log("click decrement")
    let value = Number(doc.querySelector(".value").textContent)
    if (value > 0) doc.querySelector(".value").textContent = --value
}

function reset() {
    // console.log("click reset")
    let value = Number(doc.querySelector(".value").textContent)
    doc.querySelector(".value").textContent = 0
}
doc.body.classList.add("center")

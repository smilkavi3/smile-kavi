const doc = document


const div = doc.createElement("div")
const div1 = doc.createElement("div")
const h1 = doc.createElement("h1")
const h2 = doc.createElement("h2")

h1.textContent = "OUR MENU"
h2.textContent = "________"
div1.append(h1, h2);
div1.className = "top"
div.className = "main"
div.classList.add("main")
div1.classList.add("top")
div.append(div1)
doc.body.append(div)

//create list items

const div2 = doc.createElement("div")
const ul = doc.createElement("ul")

ul.classList.add("container")

// ul.className="container"

// const button1=doc.createElement("button")
// const button2=doc.createElement("button")
// const button3=doc.createElement("button")
// const button4=doc.createElement("button")
// const button5=doc.createElement("button")

// // button1.addEventListener("click",function(){
// //    alert("button is click")
// // })
// button1.textContent="All"
// button2.textContent="Break fast"
// button3.textContent="Lunch"
// button4.textContent="Shakes"
// button5.textContent="Diner"

// ul.append(button1,button2,button3,button4,button5)

// div2.append(ul)
// div.append(div2)


// const div3=doc.createElement("div");
// const div4=doc.createElement("div");
// const div5=doc.createElement("div");
// const div6=doc.createElement("div");
// const div7=doc.createElement("div");
// const div8=doc.createElement("div");
// const div9=doc.createElement("div");
// const div10=doc.createElement("div");
// const image=doc.createElement("img");
// const para=doc.createElement("p");


// div3.className="recipes";
// div4.className="receip";
// div5.className="one";
// div6.className="two";
// div7.className="np";
// div8.className="name";
// div9.className="amount";
// div10.className="line";


// div8.textContent="Godzilla Milkshake";
// div9.textContent="$15.99";
// div10.textContent=".......................................................................";

// para.textContent="Lorem ipsum dolor sit amet consectetur, adipisicing elit. Voluptas facere ipsam sint, ab culpa inventore sunt molestias deserunt sit, reprehenderit blanditiis deleniti fugit voluptate unde? Ipsum ipsa quasi quod sed?"

// image.src=""
// image.style.width="130px"
// image.style.height="130px"
// div5.append(image);
// div7.append(div8,div9);
// div6.append(div7,div10,para);
// div4.append(div5,div6)
// div3.append(div4)
// div.append(div3)


// // const div3=doc.createElement("div");
// const div11=doc.createElement("div");
// const div12=doc.createElement("div");
// const div13=doc.createElement("div");
// const div14=doc.createElement("div");
// const div15=doc.createElement("div");
// const div16=doc.createElement("div");
// const div17=doc.createElement("div");
// const image2=doc.createElement("img");
// const para2=doc.createElement("p");


// // div3.className="recipes";
// div11.className="receip";
// div12.className="one";
// div13.className="two";
// div14.className="np";
// div15.className="name";
// div16.className="amount";
// div17.className="line";


// div15.textContent="Godzilla Milkshake";
// div16.textContent="$15.99";
// div17.textContent=".......................................................................";

// para2.textContent="Lorem ipsum dolor sit amet consectetur, adipisicing elit. Voluptas facere ipsam sint, ab culpa inventore sunt molestias deserunt sit, reprehenderit blanditiis deleniti fugit voluptate unde? Ipsum ipsa quasi quod sed?"

// image2.src=""
// image2.style.width="130px"
// image2.style.height="130px"
// div12.append(image2);
// div14.append(div15,div16);
// div13.append(div14,div17,para2);
// div3.append(div12,div13);


// const div18=doc.createElement("div");
// const div19=doc.createElement("div");
// const div20=doc.createElement("div");
// const div21=doc.createElement("div");
// const div22=doc.createElement("div");
// const div23=doc.createElement("div");
// const div24=doc.createElement("div");
// const image3=doc.createElement("img");
// const para3=doc.createElement("p");


// // div3.className="recipes";
// div18.className="receip";
// div19.className="one";
// div20.className="two";
// div21.className="np";
// div22.className="name";
// div23.className="amount";
// div24.className="line";


// div22.textContent="Godzilla Milkshake";
// div23.textContent="$15.99";
// div24.textContent=".......................................................................";

// para3.textContent="Lorem ipsum dolor sit amet consectetur, adipisicing elit. Voluptas facere ipsam sint, ab culpa inventore sunt molestias deserunt sit, reprehenderit blanditiis deleniti fugit voluptate unde? Ipsum ipsa quasi quod sed?"

// image3.src=""
// image3.style.width="130px"
// image3.style.height="130px"
// div19.append(image3);
// div21.append(div22,div23);
// div20.append(div21,div24,para3);
// div3.append(div19,div20);

const categories = ["All", "Breakfast", "Lunch", "Shakes", "Dinner"]

for (let i = 0; i < categories.length; i++) {
    const button = doc.createElement("button")
    button.textContent = categories[i]
    ul.appendChild(button)
}

div2.append(ul)
div.append(div2)

function createReceipes(name, price, description, image, category) {
    const div4 = doc.createElement("div");
    const div5 = doc.createElement("div");
    const div6 = doc.createElement("div");
    const div7 = doc.createElement("div");
    const div8 = doc.createElement("div");
    const div9 = doc.createElement("div");
    const div10 = doc.createElement("div");
    const images = doc.createElement("img");
    const para = doc.createElement("p");


    // div3.className = "recipes";
    div4.className = "receip";
    div4.setAttribute("data-category", category)
    div5.className = "one";
    div6.className = "two";
    div7.className = "np";
    div8.className = "name";
    div9.className = "amount";
    div10.className = "line";


    div8.textContent = name;
    div9.textContent = `$${price}`;
    div10.textContent = ".......................................................................";

    para.textContent = description


    images.src = image;
    images.alt = "image";
    images.style.width = "150px"
    images.style.height = "150px"
    div5.append(images);
    div7.append(div8, div9);
    div6.append(div7, div10, para);
    div4.append(div5, div6)

    return div4
}


const div3 = doc.createElement("div");
div3.className = "recipes"

const recip = [
    { name: "Godzilla Milkshake", price: "15.99", description: "Lorem ipsum dolor sit amet consectetur, adipisicing elit. Voluptas facere ipsam sint, ab culpa inventore sunt molestias deserunt sit, reprehenderit blanditiis deleniti fugit voluptate unde? Ipsum ipsa quasi quod sed?", imageUrl: "https://shorturl.at/9UV4e", category: "Shakes" },

    { name: "Shark Bite Smoothie", price: "12.99", description: "Lorem ipsum dolor sit amet consectetur, adipisicing elit. Voluptas facere ipsam sint, ab culpa inventore sunt molestias deserunt sit, reprehenderit blanditiis deleniti fugit voluptate unde? Ipsum ipsa quasi quod sed?", imageUrl: "https://shorturl.at/9UV4e", category: "Dinner" },

    { name: "Mega Burger", price: "19.99", description: "Lorem ipsum dolor sit amet consectetur, adipisicing elit. Voluptas facere ipsam sint, ab culpa inventore sunt molestias deserunt sit, reprehenderit blanditiis deleniti fugit voluptate unde? Ipsum ipsa quasi quod sed?", imageUrl: "https://shorturl.at/9UV4e", category: "Lunch" },

    { name: "Pancakes Deluxe", price: "9.99", description: "Lorem ipsum dolor sit amet consectetur, adipisicing elit. Voluptas facere ipsam sint, ab culpa inventore sunt molestias deserunt sit, reprehenderit blanditiis deleniti fugit voluptate unde? Ipsum ipsa quasi quod sed?", imageUrl: "https://shorturl.at/9UV4e", category: "Breakfast" },

    { name: "Dinner Special", price: "24.99", description: "Lorem ipsum dolor sit amet consectetur, adipisicing elit. Voluptas facere ipsam sint, ab culpa inventore sunt molestias deserunt sit, reprehenderit blanditiis deleniti fugit voluptate unde? Ipsum ipsa quasi quod sed?", imageUrl: "https://shorturl.at/9UV4e", category: "Dinner" }
];  

for (let j = 0; j < recip.length; j++) {
    const itmes = createReceipes(recip[j].name, recip[j].price, recip[j].description, recip[j].imageUrl, recip[j].category)
    console.log();


    div3.appendChild(itmes)
    div.append(div3)
}

const butt = doc.querySelectorAll("button")


for (let k = 0; k < butt.length; k++) {
    butt[k].addEventListener('click', function () {
        const varity = butt[k].textContent
        console.log(varity);

        showfinal(varity)
    })
}

showfinal("All")
function showfinal(varity){
    const itme = doc.querySelectorAll(".receip")
    // console.log(itme[1]);
    for (let l=0;l<itme.length;l++){
        
        if("All"===varity){
            itme[l].style.display="flex"
        }else{
            for(let m=0;m<itme.length;m++){
                const data=itme[m].getAttribute("data-category")
                // console.log(String(data));
                
                if(varity===data){
                    itme[m].style.display="flex"
                    // console.log("shake");
                    
                }else{
                    itme[m].style.display="none"
                }
            
            }
            
        }
          
    }

}

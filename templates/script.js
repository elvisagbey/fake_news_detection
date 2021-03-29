 let buttton = document.querySelector ("My_function");
 let div = document.querySelector("Predict");

buttton.addEventListener ("click",() =>{
	if (div.style.display === "none"){
			div.style.display = "block";
	}else{
		div.style.display = "none";
	}
})
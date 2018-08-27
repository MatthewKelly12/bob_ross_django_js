let clicker = document.getElementById("butt")


clicker.addEventListener('click', function () {
	$.ajax("/birthdays").then(birthdays => {
		birthdays.forEach(birthday => {
		console.log(birthday)
		let bd = `<div>
		<p>${birthday.name} ${birthday.date} ${birthday.time} ${birthday.greeting}</p>
		</div>`
		$("#bdDiv").append(bd)
		});
	}
)
	console.log('clicked it')
})



// make an http request to get info
// url: /birdthdays
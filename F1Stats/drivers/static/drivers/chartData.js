function processChartData() {
    console.log(document.getElementById("lbls"))
    console.log(document)
	let lbls = JSON.parse(document.getElementById("lbls").textContent);
	let races = JSON.parse(document.getElementById('results').textContent);
	console.log(races)
	console.log(lbls);
	const ctx = document.getElementById('canvasRecentPerf').getContext('2d');

	let lineChart = new Chart(ctx, {
	    type: 'line',
	    data:{
	        labels: lbls,
            datasets: [{
            data: races,
            label: "Bottas",
            fill: false}],
        },
        options: {
            scales: {
            yAxes: [{
                ticks: {
                beginAtZero: true
                }
                }]
            },
            elements: {
                line: {
                    tension: 0
                }
            },
            hoverMode: 'index',
            title: {
                display: true,
                text: 'Recent Performance',
                fontColor: '#666',
                fontSize: 40
            }
        }
    })
}

processChartData()

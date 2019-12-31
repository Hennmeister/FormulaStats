function processChartData() {
	let lbls = JSON.parse(document.getElementById("lbls").textContent);
	let races = JSON.parse(document.getElementById("results").textContent);
	//let d = JSON.parse(document.getElementById('driver').textContent);
	const ctx = document.getElementById('canvasRecentPerf').getContext('2d');

	let lineChart = new Chart(ctx, {
	    type: 'line',
	    data:{
	        labels: lbls,
            datasets: [{
            data: races,
            fill: false}],
        },
        options: {
            legend: {
                display: false
            },
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
            },
            responsive: false
        }
    })
}

processChartData()

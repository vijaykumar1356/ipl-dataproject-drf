function solution4(event){
    event.preventDefault();
    // getting form data
    const formData = new FormData(event.target);
    // converting form data as url parameters for a get request from api
    const urlParams = new URLSearchParams(formData).toString()
    fetch("http://127.0.0.1:8000/app/api/problem4?"+urlParams)
        .then(response => response.json())
        .then(data => {
            loadDataProblem4(data)
        })
}

function loadDataProblem4(data) {
    let years = data['years'];
    let teams = data['teams'];
    let matches_played = data['matches_played'];
    let seriesData = [];
    for (var i=years.length-1; i>=0; i--)
        {
            seriesData.push({name:years[i], data:matches_played[i]})
        }
    console.log(seriesData)
    Highcharts.chart('output', {
        chart:{type:'column'},
        title:{text: 'Stacked data of No. of Matches Playedby each Team Season wise'},
        subtitle: {text: `${years[0]} - ${years[years.length-1]}`},
        xAxis: {categories: teams},
        yAxis:{
            min: 0,
            title:{text: 'Seasons'},
            stackedLabels:{enabled: true, 
            style:{
                fontWeight: 'bold',
                color: ( // theme
                    Highcharts.defaultOptions.title.style &&
                    Highcharts.defaultOptions.title.style.color
                ) || 'gray'
            },
            },
        },

        tooltip: {
            headerFormat: '<b>{point.x}</b><br/>',
            pointFormat: '{series.name}: {point.y}<br/>Total: {point.stackTotal}'
        },
        plotOptions:{
            column: {
                stacking: 'normal',
            }
        },
        series: seriesData
    })
}

function solution3(event){
    event.preventDefault();
    const formData = new FormData(event.target);
    const urlParams = new URLSearchParams(formData).toString()
    fetch("http://127.0.0.1:8000/app/api/problem3?"+urlParams)
        .then(response => response.json())
        .then(data => {
            loadDataProblem3(data)
        })
}
function loadDataProblem3(data){
    let countries = data.countries
    let umpires_count = data.count
    console.log(countries, umpires_count)
    Highcharts.chart('output', {
        chart: {
            type: 'column',
        },
        title: {
            text: 'Countries - No of Umpires represented in IPL'
        },
        xAxis: {
            categories: countries ,         
        },
        yAxis: {
            title: {
                text: 'No. of Umpires from each Country'
            },
            tickInterval:5,
        },
        series: [{
            name: 'No. of Umpires',
            data: umpires_count
        }]
    });
}


function solution1(event){
    event.preventDefault();
    const formData = new FormData(event.target);
    const urlParams = new URLSearchParams(formData).toString()
    fetch("http://127.0.0.1:8000/app/api/problem1?"+urlParams)
        .then(response => response.json())
        .then(data => {
            loadDataProblem1(data)
        }).catch(error => {
            console.log(error)
        })
}

function loadDataProblem1(data) {
    if (data.length == 0){
        document.getElementById("output").innerText = "No data for that team in that year!"
        return
    }
    let teams = []
    let scores = []
    for (const obj of data){
        teams.push(obj.batting_team)
        scores.push(obj.sum_score)
    }
    Highcharts.chart('output', {
        chart: {
            type: 'column',
        },
        title: {
            text: 'IPL Teams vs Total Runs Scored in Year Range'
        },
        subtitle:{
            text: "Selected Seasons",
        },
        xAxis: {
            categories: teams ,         
        },
        yAxis: {
            title: {
                text: 'Runs Scored by each Team'
            },
            tickInterval:2500,

        },
        series: [{
            name: 'Runs scored',
            data: scores
        }]
    });
}

function solution2(event){
    event.preventDefault();
    const formData = new FormData(event.target);
    const urlParams = new URLSearchParams(formData).toString()
    const top = formData.get('top')
    fetch("http://127.0.0.1:8000/app/api/problem2?"+urlParams)
        .then(response => response.json())
        .then(data => {
            loadDataProblem2(data, top);
        }).catch(error => {
            console.log(error)
        })
}

function loadDataProblem2(data, top){
    if (data.length == 0){
        document.getElementById("output").innerText = "No data for that team in that year!"
        return
    }
    let batsmen = []
    let scores = []
    for (const obj of data){
        batsmen.push(obj.batsman)
        scores.push(obj.total_runs)
    }
    Highcharts.chart('output', {
        chart: {
            type: 'column',
        },
        title: {
            text: `Top ${top} Batsmen by runs scored for the team`
        },
        xAxis: {
            categories: batsmen ,         
        },
        yAxis: {
            title: {
                text: 'Total Runs by Batsman'
            },
            tickInterval:50,
        },
        series: [{
            name: 'Runs Scored by Batsman',
            data: scores
        }]
    });
}


